import pyperclip
import time

from server import Server


def update_clipboard(clip: str) -> None:
    pyperclip.copy(clip)


def listen(server: Server) -> None:
    clip = pyperclip.paste()
    while True:
        new_clip = pyperclip.paste()
        if clip != new_clip:
            clip = new_clip
            server.update_clipboard(clip)
            print(clip)

        time.sleep(0.1)

