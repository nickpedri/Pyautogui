import os
import functions as f
import pyautogui as pag
import cv2 as cv
import numpy as np

# functions are designed to work at 25% zoom

needle = cv.imread('fish2.png', cv.IMREAD_UNCHANGED)
character_location = (945, 540)


def find_spots(threshold=0.60):
    pag.screenshot('fish_spots.png', region=(0, 0, 1650, 1000))
    global needle
    haystack = cv.imread('fish_spots.png', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack, needle, cv.TM_CCOEFF_NORMED)
    locations = np.where(result > threshold)
    locations = list(zip(*locations[::-1]))
    return locations


def create_rectangles(coordinates, group_threshold=1, eps=0.50):
    global needle
    rectangles = []
    for loc in coordinates:
        rect = [int(loc[0]), int(loc[1]), needle.shape[1], needle.shape[0]]
        rectangles.append(rect)
        rectangles.append(rect)
    rectangles, weights = cv.groupRectangles(rectangles, group_threshold, eps)
    return rectangles


def draw_rectangles(haystack, locations):
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


def draw_markers(haystack, rectangles):
    img = cv.imread(haystack, cv.IMREAD_UNCHANGED)
    marker_color = (255, 0, 255)
    marker_type = cv.MARKER_CROSS
    for (x, y, w, h) in rectangles:
        center = ((x + int(w/2)), y + int(h/2))
        cv.drawMarker(img, center, marker_color, marker_type)
    cv.imshow('Matches', img)
    cv.waitKey()


def find_click_spots(rectangles):
    click_points = []
    for (x, y, w, h) in rectangles:
        center = ((x + int(w/2)), y + int(h/2))
        click_points.append(center)
    return click_points


def calculate_distance(click_points):
    global character_location
    distances = []
    closest = 0
    for (x, y) in click_points:
        total_distance = abs(x - character_location[0]) + abs(y - character_location[1])
        distances.append(total_distance)
    return distances


results = find_spots(.50)
results = create_rectangles(results)
results = find_click_spots(results)
# draw_rectangles('fish_spots.png', results)
# draw_markers('fish_spots.png', results)
print(results)
print(calculate_distance(results))
