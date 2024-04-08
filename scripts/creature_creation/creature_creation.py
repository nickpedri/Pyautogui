import time
import functions as f
import pyautogui as pag
import cv2 as cv
import numpy as np


reset_tile = f.find('reset_tile_monastery.png')
take_option = f.find('take_option.png')
f.move_click(*take_option)
