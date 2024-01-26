import pyautogui
import pyautogui as pag
import time
import os
from randomizers import r, p


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
        pass
    else:
        pag.moveTo(972 + p(-4, 4), 535 + p(-4, 4), r(0.25, 0.75))
        pag.click()
        time.sleep(1 + r(0, 1))


def wait_for(image):
    script_dir = os.path.dirname(__file__)
    img = os.path.join(script_dir, 'images', image)
    while True:
        try:
            pyautogui.locateOnScreen(img, confidence=0.95)
            print(f'Found at: {pyautogui.locateOnScreen(img, confidence=0.95)}')
            break
        except pyautogui.ImageNotFoundException:
            print('Not found!')
            time.sleep(0.25)


check_pixel(954, 506, (0, 255, 0), 5)
