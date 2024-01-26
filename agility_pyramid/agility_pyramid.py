import pyautogui as pag
import time
import os
import json
from randomizers import p, r


def initialize_pag():
    pag.FAILSAFE = True  # Turn on failsafe
    print('Pyautogui failsafe enabled!')


def countdown(seconds=10):
    print(f'Starting', end='')
    for s in range(1, seconds + 1):
        print('.', end='')
        time.sleep(1)
    print(' now!')


def convert_key(key):
    key_map = {
        'alt_l': 'altleft',
        'alt_r': 'altright',
        'alt_gr': 'altright',
        'caps_lock': 'capslock',
        'ctrl_l': 'ctrlleft',
        'ctrl_r': 'ctrlright',
        'page_down': 'pagedown',
        'page_up': 'pageup',
        'shift_l': 'shiftleft',
        'shift_r': 'shiftright',
        'num_lock': 'numlock',
        'print_screen': 'printscreen',
        'scroll_lock': 'scrolllock'}

    # example: 'Key.F9' should return 'F9', 'w' should return as 'w'
    cleaned_key = key.replace('Key.', '')

    if cleaned_key in key_map:
        return key_map[cleaned_key]

    return cleaned_key


def play_actions(filename):
    previous_position = None
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, filename)
    with open(filepath, 'r') as jsonfile:
        data = json.load(jsonfile)
        for index, action in enumerate(data):
            start_time = time.time()
            if action['button'] == 'Key.f10':
                break
            # Perform action
            elif action['type'] == 'KeyDown':
                key = convert_key(action['button'])
                # key = key[4:] if key[:4] == 'Key.' else key
                pag.keyDown(key)
            elif action['type'] == 'KeyUp':
                key = convert_key(action['button'])
                # key = key[4:] if key[:4] == 'Key.' else key
                pag.keyDown(key)

            elif action['type'] == 'clickDown':
                previous_position = (action['pos'][0], action['pos'][1])
                pag.moveTo(action['pos'][0] + p(-4, 4), action['pos'][1] + p(-4, 4), duration=r(0.25, 0.70))
                pag.mouseDown()
            elif action['type'] == 'clickUp':
                if previous_position == (action['pos'][0], action['pos'][1]):
                    pag.mouseUp()
                else:
                    pag.moveTo(action['pos'][0] + p(-4, 4), action['pos'][1] + p(-4, 4), duration=r(0.25, 1.00))
                    pag.mouseUp()

            # Sleep until next action
            try:
                next_action = data[index + 1]
            except IndexError:
                break
            elapsed_time = time.time() - start_time
            wait_time = next_action['time'] - action['time']
            if wait_time >= 0:
                wait_time -= elapsed_time
                if wait_time < 0:
                    wait_time = 0
                if action['type'] == 'clickDown':
                    time.sleep(wait_time)
                else:
                    time.sleep(wait_time + r(0, 0.30))
            else:
                raise Exception('Unexpected action ordering.')


def wait_for(image, c=0.98):
    script_dir = os.path.dirname(__file__)
    img = os.path.join(script_dir, image)
    print('Waiting ', end='')
    while True:
        try:
            pag.locateOnScreen(img, confidence=c)
            print(f' now!')
            break
        except pag.ImageNotFoundException:
            print('.', end='')
            time.sleep(0.25)


def check_position(x, y, rgb, t=5):
    if pag.pixelMatchesColor(x, y, rgb, tolerance=t):
        pass
    else:
        pag.moveTo(972 + p(-4, 4), 535 + p(-4, 4), r(0.25, 0.75))
        pag.click()
        time.sleep(1.5 + r(0, 1))


def main():
    countdown(3)
    initialize_pag()
    play_actions('agility_pyramid_pt1.json')
    time.sleep(4)
    wait_for('pyramid_block_1.png', c=0.98)
    play_actions('agility_pyramid_pt2.json')
    time.sleep(4)
    wait_for('pyramid_block_2.png', c=0.95)
    play_actions('agility_pyramid_pt3.json')
    time.sleep(4)
    check_position(954, 506, (0, 255, 0), 5)
    play_actions('agility_pyramid_pt4.json')
    time.sleep(5)

