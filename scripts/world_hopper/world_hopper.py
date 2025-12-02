import pyautogui as pag
import functions as f
import time
import sys
import os
import numpy as np
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
    world_tab('open')
    pag.moveTo(1300 + f.p(), 100 + f.p())

    x = 1852
    h = length - 50
    screenshot = pag.screenshot(region=(x, 50, 1, h))  # width=1
    col = np.array(screenshot)[:, :, :3]               # shape (h,1,3)
    col = col.reshape(h, 3)

    # Compare each pixel row to detect changes
    diffs = np.any(col[1:] != col[:-1], axis=1)
    change_indices = np.where(diffs)[0] + 1 + 50

    adjusted_worlds = []
    last_y = change_indices[0]

    for y in change_indices[1:]:
        midpoint = int((last_y + y) / 2)
        adjusted_worlds.append((x, midpoint))
        last_y = y

    return adjusted_worlds


def check_world_number(world, debug=False):
    x = 1674
    xx = 28
    world_cords = (x, world[1] - 6)
    screenshot = f.take_screenshot((*world_cords, xx, 10), save_img=debug, img_name='wrld_num.png')
    w_num = de.read_digits(screenshot, number_type='w')
    return w_num


def check_world_population(world, debug=False):
    x = 1711
    xx = 28
    world_cords = (x, world[1] - 5)
    screenshot = f.take_screenshot((*world_cords, xx, 8), save_img=debug, img_name='world_pop.png')
    population = de.read_digits(screenshot, debug=debug)
    return population


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


def check_activity(world, debug=False):
    x = 1753
    y = world[1]
    allowed_colors = np.array([(255, 255, 255), (44, 44, 44), (40, 40, 40)])
    scr = pag.screenshot(region=(x, y-5, 15, 11))
    if debug:
        scr.save('activity_screenshot.png')
    scr = np.array(scr)
    matches_any = np.any(
        np.all(scr[:, :, None] == allowed_colors, axis=3), axis=2)

    illegal_mask = ~matches_any  # shape (8,15), True where illegal
    # True if any illegal pixel exists
    has_illegal = np.any(illegal_mask)
    return "bad world" if has_illegal else "good world"


def check_ping(world, debug=False):
    x = 1858
    xx = 20
    world_cords = (x, world[1] - 5)
    screenshot = f.take_screenshot((*world_cords, xx, 8), save_img=debug, img_name='ping.png')
    ping = de.read_digits(screenshot)
    return ping


def display_world_info(worlds, debug=False):
    for w in worlds:
        if check_world_type(w) == 'current':
            continue

        world_num = check_world_number(w, debug)
        print(f'World number {world_num}')
        pop = check_world_population(w, debug)
        print(f'World population: {pop}')
        world_type = check_world_type(w)
        print(f'World type: {world_type}')
        world_activity = check_activity(w, debug)
        print(f'World activity: {world_activity}')
        world_ping = check_ping(w, debug)
        print(f'World ping: {world_ping}')
        print()


def gen_world_list(length):
    world_l = create_world_list(length)
    print(f'List of {len(world_l)} worlds created')
    print()
    return world_l


wl = gen_world_list(400)
display_world_info(wl, True)
