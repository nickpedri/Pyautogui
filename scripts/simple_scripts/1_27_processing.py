import functions as f
import pyautogui as pag
import time


inv = f.create_inv_grid()
bank = (951, 377)


def process(items):
    loops = round(items / 27)
    item = (790, 680)
    for n in range(1, loops + 1):
        f.move_click(*item, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
        pag.press('esc')
        time.sleep(f.r(0.2, 0.3))
        f.move_click(*inv['Slot 1'], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.5))
        f.move_click(*inv['Slot 2'], wait_duration=f.r(1, 1.5), move_duration=f.r(0.1, 0.2))
        pag.press('space')
        time.sleep(f.r(32, 33))
        f.move_click(*bank, wait_duration=f.r(1, 1.5))
        f.move_click(*inv['Slot 2'], wait_duration=f.r(1, 1.5), move_duration=f.r(0.1, 0.2))


process(4250)