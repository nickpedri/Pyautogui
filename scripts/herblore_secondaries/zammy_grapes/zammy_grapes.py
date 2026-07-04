import functions as f
import pyautogui as pag
import time
import numpy as np
import cv2 as cv


character_position = 'bank'


def set_up():
    f.shift_camera_direction('north')
    pag.moveTo(1140 + f.p(0, 100), 500 + f.p(0, 100), f.r(0, 1))
    pag.scroll(-10000)
    pag.press('f2')



def enter_game():
    f.move_click(945, 285, wait_duration=f.r(10, 12))
    f.move_click(950, 354, wait_duration=f.r(2, 3))


def open_bank():
    if f.is_bank_open():
        return
    f.move_click(944, 505)
    pin = ['7', '3', '5', '7']
    time.sleep(f.r(1, 1.5))
    if f.is_bank_open():
        return None
    for n in pin:
        pag.press(n)
        time.sleep(f.r(1, 1.5))
    f.wait_until(f.is_bank_open)


def navigate_to_tab():
    f.move_click(640, 103)
    pag.moveTo(600 + f.p(5), 208 + f.p(5), f.r(0, 0.5))
    for i in range(10):
        pag.scroll(100)
        time.sleep(0.015)
    pag.click()


def set_deposit(option):
    if option == 'all':
        f.move_click(833, 825, 'fast')  # deposit all
    if option == 'one':
        f.move_click(680, 821, 'fast')  # withdraw one
    if option == 'five':
        f.move_click(719, 821, 'fast')  # withdraw one
    if option == 'ten':
        f.move_click(753, 821, 'fast')  # withdraw one
    if option == 'x':
        f.move_click(792, 821, 'fast')  # withdraw one


def gear_up():
    navigate_to_tab()
    f.move_click(1002, 821, 'fast')  # deposit items
    f.move_click(1040, 821, 'fast')  # deposit gear
    set_deposit('one')
    items = [(838, 143), (883, 143), (696, 137), (696, 210), (696, 252), (696, 285),
             (646, 178), (647, 212)]
    for i in items:
        f.move_click(*i, 'fast')
    pag.press('esc')
    time.sleep(f.r())
    inv = list(f.create_inv_grid().values())
    for xy in range(2, 8):  # equip slots 2-7
        f.move_click(*inv[xy], 'fast')
    open_bank()
    navigate_to_tab()
    set_deposit('all')
    f.move_click(933, 145, 'fast')
    f.move_click(983, 145, 'fast')
    pag.press('esc')
    f.wait_until(lambda: not(f.is_bank_open()))


def grab_fertilizers():
    open_bank()
    navigate_to_tab()
    set_deposit('all')
    inv = f.create_inv()
    f.move_click(*inv['Slot 4'], 'fast')
    set_deposit('x')
    f.move_click(935, 178, 'fast')
    f.move_click(834, 178, 'fast')
    f.move_click(888, 179, 'fast')
    pag.press('esc')
    f.wait_until(lambda: not(f.is_bank_open()))


def prep_soil(patch='1', right=False):
    global character_position
    if character_position == 'bank':
        bank_to_patch(patch)
    character_position = patch
    items = f.create_inv(28)
    inv = list(items.values())[16:28]
    slot = int(patch) - 1

    if patch in ['7', '8', '9', '10', '11', '12']:
        right = True
    xy = (976, 533) if right else (911, 533)

    f.move_click(*xy, speed='fast', wait_duration=f.r(3, 4))  # dig
    f.move_click(*inv[slot], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.5))
    f.move_click(*xy, wait_duration=f.r(4, 5))  # fertilize
    f.move_click(*items['Slot 3'], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.5))  # select seed
    f.move_click(*xy, wait_duration=f.r(4, 5))  # plant seed

    next_patch = int(character_position) + 1
    patch_to_patch(str(next_patch))


def patch_to_patch(to='2'):
    global character_position
    move_key = {'1 to 2': (946, 597),  '2 to 3': (946, 597),   '3 to 4': (946, 698),  '4 to 5': (946, 597),
                '5 to 6': (946, 597),  '6 to 7': 'special',    '7 to 8': (943, 477),  '8 to 9': (946, 477),
                '9 to 10': (946, 401), '10 to 11': (946, 477), '11 to 12': (946, 477)}

    key = f'{character_position} to {to}'
    if key == '6 to 7':
        return_to_bank()
        bank_to_patch(to)
    elif key == '12 to 13':
        return_to_bank(deposit=True)
    else:
        f.move_click(*move_key[key], wait_duration=f.r(3, 4))
        character_position = to


def wait_to_stop(area=(1683, 746, 168, 252), delay=3, tolerance=0):
    while True:
        img1 = f.take_screenshot(area)
        time.sleep(delay)
        img2 = f.take_screenshot(area)
        difference = cv.absdiff(img1, img2)
        if not(np.any(difference > tolerance)):
            break


# first tuple is xy to return to bank and second tuple is to go to tile
bank_guide = {'red': [(944, 291),  (944, 866)],
              '1':   [(944, 400),  (944, 665)],
              '2':   [(944, 353),  (944, 737)],
              '3':   [(944, 312),  (944, 818)],
              '4':   [(944, 219),  (944, 665)],  # from here down, must go to red tile first to go to tile
              '5':   [(944, 184),  (944, 737)],
              '6':   [(944, 153),  (944, 818)],
              '7':   [(1013, 155), (825, 819)],
              '8':   [(1014, 184), (825, 737)],
              '9':   [(1018, 216), (825, 663)],
              '10':  [(1025, 309), (829, 819)],
              '11':  [(1028, 351), (834, 737)],
              '12':  [(1032, 397), (838, 663)]}
                     # RETURN       GO TO TILE


def bank_to_patch(pos):
    global character_position
    global bank_guide

    special = ['4', '5', '6', '7',  '8', '9']
    if pos in special:
        f.move_click(*bank_guide['red'][1])
        f.wait_until(lambda: f.on_tile('red'))
    f.move_click(*bank_guide[pos][1], wait_duration=f.r(4, 5))
    character_position = pos


def return_to_bank(deposit=False):
    global bank_guide
    global character_position
    f.move_click(*bank_guide[character_position][0])
    f.wait_until(f.is_bank_open)
    time.sleep(f.r(0.25, 0.5))
    character_position = 'bank'
    if deposit:
        inv = f.create_inv(28)
        set_deposit('all')
        f.move_click(*inv['Slot 5'], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.5))
        f.move_click(*inv['Slot 6'], wait_duration=f.r(1, 1.5), move_duration=f.r(0.1, 0.2))
    pag.press('esc')
    time.sleep(f.r())


def collect_grapes(patch='1', right=False):
    global character_position
    if patch in ['7', '8', '9', '10', '11', '12']:
        right = True
    if character_position == 'bank':
        bank_to_patch(patch)
    status = check_grapes(right)
    xy = (976, 533) if right else (911, 533)
    # print(xy)
    while True:
        if status == 'check':
            f.move_click(*xy, speed='fast', wait_duration=f.r(3, 4))  # check health
            status = 'ready'

        while status == 'ready':
            f.move_click(*xy, speed='fast', wait_duration=f.r(3, 4))  # collect
            wait_to_stop()
            if f.full_inventory():
                return_to_bank(True)
                bank_to_patch(patch)
            status = check_grapes(right)

        if status == 'clear':
            f.move_click(*xy, wait_duration=f.r(6, 7))  # clear
            status = 'removed'

        if status == 'removed':
            if f.full_inventory():
                return_to_bank(True)
                character_position = 'bank'
            else:
                next_patch = int(character_position) + 1
                patch_to_patch(str(next_patch))
            return

        status = check_grapes(right)


def check_grapes(right=False):
    templates = {'check_health.png': 'check',
                 'pick.png':         'ready',
                 'clear.png':        'clear',
                 'dig.png':          'removed'}

    cords = (976, 533) if right else (911, 533)

    # right click once
    f.move_right_click(*cords)

    # screenshot once
    search_window = (100, 25, 200, 75)
    x = max(cords[0] - search_window[0], 0)
    y = max(cords[1] - search_window[1], 0)

    haystack = f.take_screenshot((x, y, search_window[2], search_window[3]))

    for image, status in templates.items():
        if f.option_in_screenshot(haystack, image):
            print(status)
            pag.move(f.p(-50, 50), f.p(-75, -50), f.r(0.1, 0.2))
            return status  # or return message if you prefer
    print('No matches')
    return None


def farm_run():
    enter_game()
    set_up()
    open_bank()
    gear_up()
    spots = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    for s in spots:
        collect_grapes(s)
    grab_fertilizers()
    for s in spots:
        prep_soil(s)


def main():
    for n in range(8):
        farm_run()
        time.sleep(f.r(3500, 3700))


main()
