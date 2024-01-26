import pyautogui
import pyautogui as pag
import time
import os
import json


def check_inv():
    script_dir = os.path.dirname(__file__)
    img = os.path.join(script_dir, 'images', 'maple_bow_full_inv.png')
    image_pos = None
    print('Searching', end='')
    for s in range(1, 91):
        try:
            image_pos = pyautogui.locateOnScreen(img)
            print('image found!')
        except pyautogui.ImageNotFoundException:
            pass
        if image_pos:
            break
        print('.', end='')
        time.sleep(1)
    print('Done!')


def check_pixel(x, y, rgb, t=5):
    if pag.pixelMatchesColor(x, y, rgb, tolerance=t):
        print('Match!')
    else:
        print('No match.')


# check_inv()

check_pixel(750, 322, (255, 242, 0), t=5)
