import os
import functions as f
import pyautogui as pag
import cv2 as cv
import numpy as np


def find_spots(threshold=0.60):
    pag.screenshot('fish_spots.png', region=(0, 0, 1650, 1000))
    fish = cv.imread('fish.png', cv.IMREAD_UNCHANGED)
    fish_spots = cv.imread('fish_spots.png', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(fish_spots, fish, cv.TM_CCOEFF_NORMED)
    locations = np.where(result > threshold)
    locations = list(zip(*locations[::-1]))
    return locations


# find_spots()


pag.screenshot('fish_spots.png', region=(0, 0, 1650, 1000))
fish = cv.imread('fish.png', cv.IMREAD_UNCHANGED)
fish_spots = cv.imread('fish_spots.png', cv.IMREAD_UNCHANGED)
result = cv.matchTemplate(fish_spots, fish, cv.TM_CCOEFF_NORMED)
locations = np.where(result > 0.60)
locations = list(zip(*locations[::-1]))

if locations:
    image_h = fish.shape[0]
    image_w = fish.shape[1]
    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + image_w, top_left[1] + image_h)
        cv.rectangle(fish_spots, top_left, bottom_right, line_color, line_type)
    cv.imshow('Matches', fish_spots)
    cv.waitKey()
else:
    print('No matches :(')

