import pyperclip
import time
from typing import Callable


def update_clipboard(clip: str) -> None:
    pyperclip.copy(clip)


def listen(callback: Callable[[str], None], exit_callback: Callable[[], None]) -> None:
    try:
        clip = pyperclip.paste()
        while True:
            new_clip = pyperclip.paste()
            if clip != new_clip:
                clip = new_clip
                callback(clip)
                #print(clip)

            time.sleep(0.1)
    
    except KeyboardInterrupt:
        exit_callback()

