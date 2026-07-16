import datetime
import functions as f
import pyautogui as pag
import time
import farm_functions as ff


berry_ready = {'ardy': True, 'cg': True, 'etceteria': True, 'fg': True, 'rimmington': True}


def reset_status():
    global berry_ready
    berry_ready = {'ardy': True, 'cg': True, 'etceteria': True, 'fg': True, 'rimmington': True}


## TELEPORT FUNCTIONS ##--##--##--##--##--##--##--##--##--##--##--##--##--##--
def tp_ardy():
    inv = list(f.create_inv().values())
    # print(inv)
    xy = f.find_option('pngs/monastery.png', xy=(1745, 765))
    f.move_click(*xy, wait_duration=f.r(6, 8))


def champ_guild_tp():
    f.move_click(1800, 721)
    f.shift_click(1822, 840, wait=f.r(5, 6))
    pag.press('f2')


def tp_etceteria():
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 1'], wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.shift_click(964, 901, wait=f.r(4, 5))
    pag.press('8')
    time.sleep(f.r(3, 4))


def tp_fg():
    f.move_click(1800, 721)
    f.shift_click(1726, 802, wait=f.r(5, 6))
    pag.press('f2')


def tp_rimmington():
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 1'], wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(961, 567, wait_duration=f.r(4, 5))


##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--
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


##--##--##--##--##--##--##--##-- RUN FUNCTIONS ##--##--##--##--##--##--##--##--
def ardy_run():
    global berry_ready
    while berry_ready['ardy']:
        tp_ardy()
        reposition_to_MMM()
        pick_berry('ardy')
        # print(berry_ready)
        bank_berries()


def cg_run():
    global berry_ready
    while berry_ready['cg']:
        champ_guild_tp()
        reposition_to_MMM()
        pick_berry('cg')
        # print(berry_ready)
        bank_berries()


def etc_run():
    global berry_ready
    while berry_ready['etceteria']:
        tp_etceteria()
        pick_berry('etceteria')
        # print(berry_ready)
        bank_berries()


def fg_run():
    global berry_ready
    while berry_ready['fg']:
        tp_fg()
        reposition_to_MMM()
        pick_berry('fg')
        # print(berry_ready)
        bank_berries()


def rimmington_run():
    global berry_ready
    while berry_ready['rimmington']:
        tp_rimmington()
        pick_berry('rimmington')
        # print(berry_ready)
        bank_berries()


##--##--##--##--##--##--##--##--##--##--##--##--##--##--
def berry_run(current_items):
    ff.open_bank()
    ff.item_up(current_items=current_items, items_to_equip='basic')
    ardy_run()
    cg_run()
    etc_run()
    fg_run()
    rimmington_run()
    reset_status()
