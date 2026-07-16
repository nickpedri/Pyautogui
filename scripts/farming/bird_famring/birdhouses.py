import farm_functions as ff
import functions as f
import pyautogui as pag
import time


def navigate_to_tab():
    f.move_click(640, 103)
    pag.moveTo(600 + f.p(5), 285 + f.p(5), f.r(0, 0.5))
    for i in range(10):
        pag.scroll(100)
        time.sleep(0.015)
    pag.click()


def item_up(current_items=None):
    if current_items != 'birdhouse':
        pass
    navigate_to_tab()
    f.move_click(1002, 821, 'fast')  # deposit items

    f.set_deposit('one')
    items = [(838, 143), (887, 143), (936, 146), (982, 143),
             (838, 177), (887, 177), (936, 177), (982, 177)]
    for i in items:
        f.move_click(*i, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.1, 0.15))
    f.set_deposit('all')
    f.move_click(838, 214)
    pag.press('esc')
    f.wait_until(lambda: not (f.is_bank_open()))


def tp_fossil_island():
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(1026, 258, wait_duration=f.r(7, 8))
    ff.reposition_to_MMM()


def craft_birdhouse(n):
    x = 5 if n > 1 else 10

    f.click_slot(n+4)
    f.click_slot(x)
    time.sleep(3)


def build_and_seed(x, y):
    f.move_click(x, y, wait_duration=f.r(2, 3))
    f.click_slot(9)
    f.move_click(x, y, wait_duration=f.r(2, 3))


def birdhouse_1_2():
    # Tp to area 1
    f.move_click(930, 256, wait_duration=f.r(6, 8))
    pag.press('2')
    time.sleep(f.r(5, 6))

    # Move to birdhouse 1
    f.move_click(1051, 623, wait_duration=f.r(6, 8))
    craft_birdhouse(1)
    build_and_seed(975, 535)

    # Move to birdhouse 2
    f.move_click(1125, 346, wait_duration=f.r(6, 8))
    craft_birdhouse(2)
    build_and_seed(944, 507)

    # Tp to area 2
    f.move_click(615, 645, wait_duration=f.r(6, 8))
    pag.press('4')
    time.sleep(f.r(5, 6))


def birdhouse_3_4():
    # Move to birdhouse 3
    f.move_click(971, 234, wait_duration=f.r(6, 8))
    craft_birdhouse(3)
    build_and_seed(943, 506)

    # Run to birdhouse 4
    f.move_click(1025, 955, wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(1104, 950, wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(813, 1015, wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(1030, 1016, wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(901, 1015, wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('yellow'))

    # Birdhouse 4
    f.move_click(860, 825, wait_duration=f.r(6, 8))
    craft_birdhouse(4)
    build_and_seed(912, 534)

    # Bank
    ff.bank_items()


def bird_run(current_items):
    ff.open_bank()
    item_up(current_items=current_items)
    tp_fossil_island()
    birdhouse_1_2()
    birdhouse_3_4()
