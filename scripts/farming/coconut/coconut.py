import farm_functions as ff
import functions as f
import pyautogui as pag
import time


def item_up(current_items=None):
    ff.navigate_to_tab()
    if current_items != 'cocout':
        pass
    f.move_click(1002, 821, 'fast')  # deposit items

    f.set_deposit('one')
    items = [(838, 143), (935, 142), (934, 213)]
    for i in items:
        f.move_click(*i, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.1, 0.15))
    pag.press('esc')
    f.wait_until(lambda: not (f.is_bank_open()))


def brimhaven():
    # tp to brimhaven
    inv = f.create_inv(28)
    f.shift_click(*inv['Slot 1'], wait=(f.r(1, 2)))
    pag.press('8')
    time.sleep(f.r(4, 5))
    # run to tree and collect
    f.move_click(892, 170, wait_duration=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(1116, 174, wait_duration=f.r(7, 8))
    f.wait_to_stop()


def catherby():
    # tp to catherby
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(959, 356, wait_duration=f.r(4, 5))
    ff.reposition_to_MMM()

    # run to tree and collect
    f.move_click(1569, 600,  wait_duration=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(1590, 593,  wait_duration=f.r(7, 8))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.shift_camera_direction('east')
    f.move_click(1183, 169, wait_duration=f.r(10, 12))
    f.wait_to_stop()
    f.shift_camera_direction('north')


def farming_guild():
    # tp to farming guild
    f.move_click(1800, 721)
    f.shift_click(1726, 802, wait=f.r(5, 6))
    pag.press('f2')
    ff.reposition_to_MMM()

    # run to tree and collect
    f.move_click(944, 234,  wait_duration=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(800, 155, wait_duration=f.r(10, 12))
    f.wait_to_stop()

    # Bank items to the bank nearby
    f.move_click(1100, 470,  wait_duration=f.r(2, 3))
    f.wait_until(f.is_bank_open)
    f.set_deposit('all')
    f.click_slot(4)
    pag.press('esc')
    time.sleep(f.r(1, 2))


def gnome_stronghold():
    # tp to gnome stronghold
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 1'], wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.shift_click(964, 901, wait=f.r(4, 5))
    pag.press('2')
    time.sleep(f.r(3, 4))

    # run to tree and collect
    f.move_click(1400, 495, wait_duration=f.r(10, 12))
    f.wait_to_stop()


def kastori():
    # tp to civ
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.shift_click(959, 356, wait=f.r(5, 6))
    pag.press('6')
    time.sleep(3)
    ff.reposition_to_MMM()
    f.move_click(1300, 419,  wait_duration=f.r(5, 6))

    # fly quetzal
    f.move_click(738, 483,  wait_duration=f.r(5, 6))

    # run to tree and collect
    f.move_click(903, 51,  wait_duration=f.r(5, 6))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(1146, 267,  wait_duration=f.r(10, 12))
    f.wait_to_stop()


def lletya():
    # tp to lletya
    inv = f.create_inv(28)
    f.shift_click(*inv['Slot 3'], wait=(f.r(5, 6)))
    ff.reposition_to_MMM()

    # collect tree
    f.move_click(1396, 892,  wait_duration=f.r(7, 8))
    f.wait_to_stop()


def tree_gnome_village():
    # tp to tree gnome village fairy ring
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    ring = f.find_option('pngs/ring_config.png', xy=(965, 895), search_window=(200, 100, 400, 400))
    f.move_click(*ring, wait_duration=f.r(4, 5))
    pag.typewrite('ciq', interval=0.1)
    f.move_click(1718, 802, wait_duration=f.r(0.5, 1))
    f.move_click(805, 562, wait_duration=f.r(7, 8))

    # run to tree
    f.move_click(231, 445,  wait_duration=f.r(5, 6))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(760, 194,  wait_duration=f.r(5, 6))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(794, 115,  wait_duration=f.r(7, 8))
    f.wait_until(lambda: f.on_tile('yellow'))

    # collect tree
    f.move_click(1014, 256,  wait_duration=f.r(7, 8))
    f.wait_to_stop()


def bank_items():
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 2'], wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('purple'))
    f.move_click(1127, 736, wait_duration=f.r(1, 2))
    f.wait_until(f.is_bank_open)
    f.move_click(1002, 821, 'fast')  # deposit items
    pag.press('esc')
    f.wait_until(lambda: not (f.is_bank_open()))


def coconut_run(current_items):
    ff.open_bank()
    item_up(current_items=current_items)
    brimhaven()
    catherby()
    farming_guild()
    gnome_stronghold()
    kastori()
    lletya()
    tree_gnome_village()
    bank_items()