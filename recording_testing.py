import os
from pynput import mouse, keyboard
from time import time
import json


def press_release(press):
    return 'pressed' if press else 'released'


def on_click(x, y, button, pressed):
    print(f'{button} {press_release(pressed)} at {(x, y)}')


with mouse.Listener(on_click=on_click)as listener:
    listener.join()
