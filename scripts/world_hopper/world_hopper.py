import pyautogui as pag
import functions as f
import time
import sys
import os
import cv2 as cv
import digit_extractor as de

# Add the number_extraction folder to Python's module search path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EXTRACTOR_DIR = os.path.join(SCRIPT_DIR, "..", "number_extraction")

sys.path.append(os.path.abspath(EXTRACTOR_DIR))


def world_tab(command):
    pag.moveTo(100 + f.p(), 100 + f.p())
    open_color = (220, 138, 0)
    color_location = (1890, 137)
    location = (1904, 139)
    pixel_match = pag.pixelMatchesColor(*color_location, open_color, tolerance=5)

    if command == 'open' and pixel_match:
        print('World tab is already open.')

    if command == 'close' and pixel_match:
        print('Closing world tab.')
        f.move_click(*location)

    if command == 'close' and not pixel_match:
        print('World tab is already closed.')

    if command == 'open' and not pixel_match:
        print('Opening world tab.')
        f.move_click(*location)


def create_world_list(length):
    pag.moveTo(1300 + f.p(), 100 + f.p())
    world_tab('open')
    x = 1852
    worlds = list()
    current_px_color = (0, 0, 0)

    for y in range(50, length):
        pix = pag.pixel(x, y)
        if pix != current_px_color:
            worlds.append((x, y))
            current_px_color = pix

    adjusted_worlds = []
    top_edge = 0
    worlds.pop(0)
    ls = len(worlds)

    for w, n in zip(worlds, range(1, ls + 1)):
        if n == 1:
            top_edge = w[1]
            continue
        adjusted_worlds.append((x, int(round(w[1] + top_edge)/2)))
        top_edge = w[1]

    return adjusted_worlds


def check_world_type(world):
    x = 1674
    p2p_color = (210, 193, 53)
    current_world_color = (66, 227, 17)
    if f.check_pixel_color_in_area((x, world[1], 20, 0), current_world_color):
        world_type = 'current'
    elif f.check_pixel_color_in_area((x, world[1], 20, 0), p2p_color):
        world_type = 'p2p'
    else:
        world_type = 'f2p'
    return world_type


def check_world_population(world):
    templates = de.load_templates()
    x = 1711
    xx = 28
    world_cords = (x, world[1] - 5)

    screenshot = f.take_screenshot((*world_cords, xx, 8), save_img=True)

    population = de.read_digits(screenshot)
    return population


def hop_world():
    pass


def hover_options(options):
    for world in options:
        # pag.moveTo(*world)
        w_type = check_world_type(world)
        pop = check_world_population(world)
        print('World type: ', w_type)
        print('World population: ', pop)
        print()
        time.sleep(.1)


world_list = create_world_list(250)
hover_options(world_list)
