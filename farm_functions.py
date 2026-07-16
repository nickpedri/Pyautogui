import datetime
import functions as f
import pyautogui as pag
import time


def set_up():
    f.shift_camera_direction('north')
    pag.moveTo(1140 + f.p(0, 100), 500 + f.p(0, 100), f.r(0, 1))
    pag.scroll(-10000)
    pag.press('f2')


def open_bank(bank=None):
    if bank is None:
        bank = (944, 561)
    if f.is_bank_open():
        return
    f.move_click(*bank)
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
    pag.moveTo(600 + f.p(5), 247 + f.p(5), f.r(0, 0.5))
    for i in range(10):
        pag.scroll(100)
        time.sleep(0.015)
    pag.click()


def gear_up(gear=True):
    navigate_to_tab()
    f.move_click(1002, 821, 'fast')  # deposit items
    f.move_click(1040, 821, 'fast')  # deposit gear

    f.set_deposit('one')
    armor = [(696, 210), (696, 252), (696, 285), (646, 178), (647, 212), (743, 211), (743, 283), (696, 137)]
    for g in armor:
        f.move_click(*g, wait_duration=f.r(0.01, 0.02), move_duration=f.r(0.025, 0.15))
    pag.press('esc')
    time.sleep(f.r())
    inv = list(f.create_inv_grid().values())
    for xy in range(0, 8):  # equip slots 2-7
        f.move_click(*inv[xy], wait_duration=f.r(0.025, 0.075), move_duration=f.r(0.025, 0.15))
    open_bank()


def item_up(items_to_equip='basic', current_items='advanced'):
    if current_items != items_to_equip:
        swap_items = True
    else:
        swap_items = False

    if swap_items:
        navigate_to_tab()
        f.move_click(1002, 821, 'fast')  # deposit items

        f.set_deposit('one')
        if items_to_equip == 'basic':
            items = [(838, 143), (887, 143), (936, 146)]
            for i in items:
                f.move_click(*i, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.1, 0.15))

        elif items_to_equip == 'advanced':
            items = [(838, 143), (887, 143), (936, 146), (982, 143), (838, 177), (887, 177), (936, 177), (982, 177)]
            for i in items:
                f.move_click(*i, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.1, 0.15))
            f.set_deposit('all')
            f.move_click(838, 212, 'fast')
            f.move_click(887, 212, 'fast')

    pag.press('esc')
    f.wait_until(lambda: not (f.is_bank_open()))


def reposition_to_MMM():
    start = time.time()
    timeout = 300
    directions = ['north', 'east', 'south', 'west']
    index = 1
    camera_moved = False
    while time.time() - start < timeout:
        xy = f.find('pngs/MMM_tile.png', area=(800, 300, 500, 500))
        if xy:
            f.move_click(*xy, wait_duration=f.r(3, 4))
            f.wait_until(lambda: f.on_tile('yellow'))
            break
        camera_moved = True
        f.shift_camera_direction(directions[index])
        index += 1
        if index == 4:
            index = 0
        time.sleep(5)
        if time.time() - start > timeout:
            raise TimeoutError('Could not reposition!')
    if camera_moved:
        set_up()


def bank_items():
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 3'], wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('purple'))
    f.move_click(1127, 736, wait_duration=f.r(1, 2))
    f.wait_until(f.is_bank_open)
    f.set_deposit('all')
    f.move_click(*inv['Slot 6'], wait_duration=f.r(0.1, 0.2), speed='fast')
    f.move_click(*inv['Slot 11'], wait_duration=f.r(0.1, 0.2), speed='fast')
    pag.press('esc')
    time.sleep(f.r(1, 2))
