from pynput import mouse, keyboard
from time import time

# Declare mouse_listener globally so that keyboard on release can stop it
mouse_listener = None
# Declare start_time globally so that the callback functions can reference it
start_time = None
# Keep track of unreleased keys to prevent over_reporting press events
unreleased_keys = []
# Storing all input events
input_events = []


def record_event(event_type, event_time, button, pos=None):
    global input_events
    input_events.append({'time': event_time,
                         'type': event_type,
                         'button': button,
                         'pos': pos})



def on_press(key):
    # We only want to record first key press event until that key has been released
    global unreleased_keys
    if key in unreleased_keys:
        return
    else:
        unreleased_keys.append(key)
    try:
        print(f'alphanumeric key {key.char} pressed at {elapsed_time()}')
    except AttributeError:
        print(f'special key {key} pressed at {elapsed_time()}')


def on_release(key):
    # Mark key as no longer pressed
    global unreleased_keys
    try:
        unreleased_keys.remove(key)
    except ValueError:
        print(f'ERROR: {key} not in unreleased_keys')
    print(f'{key} released at {elapsed_time()}')
    if key == keyboard.Key.esc:
        # Stop mouse listener
        mouse_listener.stop()
        # Stop keyboard listener
        return False
        # raise keyboard.Listener.StopException


def on_click(x, y, button, pressed):
    if not pressed:
        print(f'Clicked {button} on {(x, y)} at {elapsed_time()}')
        # record_event(EventType.CLICK, elapsed_time(), button, (x, y))


def run_listeners():
    global mouse_listener
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()
    mouse_listener.wait()

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        global start_time
        start_time = time()
        listener.join()


def elapsed_time():
    global start_time
    return time() - start_time


def main():
    run_listeners()


if __name__ == "__main__":
    main()
