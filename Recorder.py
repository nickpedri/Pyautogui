import os
from pynput import mouse, keyboard
from time import time
import json


OUTPUT_FILENAME = 'agility_pyramid_pt_test'
# Declare mouse_listener globally so that keyboard on release can stop it
mouse_listener = None
# Declare start_time globally so that the callback functions can reference it
start_time = None
# Keep track of unreleased keys to prevent over_reporting press events
unreleased_keys = []
# Storing all input events
input_events = []
# Store click event
unreleased_click = False


class EventType:
    KEYDOWN = 'KeyDown'
    KEYUP = 'KeyUp'
    CLICKDOWN = 'clickDown'
    CLICKUP = 'clickUp'
    MOUSEMOVE = 'moveTo'


def record_event(event_type, event_time, button, pos=None):
    global input_events
    input_events.append({'time': event_time,
                         'type': event_type,
                         'button': str(button),
                         'pos': pos})
    if event_type == EventType.CLICKDOWN or event_type == EventType.CLICKUP:
        print(f'{event_type} on {button} pos {pos} at {event_time}')
    else:
        print(f'{event_type} on {button} at {event_time}')


def on_press(key):
    # We only want to record first key press event until that key has been released
    global unreleased_keys
    if key in unreleased_keys:
        return
    else:
        unreleased_keys.append(key)
    try:
        record_event(EventType.KEYDOWN, elapsed_time(), key.char)
    except AttributeError:
        record_event(EventType.KEYDOWN, elapsed_time(), key)


def on_release(key):
    # Mark key as no longer pressed
    global unreleased_keys
    try:
        unreleased_keys.remove(key)
    except ValueError:
        print(f'ERROR: {key} not in unreleased_keys')
    try:
        record_event(EventType.KEYUP, elapsed_time(), key.char)
    except AttributeError:
        record_event(EventType.KEYUP, elapsed_time(), key)

    if key == keyboard.Key.f10:
        # Stop mouse listener
        mouse_listener.stop()
        # Stop keyboard listener
        return False
        # raise keyboard.Listener.StopException


def on_click(x, y, button, pressed):
    if pressed:
        record_event(EventType.CLICKDOWN, elapsed_time(), button, (x, y))
    if not pressed:
        record_event(EventType.CLICKUP, elapsed_time(), button, (x, y))


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
    print(f'Recording duration: {elapsed_time()} seconds')
    global input_events
    print(json.dumps(input_events))

    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, 'recordings', f'{OUTPUT_FILENAME}.json')
    with open(filepath, 'w') as outfile:
        json.dump(input_events, outfile, indent=4)


if __name__ == "__main__":
    main()
