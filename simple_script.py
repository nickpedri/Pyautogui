import time
import functions as f
import pyautogui as pag
import cv2 as cv
import numpy as np

for n in range(1, 105):
    f.play_actions('clean_herbs.json')
    time.sleep(1)
