import functions as f
import pyautogui as pag


def process_14_14(items):
    bank = (952, 382)
    item1 = (648, 646)
    item2 = (695, 648)

    loops = round(items / 14)

    for n in range(loops):
        f.move_click(*item1, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
        f.move_click(*item2, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
        pag.press('esc')
        f.wait_until(lambda: not(f.is_bank_open()))
        inv = f.create_inv(28)
        f.move_click(*inv['Slot 14'], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.5))
        f.move_click(*inv['Slot 15'], wait_duration=f.r(1, 1.5), move_duration=f.r(0.1, 0.2))
        pag.press('space')
        f.wait_until(lambda: f.slot_empty(28))
        f.move_click(*bank, wait_duration=f.r(1, 1.5))
        f.wait_until(f.is_bank_open)
        f.move_click(1004, 825, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.2, 0.35))


process_14_14(2300)
