import functions as f
import pyautogui as pag

bank = (944, 218)
item1 = (840, 468)
spell = (1750, 787)


def humidify():
    inv = f.create_inv(28)
    f.move_click(*item1, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
    pag.press('esc')
    f.wait_until(lambda: not(f.is_bank_open()))
    f.move_click(*spell, wait_duration=f.r(4, 5), move_duration=f.r(0.3, 0.5))
    f.move_click(*bank)
    f.wait_until(f.is_bank_open)
    f.move_click(*inv['Slot 1'], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.5))


items = 559
loops = round(items / 27)
for n in range(loops+1):
    humidify()
