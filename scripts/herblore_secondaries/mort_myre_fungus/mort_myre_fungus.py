import time
import functions as f
import pyautogui as pag
import datetime


def set_up():
    f.shift_camera_direction('north')
    pag.moveTo(1140 + f.p(0, 100), 500 + f.p(0, 100), f.r(0, 1))
    pag.scroll(-10000)
    pag.press('f2')


def bloom():
    f.move_click(1826, 767)
    time.sleep(0.5 + f.r())


def check_shrooms():
    p1 = not(f.check_pixel_color_in_area(search_region=(891, 518, 30, 30), target_color=(255, 0, 0)))
    p2 = not(f.check_pixel_color_in_area(search_region=(934, 485, 30, 30), target_color=(255, 0, 0)))
    p3 = not(f.check_pixel_color_in_area(search_region=(966, 519, 30, 30), target_color=(255, 0, 0)))
    pag.moveTo(940 + f.p(100), 530 + f.p(100), f.r(0.3, 0.5))
    # print(p1, p2, p3)
    return p1, p2, p3


def collect_shrooms():
    bloom()
    p1, p2, p3 = check_shrooms()
    l1, l2, l3 = (912, 535), (945, 502), (977, 534)
    if p1:
        # xy = f.find_option('pick.png', l1, search_window=(75, 5, 150, 80), test=False, img_name='log.png')
        # if xy:
        f.move_click(*l1, move_duration=f.r(0.1, 0.2))
    if p2:
        # xy = f.find_option('pick.png', l1, search_window=(75, 5, 150, 80), test=False, img_name='log.png')
        # if xy:
        f.move_click(*l2, move_duration=f.r(0.1, 0.2))
    if p3:
        # xy = f.find_option('pick.png', l1, search_window=(75, 5, 150, 80), test=False, img_name='log.png')
        # if xy:
        f.move_click(*l3, move_duration=f.r(0.1, 0.2))


def shroom_it_up():
    start = time.time()
    print(f.full_inventory())
    while not(f.full_inventory()):
        collect_shrooms()
        if time.time() - start > 300:
            print(f'Script ended at {datetime.datetime.now()}!')
            raise TimeoutError("Condition was not met in time.")


def teleport(location):
    if location == 'Ver_Sinzhaza':
        f.move_click(1750, 766)
        f.wait_until(lambda: f.on_tile('yellow'))
        f.move_click(1154, 126, wait_duration=5)
        f.wait_until(lambda: f.on_tile('yellow'))
        f.move_click(1302, 565)
        f.wait_until(lambda: f.on_tile('blue'))

    if location == 'crafting_guild':
        f.move_click(1786, 767)
        time.sleep(3 + f.r())

    if location == 'house':
        f.move_click(1704, 769, wait_duration=f.r(3, 4))
        f.wait_until(lambda: f.on_tile('yellow'))
        f.move_click(850, 757)
        time.sleep(3 + f.r())


def bank():
    teleport('crafting_guild')
    f.move_click(1130, 737)
    time.sleep(4)
    f.move_click(1703, 802)
    time.sleep(f.r())
    pag.press('esc')
    time.sleep(f.r())


def main(setup=False):
    # ~95 s per loop. ~38 loops per hour
    f.countdown()
    f.initialize_pag()
    if setup:
        set_up()
    for n in range(1, 200):
        teleport('house')
        teleport('Ver_Sinzhaza')
        shroom_it_up()
        bank()
        print(f'Loop {n} done!')


main(True)
