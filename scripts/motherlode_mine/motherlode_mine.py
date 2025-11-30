import pyautogui as pag
import functions as f
import time
import os
import datetime


project_dir = os.path.dirname(__file__)


def set_up():
    f.shift_camera_direction('north')
    pag.moveTo(1040 + f.p(0, 100), 500 + f.p(0, 100), f.r(0, 1))
    pag.scroll(-10000)


def check_if_mining(t=5):
    elapsed_time = 0
    start_time = time.time()
    print('Mining ...', end='')
    while elapsed_time < 120:
        if pag.pixelMatchesColor(40, 121, (255, 0, 0), tolerance=t):
            print('Not mining!')
            break
        elif pag.pixelMatchesColor(52, 120, (0, 255, 0), tolerance=t):
            print('.', end='')
            elapsed_time = time.time() - start_time
            time.sleep(4 + f.r(1, 2))
        else:
            print('No overlay found!')
            time.sleep(10)
            break


def identify_position(t=10):
    if f.check_pixel_color_in_area(search_region=(990, 547, 6, 6), target_color=(0, 255, 0), tolerance=5):
        print('On blue tile.')
        return 'blue'
    else:
        print('On green tile.')
        return 'green'


def swap_position(current_tile=None):
    if current_tile is None:
        current_tile = identify_position()
    if current_tile == 'blue':
        f.move_click(977, 532)
        time.sleep(f.r(2, 3))
    else:
        f.move_click(911, 534)
        time.sleep(f.r(2, 3))


def mine():
    pag.moveTo(100 + f.p(), 100 + f.p())
    ore_available = f.check_pixel_color_in_area(search_region=(940, 474, 6, 6), target_color=(255, 255, 0), tolerance=5)
    if not ore_available:
        f.move_click(945, 485)
        pag.move(f.r(-100, 100), -f.r(30, 100), f.r())
        time.sleep(f.r(2, 4))
    else:
        swap_position()
        f.move_click(945, 483)
        pag.move(f.r(-100, 100), -f.r(30, 100), f.r())
        time.sleep(f.r(2, 4))


def check_inv():
    full = f.find_spots('inv_full_slot.png', threshold=0.95, area=(1800, 960, 70, 60))
    if full:
        full = False
        print('Inventory not full!')
    else:
        full = True
        print('Inventory full!')
    return full


def deposit_in_hopper():
    position = identify_position()
    if position == 'green':
        swap_position('green')

    f.move_click(1051, 740)
    time.sleep(f.r(6, 7))


def main(setup=True):
    start_time = time.time()  # Start timer for script
    f.countdown(2)
    f.initialize_pag()
    if setup:
        set_up()

    for n in range(1, 90):  # Number of inventories to do
        full = check_inv()
        while full is False:
            mine()
            check_if_mining()
            full = check_inv()
        deposit_in_hopper()
        if n % 4 == 0:
            f.play_actions('collect_ores.json', project_dir)
            time.sleep(f.r(7, 8))
        else:
            f.move_click(887, 366)
            time.sleep(f.r(5, 6))
        print(f'Inventory {n} done at {datetime.datetime.now()}')

    print(f'Script duration: {str(datetime.timedelta(seconds=time.time() - start_time))}')


main()
