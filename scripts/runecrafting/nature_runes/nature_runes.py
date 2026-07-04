import pyautogui as pag
import functions as f
import time
import os
import datetime


def set_up():
    f.shift_camera_direction('east')
    pag.moveTo(1140 + f.p(0, 100), 500 + f.p(0, 100), f.r(0, 1))
    pag.scroll(-10000)
    pag.press('f2')


def fill_inv():
    f.move_click(744, 283)  # withdraw essence
    f.move_click(1789, 768)  # fill pouch
    f.move_click(744, 283)  # withdraw essence
    f.move_click(1789, 768)  # fill pouch
    f.move_click(744, 283)  # withdraw essence
    pag.press('esc')


def tp_shilo():
    f.move_right_click(1705, 765)
    tp = f.find_option('tp.png', (1705, 765), search_window=(150, 50, 300, 150))
    # print(tp)
    pag.moveTo(*tp, f.r())
    shilo = f.find('shilo.png')
    # print(shilo)
    pag.move(f.p(-125, -50), 0, f.r())
    f.move_click(*shilo)
    time.sleep(f.r(4, 5))


def climb_down_ladder():
    ladder = f.find('ladder.png',  area=(700, 400, 300, 300))
    # print(ladder)
    climb_down = f.find_option('climb_down.png', ladder)
    # print(climb_down)
    f.move_click(*climb_down)
    time.sleep(f.r(5, 6))
    x_tile = f.find('orientation_tile.png', area=(800, 350, 300, 300), threshold=0.30)
    print(x_tile)
    f.move_click(*x_tile)
    time.sleep(f.r(4, 5))


def go_to_altar():
    f.move_click(797, 333)  # use shortcut
    time.sleep(f.r(9, 10))  # wait to use
    f.move_click(566, 586)  # enter ruins
    time.sleep(f.r(5, 6))  # wait to enter


def craft_at_altar():
    f.move_click(739, 524, wait_duration=f.r(4, 5))
    f.move_click(1788, 766)  # empty pouch
    f.move_click(880, 527)  # craft natures
    f.move_click(1788, 766)  # empty pouch again
    f.move_click(880, 527)  # craft natures again


def return_to_bank():
    f.move_click(1747, 767, wait_duration=f.r(4, 5))  # tp to bank
    f.move_click(1120, 400, wait_duration=f.r(3, 4))  # access bank


def repair_pouch():
    pag.press('f4')
    mage = f.find_option('dark_mage.png', (1688, 787), )
    f.move_click(*mage)
    time.sleep(f.r(6, 7))
    pag.press('space')
    time.sleep(f.r(2, 3))
    pag.press('2')
    time.sleep(f.r(2, 3))
    pag.press('space')
    time.sleep(f.r(2, 3))
    pag.press('space')
    time.sleep(f.r(2, 3))
    pag.press('esc')
    pag.press('f2')


def craft_natures(repair=False):
    fill_inv()
    tp_shilo()
    climb_down_ladder()
    go_to_altar()
    craft_at_altar()
    if repair:
        repair_pouch()
    return_to_bank()


def main():
    set_up()
    for n in range(1, 300):
        fix = (n % 7 == 0)
        craft_natures(fix)


# main()
