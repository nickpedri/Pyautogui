import functions as f
import pyautogui as pag
import time


bank = (950, 511)
amulet_of_chem = (742, 141)


def interface_open():
    area = (80, 894, 30, 5)
    color = (64, 48, 32)
    if f.check_pixel_color_in_area(area, color, tolerance=1):
        return True
    else:
        return False


def make_compost_potion(items):
    loops = round(items / 27)
    harralander_unf_pot = (984, 540)
    inv = f.create_inv(28)
    for n in range(1, loops + 1):
        f.move_click(*harralander_unf_pot, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
        pag.press('esc')
        time.sleep(f.r(0.2, 0.3))
        f.move_click(*inv['Slot 1'], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.5))
        f.move_click(*inv['Slot 2'], wait_duration=f.r(1, 1.5), move_duration=f.r(0.1, 0.2))
        pag.press('space')
        time.sleep(f.r(32, 33))
        f.move_click(*bank, wait_duration=f.r(1, 1.5))
        f.move_click(*inv['Slot 2'], wait_duration=f.r(1, 1.5), move_duration=f.r(0.1, 0.2))


def make_stamina_potion(items):
    loops = round(items / 27)
    super_energy = (791, 652)
    amylase_crystal = (747, 646)
    inv = f.create_inv(28)
    for n in range(1, loops + 1):
        f.move_click(*amulet_of_chem, speed='fast')
        pag.keyDown('shift')
        f.move_click(*inv['Slot 1'])
        pag.keyUp('shift')
        f.move_click(1002, 824, 'fast')  # deposit all
        f.move_click(*amylase_crystal, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
        f.move_click(*super_energy, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
        pag.press('esc')
        time.sleep(f.r(0.2, 0.3))
        f.move_click(*inv['Slot 1'], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.5))
        f.move_click(*inv['Slot 2'], wait_duration=f.r(1, 1.5), move_duration=f.r(0.1, 0.2))
        pag.press('space')
        time.sleep(f.r(32, 33))
        f.move_click(*bank, wait_duration=f.r(1, 1.5))
        f.move_click(1002, 824, 'fast')


def make_14_potion(unf_pot, secondary, items, amulet=False):
    loops = round(items / 14)
    inv = f.create_inv(28)
    f.set_deposit('custom', '14')
    for n in range(loops):
        if amulet:
            f.move_click(*amulet_of_chem, speed='fast')
            pag.keyDown('shift')
            f.move_click(*inv['Slot 1'])
            pag.keyUp('shift')
            f.move_click(1002, 824, 'fast')
        f.move_click(*unf_pot, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
        f.move_click(*secondary, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
        pag.press('esc')
        f.wait_until(lambda: not (f.is_bank_open()))
        time.sleep(f.r(0.25, 0.5))
        f.move_click(*inv['Slot 14'], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.5))
        f.move_click(*inv['Slot 15'], wait_duration=f.r(1, 1.5), move_duration=f.r(0.1, 0.2))
        f.wait_until(interface_open)
        pag.press('space')
        f.wait_until(lambda: f.slot_empty(28))
        f.move_click(*bank, wait_duration=f.r(1, 1.5))
        f.wait_until(f.is_bank_open)
        f.move_click(1004, 825, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.2, 0.35))


# make_stamina_potion(2000)

make_14_potion((887, 576), (837, 573), 1300, False)
