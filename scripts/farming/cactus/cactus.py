import functions as f
import pyautogui as pag
import time
import farm_functions as ff

cactus_ready = {'fg': True, 'al_kharid': True}


def reset_status():
    global cactus_ready
    cactus_ready = {'fg': True, 'al_kharid': True}


def tp_fg():
    f.move_click(1800, 721)
    f.shift_click(1726, 802, wait=f.r(5, 6))
    pag.press('f2')
    ff.reposition_to_MMM()


def tp_al_kharid():
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(1160, 660, wait_duration=f.r(4, 5))
    pag.press('r')
    time.sleep(3)
    f.move_click(1017, 680, wait_duration=f.r(8, 9))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(1323, 394, wait_duration=f.r(3, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(967, 225, wait_duration=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('red'))


def pick_cactus(location='fg'):
    guide = {'fg': [(1286, 127), (959, 477)], 'al_kharid': [(1064, 39), (960, 480)]}
    f.move_click(*guide[location][0], wait_duration=f.r(6, 8))
    f.wait_until(lambda: f.on_tile('blue'))
    f.wait_to_stop()
    cactus_status = f.find_option('pngs/pick.png', guide[location][1])
    if not cactus_status:
        cactus_ready[location] = False


def bank_spines():
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 3'], wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('purple'))
    f.move_click(1127, 736, wait_duration=f.r(1, 2))
    f.wait_until(f.is_bank_open)
    f.set_deposit('all')
    f.move_click(*inv['Slot 4'], wait_duration=f.r(2, 3))
    pag.press('esc')
    time.sleep(f.r(1, 2))


def fg_run():
    global cactus_ready
    while cactus_ready['fg']:
        tp_fg()
        pick_cactus('fg')
        # print(berry_ready)
        bank_spines()


def al_kharid_run():
    global cactus_ready
    while cactus_ready['al_kharid']:
        tp_al_kharid()
        pick_cactus('al_kharid')
        # print(berry_ready)
        bank_spines()


def cactus_run(current_items):
    ff.open_bank()
    ff.item_up(current_items=current_items, items_to_equip='basic')

    fg_run()
    al_kharid_run()

    reset_status()

