import functions as f
import pyautogui as pag
import time


def mine_rock(rock='1'):
    if rock == '1':
        f.move_click(974, 532)
        pag.move(f.p(-50, 50), f.p(-75, -50), f.r(0.1, 0.2))


def rock_depleted(rock='1'):
    if rock == '1':
        depleted = f.check_pixel_color_in_area(search_region=(970, 524, 10, 10), target_color=(255, 255, 0))
        # print(depleted)
        return depleted


def not_mining():
    stopped = f.check_pixel_color_in_area(search_region=(42, 50, 10, 10), target_color=(255, 0, 0))
    return stopped


def note_basalt():
    f.move_click(567, 985, wait_duration=f.r(3, 4))
    f.wait_until(lambda: f.on_tile('yellow'), timeout=300)
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 2'], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.5, 0.7))
    f.move_click(859, 347, wait_duration=f.r(4, 5))
    f.move_click(1100, 700, wait_duration=3)
    f.wait_until(lambda: f.on_tile('blue'), timeout=300)
    f.move_click(1206, 288)
    f.wait_until(lambda: f.on_tile('green'), timeout=300)


def mine_basalt():
    while True:
        mine_rock()
        f.wait_until(not_mining, timeout=300)
        if f.full_inventory():
            note_basalt()
        f.wait_until(lambda: not(rock_depleted()), timeout=300)


##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--

def mine_salt(rock='1'):
    if rock == '1':
        f.move_click(707, 617, wait_duration=f.r(2, 3))
    if rock == '2':
        f.move_click(960, 360, wait_duration=f.r(2, 3))
    if rock == '3':
        f.move_click(1177, 626, wait_duration=f.r(2, 3))


def mine_red_or_blue_salt(hours_to_run=2):
    start = time.time()
    while time.time() - start < (hours_to_run * 3600):
        mine_salt('1')
        f.wait_until(not_mining, timeout=300)
        mine_salt('2')
        f.wait_until(not_mining, timeout=300)
        mine_salt('3')
        f.wait_until(not_mining, timeout=300)


def mine_green_salt(hours_to_run=2):
    start = time.time()
    while time.time() - start < (hours_to_run * 3600):
        mine_salt('1')
        f.wait_until(not_mining, timeout=300)
        mine_salt('3')
        f.wait_until(not_mining, timeout=300)


mine_green_salt(2)