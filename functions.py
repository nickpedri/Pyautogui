import random
import cv2 as cv
import time
import pyautogui as pag
import os
import json
import win32con
import win32gui
import win32ui
import numpy as np


def r(a=0.25, b=0.75):  # Define function and define numbers
    """ Function returns a random number between a and b"""
    return random.uniform(a, b)  # Return numbers


def p(a=3, b=None):  # Define function and define numbers
    """ This function returns a random integer between a and b or -a and a, if b isn't specified"""
    if b is None:
        return random.randint(-a, a)  # Return integers
    else:
        return random.randint(a, b)


def initialize_pag():
    """ Function simply enables the pag failsafe"""
    pag.FAILSAFE = True  # Turn on failsafe
    print('Pyautogui failsafe enabled!')


def countdown(seconds=3):
    """ This function starts a simple countdown timer"""
    print(f'Starting', end='')
    for s in range(1, seconds + 1):
        print('.', end='')
        time.sleep(1)
    print(' now!')


def move_click(x, y, move_duration=r(), wait_duration=r()):
    pag.moveTo(x + p(), y + p(), move_duration)
    pag.click()
    time.sleep(wait_duration)


def move_right_click(x, y, move_duration=r(), wait_duration=r()):
    pag.moveTo(x + p(), y + p(), move_duration)
    pag.rightClick()
    time.sleep(wait_duration)


def find(locate_img, area=(0, 0, 1920, 1080)):
    pag.screenshot('temporary_img.png', region=area)
    haystack = cv.imread('temporary_img.png', cv.IMREAD_UNCHANGED)
    needle = cv.imread(locate_img, cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack, needle, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    needle_w = needle.shape[1] / 2
    needle_h = needle.shape[0] / 2
    estimated_start_loc = (max_loc[0] + needle_w + area[0], max_loc[1] + needle_h + area[1])
    return estimated_start_loc


def shift_camera_direction(direction='north', up=True):
    pag.moveTo(1725 + p(-8, 8), 52 + p(-8, 8), r(0.75, 0.90))
    time.sleep(r(0.15, 0.80))
    if direction == 'north':
        pag.click()
    elif direction == 'east':
        pag.rightClick()
        time.sleep(r(0.10, 0.30))
        pag.move(0 + p(-5, 5), 42 + p(), r(0.75, 0.90))
        time.sleep(r(0.10, 0.30))
        pag.click()
    elif direction == 'south':
        pag.rightClick()
        time.sleep(r(0.10, 0.30))
        pag.move(0 + p(-5, 5), 57 + p(), r(0.75, 0.90))
        time.sleep(r(0.10, 0.30))
        pag.click()
    elif direction == 'west':
        pag.rightClick()
        time.sleep(r(0.10, 0.30))
        pag.move(0 + p(-5, 5), 72 + p(), r(0.75, 0.90))
        time.sleep(r(0.10, 0.30))
        pag.click()
    time.sleep(r(0.25, 1.5))
    if up:
        pag.keyDown('up')
        time.sleep(3)
        pag.keyUp('up')


def convert_key(key):
    """ This function is a simple converter to translate pynput keys to pag readable keys"""
    key_map = {
        'alt_l': 'altleft',
        'alt_r': 'altright',
        'alt_gr': 'altright',
        'caps_lock': 'capslock',
        'ctrl_l': 'ctrlleft',
        'ctrl_r': 'ctrlright',
        'page_down': 'pagedown',
        'page_up': 'pageup',
        'shift_l': 'shiftleft',
        'shift_r': 'shiftright',
        'num_lock': 'numlock',
        'print_screen': 'printscreen',
        'scroll_lock': 'scrolllock'}
    # example: 'Key.F9' should return 'F9', 'w' should return as 'w'
    cleaned_key = key.replace('Key.', '')
    if cleaned_key in key_map:
        return key_map[cleaned_key]
    return cleaned_key


def play_actions(filename, new_path=None):
    """ This function reads json 'recording' files"""
    previous_position = None
    if new_path:
        script_dir = new_path
    else:
        script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, filename)
    with open(filepath, 'r') as jsonfile:
        data = json.load(jsonfile)
        for index, action in enumerate(data):
            start_time = time.time()
            if action['button'] == 'Key.f10':
                break
            # Perform action
            elif action['type'] == 'KeyDown':
                key = convert_key(action['button'])
                # key = key[4:] if key[:4] == 'Key.' else key
                pag.keyDown(key)
            elif action['type'] == 'KeyUp':
                key = convert_key(action['button'])
                # key = key[4:] if key[:4] == 'Key.' else key
                pag.keyDown(key)

            elif action['type'] == 'clickDown':
                previous_position = (action['pos'][0], action['pos'][1])
                pag.moveTo(action['pos'][0] + p(-4, 4), action['pos'][1] + p(-4, 4), duration=r(0.25, 0.70))
                pag.mouseDown()
            elif action['type'] == 'clickUp':
                if previous_position == (action['pos'][0], action['pos'][1]):
                    pag.mouseUp()
                else:
                    pag.moveTo(action['pos'][0] + p(-4, 4), action['pos'][1] + p(-4, 4), duration=r(0.25, 1.00))
                    pag.mouseUp()

            # Sleep until next action
            try:
                next_action = data[index + 1]
            except IndexError:
                break
            elapsed_time = time.time() - start_time
            wait_time = next_action['time'] - action['time']
            if wait_time >= 0:
                wait_time -= elapsed_time
                if wait_time < 0:
                    wait_time = 0
                if action['type'] == 'clickDown':
                    time.sleep(wait_time)
                else:
                    time.sleep(wait_time + r(0, 0.30))
            else:
                raise Exception('Unexpected action ordering.')


class WindowCapture:

    # Properties
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    def __init__(self, window_name=None):

        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception(f'Window not found: {window_name}')

        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # account for the window border and titlebar and cut them off
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        # set the cropped coordinates offset, so we can translate screenshot
        # images into actual screen positions
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    def capture_window(self):
        # screenshot_name = "debug.bmp"  # set this

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (8, 30), win32con.SRCCOPY)

        # save screenshot
        # dataBitMap.SaveBitmapFile(cDC, screenshot_name)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        screencapture = np.fromstring(signedIntsArray, dtype='uint8')
        screencapture.shape = (self.h, self.w, 4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        screencapture = screencapture[..., :3]
        screencapture = np.ascontiguousarray(screencapture)

        return screencapture

    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))

        win32gui.EnumWindows(winEnumHandler, None)

    # translate a pixel position on a screenshot image to a pixel position on the screen.
    # pos = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the __init__ constructor.
    def get_screen_position(self, pos):
        return pos[0] + self.offset_x, pos[1] + self.offset_y


def take_screenshot(region=(0, 0, 1980, 1020), hwnd=None, save_screenshot=False, screenshot_name='screenshot'):
    x = region[0]
    y = region[1]
    w = region[2]
    h = region[3]
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (x, y), win32con.SRCCOPY)

    # save screenshot
    if save_screenshot:
        dataBitMap.SaveBitmapFile(cDC, screenshot_name)

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    screenshot = np.fromstring(signedIntsArray, dtype='uint8')
    screenshot.shape = (h, w, 4)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    screenshot = screenshot[..., :3]
    screenshot = np.ascontiguousarray(screenshot)

    return screenshot
