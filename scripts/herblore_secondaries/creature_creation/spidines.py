import time
import functions as f
import pyautogui as pag


def set_up():
    f.shift_camera_direction('north')
    pag.moveTo(1140 + f.p(0, 100), 500 + f.p(0, 100), f.r(0, 1))
    pag.scroll(-10000)
    pag.press('f2')


def teleport_tower_of_life(n):
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))

    if n == 1:
        ring = f.find_option('ring_config.png', xy=(965, 895), search_window=(200, 100, 400, 400))
        f.move_click(*ring, wait_duration=f.r(4, 5))
        pag.typewrite('djp', interval=0.1)
        f.move_click(1718, 802, wait_duration=f.r(0.5, 1))
        f.move_click(805, 562, wait_duration=f.r(7, 8))
    else:
        f.move_click(965, 895, wait_duration=f.r(10, 12))
    f.move_click(624, 662, wait_duration=f.r(3, 4))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(945, 566, wait_duration=f.r(5, 6))
    f.move_click(945, 962, wait_duration=f.r(3, 4))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(911, 574, wait_duration=f.r(3, 4))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(1107, 911, wait_duration=f.r(3, 4))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(1012, 630, wait_duration=f.r(3, 4))
    f.wait_until(lambda: f.on_tile('red'))


def find_spidine():
    start_time = time.time()
    directions = {'right': (976, 532), 'down': (944, 564), 'up': (945, 505)}
    while time.time() - start_time < 60:
        for side, xy in directions.items():
            if f.find_option('attack_spidine.png', xy=xy):
                pag.move(f.p(-50, 50), f.p(-105, -75), f.r(0.1, 0.2))
                return side
            else:
                pag.move(f.p(-50, 50), f.p(-105, -75), f.r(0.1, 0.2))


def loot_spidine(side):
    directions = {'right': (976, 532), 'down': (944, 564), 'up': (945, 505)}
    direction_back = {'right': (914, 532), 'down': (944, 505), 'up': (945, 565)}

    xy = directions[side]
    f.move_click(*xy, wait_duration=f.r(4, 8))
    start_time = time.time()
    while time.time() - start_time < 60:
        dead = f.find_option('take_eggs.png', xy=xy, search_window=(150, 50, 300, 400))
        if dead:
            f.move_click(*dead, wait_duration=f.r(2, 3), speed='fast')
            f.move_click(*direction_back[side], wait_duration=f.r(1.5, 2.5))
            break
        else:
            pag.move(f.p(-50, 50), f.p(-105, -75), f.r(0.1, 0.2))


def kill_spidine():
    # activate altar
    f.move_click(907, 560, wait_duration=f.r(7, 8))
    side = find_spidine()
    loot_spidine(side)


def deposit_eggs():
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 2'], wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('purple'))
    f.move_click(1127, 736, wait_duration=f.r(1, 2))
    f.wait_until(f.is_bank_open)
    f.set_deposit('all')
    f.move_click(*inv['Slot 3'])


def grab_items(n):
    eggs = (744, 611)
    sardines = (646,  681)
    if n == 1:
        f.set_deposit('custom', x='13')
    else:
        f.set_deposit('x')
    f.move_click(*eggs, speed='fast')
    f.move_click(*sardines, speed='fast')
    pag.press('esc')
    f.wait_until(lambda: not (f.is_bank_open()))


for loop in range(1, 100):
    grab_items(loop)
    teleport_tower_of_life(loop)
    for n in range(1, 14):
        kill_spidine()
    deposit_eggs()
