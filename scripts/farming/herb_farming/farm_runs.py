import functions as f
import pyautogui as pag
import time
import numpy as np
import cv2 as cv


def set_up():
    f.shift_camera_direction('north')
    pag.moveTo(1140 + f.p(0, 100), 500 + f.p(0, 100), f.r(0, 1))
    pag.scroll(-10000)
    pag.press('f2')


def enter_game():
    f.move_click(945, 285, wait_duration=f.r(10, 12))
    f.move_click(950, 354, wait_duration=f.r(2, 3))


def open_bank(bank=None):
    if bank is None:
        bank = (944, 561)
    if f.is_bank_open():
        return
    f.move_click(*bank)
    pin = ['7', '3', '5', '7']
    time.sleep(f.r(1, 1.5))
    if f.is_bank_open():
        return None
    for n in pin:
        pag.press(n)
        time.sleep(f.r(1, 1.5))
    f.wait_until(f.is_bank_open)


def navigate_to_tab():
    f.move_click(640, 103)
    pag.moveTo(600 + f.p(5), 247 + f.p(5), f.r(0, 0.5))
    for i in range(10):
        pag.scroll(100)
        time.sleep(0.015)
    pag.click()


def gear_up():
    navigate_to_tab()
    f.move_click(1002, 821, 'fast')  # deposit items
    f.move_click(1040, 821, 'fast')  # deposit gear
    f.set_deposit('one')
    gear = [(696, 210), (696, 252), (696, 285), (646, 178), (647, 212), (743, 211), (743, 283), (696, 137)]
    items = [(838, 143), (887, 143), (936, 146), (982, 143),
             (838, 177), (887, 177), (936, 177), (982, 177)]
    for g in gear:
        f.move_click(*g, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.1, 0.15))
    pag.press('esc')
    time.sleep(f.r())
    inv = list(f.create_inv_grid().values())
    for xy in range(0, 8):  # equip slots 2-7
        f.move_click(*inv[xy], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.1, 0.15))
    open_bank()
    navigate_to_tab()
    for i in items:
        f.move_click(*i, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.1, 0.15))
    f.set_deposit('all')
    f.move_click(838, 212, 'fast')
    f.move_click(887, 212, 'fast')
    pag.press('esc')
    f.wait_until(lambda: not(f.is_bank_open()))


gear_up()
