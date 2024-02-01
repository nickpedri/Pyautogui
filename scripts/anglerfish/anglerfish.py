import os
import functions as f
import pyautogui as pag
import cv2 as cv
import numpy as np

# functions are designed to work at 25% zoom

needle = cv.imread('fish.png', cv.IMREAD_UNCHANGED)


def find_spots(threshold=0.60):
    pag.screenshot('fish_spots.png', region=(0, 0, 1650, 1000))
    global needle
    haystack = cv.imread('fish_spots.png', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack, needle, cv.TM_CCOEFF_NORMED)
    locations = np.where(result > threshold)
    locations = list(zip(*locations[::-1]))
    return locations


def highlight_results(haystack, locations):
    global needle
    image1 = cv.imread(haystack, cv.IMREAD_UNCHANGED)
    if len(locations):
        line_color = (0, 0, 255)
        line_type = cv.LINE_4

        for (x, y, w, h) in locations:
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            cv.rectangle(image1, top_left, bottom_right, line_color, line_type)
        cv.imshow('Matches', image1)
        cv.waitKey()
    else:
        print('No matches :(')


# res = find_spots(.55)
# highlight_results('fish_spots.png', res)
# print(res)

def create_rectangles(coordinates):
    global needle
    rectangles = []
    for loc in coordinates:
        rect = [int(loc[0]), int(loc[1]), needle.shape[1], needle.shape[0]]
        rectangles.append(rect)
    return rectangles


res = find_spots(.50)
the_rectangles = create_rectangles(res)
highlight_results('fish_spots.png', the_rectangles)

the_rectangles, weights = cv.groupRectangles(the_rectangles, 2, 0.50)
highlight_results('fish_spots.png', the_rectangles)
print(the_rectangles)
