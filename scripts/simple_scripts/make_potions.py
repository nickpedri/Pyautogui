import functions as f
import pyautogui as pag
import time


bank = (950, 511)


def make_compost_potion(items):
    loops = round(items / 27)
    harralander_unf_pot = (984, 540)
    for n in range(1, loops + 1):
        f.move_click(*harralander_unf_pot, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
        pag.press('esc')
        time.sleep(f.r(0.2, 0.3))
        inv = f.create_inv(28)
        f.move_click(*inv['Slot 1'], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.5))
        f.move_click(*inv['Slot 2'], wait_duration=f.r(1, 1.5), move_duration=f.r(0.1, 0.2))
        pag.press('space')
        time.sleep(f.r(32, 33))
        f.move_click(*bank, wait_duration=f.r(1, 1.5))
        f.move_click(*inv['Slot 2'], wait_duration=f.r(1, 1.5), move_duration=f.r(0.1, 0.2))


make_compost_potion(915)
