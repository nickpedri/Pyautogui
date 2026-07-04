import functions as f
import pyautogui as pag
import time


bank = (950, 511)
herb = (937, 395)
first_slot = (1705, 767)


inv = f.create_inv_grid()


def clean_herbs():
    pag.moveTo(1705 + f.p(20), 767 + f.p(20), f.r(0.25, 0.5))
    for xy in inv.values():
        f.move_click(*xy, move_duration=f.r(0.05, 0.10), r1=f.p(7), r2=f.p(7), wait_duration=f.r(0.05, 0.10))


for n in range(1, 500):
    f.move_click(*herb)
    pag.press('esc')
    clean_herbs()
    # f.move_click(*first_slot)
    # time.sleep(f.r(33, 35))
    f.move_click(*bank, wait_duration=f.r(1, 1.5))
    f.move_click(*first_slot)

