import pyautogui
import pyautogui as pag
import time
import os
import json


def check_inv():
    script_dir = os.path.dirname(__file__)
    img = os.path.join(script_dir, 'images', 'maple_bow_full_inv.png')
    image_pos = pyautogui.locateOnScreen(img)
    #try:
    #    image_pos = pyautogui.locateOnScreen(img)
    #    print(image_pos)
    #except pyautogui.ImageNotFoundException:
    #    print('Not found :(')


check_inv()
