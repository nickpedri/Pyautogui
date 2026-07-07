import functions as f
import pyautogui as pag
import time
import numpy as np
import cv2 as cv

berry_ready = {'ardy': True, 'cg': True, 'etceteria': True, 'fg': True, 'rimmington': True}


def reset_status():
    global berry_ready
    berry_ready = {'ardy': True, 'cg': True, 'etceteria': True, 'fg': True, 'rimmington': True}


def set_up():
    f.shift_camera_direction('north')
    pag.moveTo(1140 + f.p(0, 100), 500 + f.p(0, 100), f.r(0, 1))
    pag.scroll(-10000)
    pag.press('f2')


def enter_game():
    f.move_click(945, 285, wait_duration=f.r(10, 12))
    f.move_click(950, 354, wait_duration=f.r(2, 3))


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


def gear_up():
    navigate_to_tab()
    f.move_click(1002, 821, 'fast')  # deposit items
    f.move_click(1040, 821, 'fast')  # deposit gear
    f.set_deposit('one')
    gear = [(696, 210), (696, 252), (696, 285), (646, 178), (647, 212), (743, 211), (743, 283), (696, 137)]
    items = [(838, 143), (887, 143), (936, 146)]
    for g in gear:
        f.move_click(*g, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.1, 0.15))
    pag.press('esc')
    time.sleep(f.r())
    inv = list(f.create_inv_grid().values())
    for xy in range(0, 8):  # equip slots 2-7
        f.move_click(*inv[xy], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.1, 0.15))
    open_bank()
    navigate_to_tab()
    for i in items:
        f.move_click(*i, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.1, 0.15))
    pag.press('esc')
    f.wait_until(lambda: not(f.is_bank_open()))


def tp_ardy():
    inv = list(f.create_inv().values())
    print(inv)
    xy = f.find_option('pngs/monastery.png', xy=(1745, 765))
    f.move_click(*xy, wait_duration=f.r(6, 8))


def reposition_to_MMM():
    xy = f.find('pngs/MMM_tile.png', area=(800, 400, 400, 400))
    f.move_click(*xy, wait_duration=f.r(3, 4))


def pick_berry(location='ardy'):
    guide = {'ardy': [(1230, 435), (990, 521)], 'cg': [(405, 435), (929, 491)], 'etceteria': [(377, 334), (898, 519)],
             'fg': [(1280, 381), (959, 485)], 'rimmington': [(496, 603), (893, 520)]}
    f.move_click(*guide[location][0], wait_duration=f.r(15, 20))
    f.wait_to_stop()
    berry_status = f.find_option('pngs/pick_from.png', guide[location][1])
    if not berry_status:
        berry_ready[location] = False


def bank_berries():
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 3'], wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('purple'))
    f.move_click(1127, 736, wait_duration=f.r(1, 2))
    f.wait_until(f.is_bank_open)
    f.set_deposit('all')
    f.move_click(*inv['Slot 4'], wait_duration=f.r(2, 3))
    pag.press('esc')
    time.sleep(f.r(1, 2))


def run_prep():
    open_bank()
    gear_up()


def ardy_run():
    global berry_ready
    while berry_ready['ardy']:
        tp_ardy()
        reposition_to_MMM()
        pick_berry('ardy')
        print(berry_ready)
        bank_berries()


def champ_guild_tp():
    f.move_click(1800, 721)
    f.shift_click(1822, 840, wait=f.r(5, 6))
    pag.press('f2')


def cg_run():
    global berry_ready
    while berry_ready['cg']:
        champ_guild_tp()
        reposition_to_MMM()
        pick_berry('cg')
        print(berry_ready)
        bank_berries()


def tp_etceteria():
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 1'], wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.shift_click(964, 901, wait=f.r(4, 5))
    pag.press('8')
    time.sleep(f.r(3, 4))


def etc_run():
    global berry_ready
    while berry_ready['etceteria']:
        tp_etceteria()
        pick_berry('etceteria')
        print(berry_ready)
        bank_berries()


def tp_fg():
    f.move_click(1800, 721)
    f.shift_click(1726, 802, wait=f.r(5, 6))
    pag.press('f2')


def fg_run():
    global berry_ready
    while berry_ready['fg']:
        tp_fg()
        reposition_to_MMM()
        pick_berry('fg')
        print(berry_ready)
        bank_berries()


def tp_rimmington():
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 1'], wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(961, 567, wait_duration=f.r(4, 5))


def rimmington_run():
    global berry_ready
    while berry_ready['rimmington']:
        tp_rimmington()
        pick_berry('rimmington')
        print(berry_ready)
        bank_berries()


def log_out():
    f.move_click(1770, 1021)
    f.move_click(1767, 969)


def berry_run():
    enter_game()
    set_up()
    run_prep()
    ardy_run()
    cg_run()
    etc_run()
    fg_run()
    rimmington_run()
    reset_status()
    log_out()


for n in range(8):
    berry_run()
    time.sleep(80*60)
    time.sleep(f.r(60, 300))
