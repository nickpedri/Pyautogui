import cv2 as cv
import pyautogui as pag
import time
import os
import json
from functions import p, r
import functions

# Done at 0% zoom


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
                    time.sleep(wait_time + r(0, 0.10))
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


def locate_simon():
    timer = time.time()
    pag.screenshot('s1.png', region=(640, 470, 400, 330))
    simon_area = cv.imread('s1.png', cv.IMREAD_UNCHANGED)
    simon = cv.imread('simon_templeton.png', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(simon_area, simon, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    simon_w = simon.shape[1] / 2
    simon_h = simon.shape[0] / 2

    simon_location = (max_loc[0] + 640 + simon_w, max_loc[1] + 470 + simon_h)
    # print(simon_location)
    print(time.time() - timer)
    return simon_location


def trade_with_simon():
    pag.moveTo(811 + p(-4, 4), 555 + p(-4, 4), r(0.25, 0.75))
    pag.click()
    time.sleep(6 + r(0.5, 0.9))

    start_time = time.time()
    elapsed_time = 0
    print('Searching for simon ', end='')

    while elapsed_time < 20:
        simon_movement = [locate_simon(), locate_simon()]
        if simon_movement[-1] == simon_movement[-2]:
            pag.moveTo(simon_movement[-1])
            pag.click()
            print('simon found!')
            # print(simon_movement)
            break
        elapsed_time = time.time() - start_time
        print('.', end='')
    if elapsed_time > 20:
        print('Could not locate simon.')
        # print(elapsed_time)
    else:
        time.sleep(6 + r(0.5, 0.9))
        pag.press('space')
        time.sleep(2 + r(0, 1))
        pag.press('1')
        time.sleep(2 + r(0, 1))
        print('Finished trading!')


def locate_start():
    pag.screenshot('s2.png', region=(0, 0, 1920, 1080))
    start_area = cv.imread('s2.png', cv.IMREAD_UNCHANGED)
    start_tile = cv.imread('start_tile.png', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(start_area, start_tile, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    estimated_start_loc = (max_loc[0], max_loc[1] - 20)
    return estimated_start_loc


def reset_position():
    pag.moveTo(locate_start())
    pag.click()
    time.sleep(5)
    pag.moveTo(974 + p(-4, 4), 536 + p(-4, 4), r(0.25, 0.75))
    pag.click()
    time.sleep(7)
    pag.moveTo(1037 + p(-4, 4), 506 + p(-4, 4), r(0.25, 0.75))
    pag.click()
    time.sleep(5)


def main():
    countdown(3)
    initialize_pag()
    for n in range(1, 66):
        play_actions('agility_pyramid_pt1.json')
        time.sleep(4)
        wait_for('pyramid_block_1.png', c=0.97)

        play_actions('agility_pyramid_pt2.json')
        time.sleep(4)
        wait_for('pyramid_block_2.png', c=0.95)

        play_actions('agility_pyramid_pt3.json')
        time.sleep(6)
        check_position(1140, 440, (255, 0, 0), 5)

        play_actions('agility_pyramid_pt4.json')
        time.sleep(4)
        check_position(954, 506, (0, 255, 0), 5)

        play_actions('agility_pyramid_pt5.json')
        time.sleep(7)
        print(f'Lap {n} done!')

        if n % 3 == 0:
            trade_with_simon()
            reset_position()
        if n % 15 == 0:
            play_actions('fill_water.json')
            time.sleep(5)


main()

# trade_with_simon()
# reset_position()

