import pyautogui as pag
import functions as f
import time
import os
import datetime


project_dir = os.path.dirname(__file__)


def set_up():
    f.shift_camera_direction('east')
    pag.moveTo(1040 + f.p(0, 100), 500 + f.p(0, 100), f.r(0, 1))
    pag.scroll(-10000)


def main(setup=True):

    # Initialize script --------------
    print(f'Script started at {datetime.datetime.now()}')
    f.initialize_pag()
    start_time = time.time()  # Start timer for script
    if setup:
        set_up()

    # Main loop --------------
    for n in range(1, 2):
        print(f'Inventory {n} done at {datetime.datetime.now()}')
        print()

    # End time --------------
    print(f'Script duration: {str(datetime.timedelta(seconds=time.time() - start_time))}')


main()