import functions as f
import pyautogui as pag

# pestle and mortar withdrawn to 28th slot
inv = f.create_inv_grid()
bank = (951, 377)
scales = (937, 280)


for n in range(1, round(800/27)+1):
    f.move_click(*scales)
    pag.press('esc')
    pag.moveTo(f.p(1750, 1850), f.p(950, 1000), f.r())
    for s in range(28):
        f.move_click(*inv['Slot 27'], move_duration=f.r(0.03, 0.08), wait_duration=f.r(0.01, 0.05))
        f.move_click(*inv['Slot 28'], move_duration=f.r(0.03, 0.08), wait_duration=f.r(0.01, 0.05))
    f.move_click(*bank)
    f.move_click(*inv['Slot 1'])
