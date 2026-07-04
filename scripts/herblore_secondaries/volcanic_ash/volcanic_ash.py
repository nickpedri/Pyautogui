import functions as f
import pyautogui as pag
import time


def set_up():
    f.shift_camera_direction('north')
    pag.moveTo(1140 + f.p(0, 100), 500 + f.p(0, 100), f.r(0, 1))
    pag.scroll(-10000)
    pag.press('f2')


def ash_depleted(direction='left'):
    if direction == 'left':
        ash = f.check_pixel_color_in_area(search_region=(906, 527, 12, 12), target_color=(255, 255, 0))
        return ash
    if direction == 'down':
        ash = f.check_pixel_color_in_area(search_region=(933, 556, 12, 12), target_color=(255, 255, 0))
        return ash
    if direction == 'right':
        ash = f.check_pixel_color_in_area(search_region=(968, 526, 12, 12), target_color=(255, 255, 0))
        return ash


def mine_ash_1():
    f.move_click(909, 537)
    pag.move(f.p(-50, -50), f.p(-150, -75), f.r(.15, 0.35))
    f.wait_until(lambda: ash_depleted(), timeout=90)
    f.move_click(1187, 663, wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('blue'))
    # print('ore depleted')


def mine_ash_2():
    f.move_click(946, 563)
    pag.move(f.p(-50, -50), f.p(-150, -75), f.r(.15, 0.35))
    f.wait_until(lambda: ash_depleted('down'), timeout=90)
    f.move_click(1063, 453, wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('green'))
    # print('ore depleted')


def mine_ash_3():
    f.move_click(973, 532)
    pag.move(f.p(-50, -50), f.p(-150, -75), f.r(.15, 0.35))
    f.wait_until(lambda: ash_depleted('right'), timeout=90)
    f.move_click(1194, 700, wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('blue'))
    # print('ore depleted')


def mine_ash_4():
    f.move_click(943, 565)
    pag.move(f.p(-50, -50), f.p(-150, -75), f.r(.15, 0.35))
    f.wait_until(lambda: ash_depleted('down'), timeout=90)
    f.move_click(440, 380, wait_duration=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('green'))
    # print('ore depleted')


def mine_ash():
    mine_ash_1()
    mine_ash_2()
    mine_ash_3()
    mine_ash_4()


def empty_inv():
    inv = list(f.create_inv_grid().values())[8:]
    # print(inv)
    # print(len(inv))
    pag.keyDown('shift')
    for xy in inv:
        f.move_click(*xy, move_duration=f.r(0.05, 0.10), r1=f.p(4), r2=f.p(4), wait_duration=f.r(0.05, 0.10))
    pag.keyUp('shift')


def main():
    set_up()
    for n in range(300):
        mine_ash()
        if n % 20 == 0:
            empty_inv()


main()
