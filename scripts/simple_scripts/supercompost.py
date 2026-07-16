import functions as f
import pyautogui as pag


inv = f.create_inv_grid()
bank = (951, 377)
compost = (791, 689)
potion = (791, 505)

for n in range(1, round(3779/22)+1):
    f.set_deposit('x') # x has to be 6
    f.move_click(*potion, speed='fast')
    f.set_deposit('all')
    f.move_click(*compost, speed='fast')
    pag.press('esc')
    f.wait_until(lambda: not(f.is_bank_open()))
    pag.moveTo(f.p(1750, 1850), f.p(950, 1000), f.r(0.05, 0.12))
    for s in range(25):
        f.move_click(*inv['Slot 6'], move_duration=f.r(0.03, 0.10), wait_duration=f.r(0.01, 0.02))
        f.move_click(*inv['Slot 28'], move_duration=f.r(0.03, 0.11), wait_duration=f.r(0.01, 0.02))
    f.move_click(*bank)
    f.move_click(1001, 823)
