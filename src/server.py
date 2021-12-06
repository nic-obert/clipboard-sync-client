import socket
import threading
import time
import os
from typing import Tuple

from clipboard import update_clipboard


def recvall(sock: socket.socket) -> bytes:
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data


class Server:

    DELAY_SCAN = 0.1

    def __init__(self, address: Tuple[str, int]) -> None:
        self.address = address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False


    def connect(self) -> None:
        self.socket.connect(self.address)
        self.connected = True
        listener = threading.Thread(target=self.listen)
        listener.start()


    def disconnect(self) -> None:
        self.socket.close()
        self.connected = False
        os._exit(0)


    def listen(self) -> None:
        try:
            while self.connected:
                clip = recvall(self.socket)
                if clip:
                    update_clipboard(clip.decode('utf-8'))
                
                time.sleep(self.DELAY_SCAN)
        
        except ConnectionResetError:
            print('Connection reset by peer')
        except ConnectionAbortedError:
            print('Connection aborted')
        except BrokenPipeError:
            print('Broken pipe')

        finally:
            self.disconnect()
            print('Connection closed')
    

    def update_clipboard(self, clip: str) -> None:
        self.socket.sendall(clip.encode('utf-8'))
    
