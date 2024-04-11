import time
import functions as f
import os
import pyautogui as pag
import cv2 as cv
import numpy as np


project_dir = os.path.dirname(__file__)

for n in range(1, 59):
    f.play_actions('', project_dir)
    time.sleep(1)
    print(f'Loop {n} done!')
