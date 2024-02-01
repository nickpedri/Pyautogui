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


def highlight_results(needle, haystack, locations):
    image2 = cv.imread(needle, cv.IMREAD_UNCHANGED)
    image1 = cv.imread(haystack, cv.IMREAD_UNCHANGED)
    if locations:
        image_h = image2.shape[0]
        image_w = image2.shape[1]
        line_color = (0, 0, 255)
        line_type = cv.LINE_4

        for loc in locations:
            top_left = loc
            bottom_right = (top_left[0] + image_w, top_left[1] + image_h)
            cv.rectangle(image1, top_left, bottom_right, line_color, line_type)
        cv.imshow('Matches', image1)
        cv.waitKey()
    else:
        print('No matches :(')


res = find_spots(.55)
highlight_results('fish.png', 'fish_spots.png', res)
print(res)


