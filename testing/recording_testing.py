import os
import pyautogui as pag
from pynput import mouse, keyboard
from time import time
import json

# Declare mouse_listener globally so that keyboard on release can stop it
# mouse_listener = None
# Declare start_time globally so that the callback functions can reference it
start_time = None


def elapsed_time():
    global start_time
    return time() - start_time


def press_release(press):
    # Returns pressed or released based on true or false value passed in by pressed
    return 'pressed' if press else 'released'


def on_click(x, y, button, pressed):
    print(f'{button} {press_release(pressed)} on {(x, y)} at {elapsed_time()}')


def on_press(key):
    try:
        print(f'alphanumeric key {key.char} pressed')
    except AttributeError:
        print(f'special key {key} pressed')


def on_release(key):
    print(f'{key} released')
    if key == keyboard.Key.f10:
        # Stop listener
        return False


def run_listeners():
    # global mouse_listener
    # Start mouse listener
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()
    mouse_listener.wait()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        global start_time
        start_time = time()
        listener.join()


# run_listeners()


def test_click_speed(coordinates=None, x=1):
    if x == 1:
        pag.mouseDown(coordinates)
        pag.mouseUp(coordinates)
        pag.mouseDown(coordinates)
        pag.mouseUp(coordinates)
        # Testing shows this action takes around .19s
    if x == 2:
        pag.click(coordinates)
        pag.click(coordinates)
        # Testing shows this action takes around .09s


test_click_speed()
