import time
import functions as f
import os
import random
import pyautogui as pag
import cv2 as cv
import numpy as np


def fletch():
    f.move_click(1705, 766, f.r(0.011, 0.024), f.r(0.004, 0.011), r1=f.p(7), r2=f.p(7))
    f.move_click(1705, 799, f.r(0.013, 0.027), f.r(0.002, 0.012), r1=f.p(7), r2=f.p(7))


for n in range(1, 500):
    fletch()
    print(n)
