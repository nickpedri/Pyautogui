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
from PIL import Image


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


def take_screenshot(area=(0, 0, 1920, 1080), save_img=False):
    """ This function takes a screenshot of a specified area of the screen and returns it ready for match template."""
    screenshot = pag.screenshot(region=area)
    if save_img:
        screenshot.save("screenshot.png")
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    return screenshot


def isolate_exact_yellow(bgr_image, tolerance=10):
    """
    Keep only pixels that are very close to pure yellow (BGR 255,255,0)
    tolerance: how many HSV units around the exact yellow to allow
    """
    # Convert BGR to HSV
    hsv = cv.cvtColor(bgr_image, cv.COLOR_BGR2HSV)

    # Pure yellow in BGR is (0, 255, 255) in HSV
    # Hue for yellow ~30, Saturation ~255, Value ~255
    # We'll allow a small tolerance for Hue/Sat/Val
    lower_yellow = np.array([30 - tolerance, 255 - tolerance, 255 - tolerance])
    upper_yellow = np.array([30 + tolerance, 255, 255])  # keep saturation/value at max

    # Create mask
    mask = cv.inRange(hsv, lower_yellow, upper_yellow)

    # Apply mask: keep yellow, black out everything else
    result = cv.bitwise_and(bgr_image, bgr_image, mask=mask)

    # Convert to grayscale
    gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)

    # Threshold to pure black and white
    _, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    return thresh


def to_pil_and_resize(cv_image, x=5, y=5, resize=True):
    """Convert OpenCV grayscale/BGR image to PIL Image for pytesseract."""
    if resize:
        cv_image = cv.resize(cv_image, None, fx=x, fy=y, interpolation=cv.INTER_CUBIC)
    if len(cv_image.shape) == 2:  # grayscale
        return Image.fromarray(cv_image)
    else:  # BGR
        rgb_image = cv.cvtColor(cv_image, cv.COLOR_BGR2RGB)
        return Image.fromarray(rgb_image)


def move_click(x, y, move_duration=r(), wait_duration=r(), r1=p(), r2=p()):
    """ This function takes in x and y coordinates, and a movement and wait duration and executes actions."""
    pag.moveTo(x + r1, y + r2, move_duration)
    pag.click()
    time.sleep(wait_duration)


def move_right_click(x, y, move_duration=r(), wait_duration=r(), r1=p(), r2=p()):
    """ This function takes in x and y coordinates, and a movement and wait duration and executes actions."""
    pag.moveTo(x + r1, y + r2, move_duration)
    pag.rightClick()
    time.sleep(wait_duration)


def check_pixel_color_in_area(search_region=(960, 540, 6, 6), target_color=(0, 255, 0), tolerance=5):
    """
    Checks if the target color exists within the specified area of the image.
    Args:
        search_region (tuple): Tuple containing (top left x coordinate, top left y coordinate, width, height) of
        the search area.
        target_color (tuple): BGR color tuple to check for (e.g., (0, 0, 255) for red).
        tolerance (int):
    Returns:
        bool: True if the color is found, False otherwise.
    """
    s = search_region
    x, y, w, h = s[0], s[1], s[2], s[3]
    pixel_match = False

    for pix in range(x, (x + w + 1)):
        for p2 in range(y, (y + h + 1)):
            pixel_match = pag.pixelMatchesColor(pix, p2, target_color, tolerance=tolerance)
            if pixel_match:
                break
        if pixel_match:
            break

    if pixel_match:
        return True
    else:
        return False


def find(locate_img, area=(0, 0, 1920, 1080)):
    """ This function takes in the name of an image file to search, and the search region, it will find the best
    match for the image within the taken screenshot. It returns the x and y coordinates for the location of the best
    match on screen."""
    haystack = take_screenshot(area)
    needle = cv.imread(locate_img, cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack, needle, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    needle_w = round(needle.shape[1] / 2)
    needle_h = round(needle.shape[0] / 2)
    estimated_start_loc = (max_loc[0] + needle_w + area[0], max_loc[1] + needle_h + area[1])
    return estimated_start_loc


def find_spots(locate_img, threshold=0.50, area=(0, 0, 1920, 1080)):
    """ This function takes in the name of an image file to search, and threshold for image recognition. It will return
    the locations of every match above the threshold."""
    haystack = take_screenshot(area)
    needle = cv.imread(locate_img, cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack, needle, cv.TM_CCOEFF_NORMED)
    locations = np.where(result > threshold)
    locations = list(zip(*locations[::-1]))
    if locations:
        return locations
    else:
        pass
        # print('No results found.')


def create_rectangles(locate_img, coordinates, group_threshold=1, eps=0.50):
    """ This function takes in the name of an image to read, coordinates for locations, and function parameters. It then
    creates and returns a list of lists containing the x and y coordinates and height and width of the rectangles."""
    needle = cv.imread(locate_img, cv.IMREAD_UNCHANGED)
    rectangles = []
    for loc in coordinates:
        rect = [int(loc[0]), int(loc[1]), needle.shape[1], needle.shape[0]]
        rectangles.append(rect)
        rectangles.append(rect)
    rectangles, weights = cv.groupRectangles(rectangles, group_threshold, eps)
    return rectangles


def draw_rectangles(haystack, locations, show=True):
    """ This function takes in an imread image and a list of rectangles and draws and draws a rectangle around
    each search result."""
    if len(locations):
        line_color = (0, 0, 255)
        line_type = cv.LINE_4

        for (x, y, w, h) in locations:
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            cv.rectangle(haystack, top_left, bottom_right, line_color, line_type)
        if show:
            cv.imshow('Matches', haystack)
            cv.waitKey()
    else:
        print('No matches :(')


def draw_markers(haystack, rectangles, show=True):
    """ This function takes in an imread image and a list of rectangles and draws and draws a marker on
        each search result."""
    if len(rectangles):
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS
        for (x, y, w, h) in rectangles:
            center = ((x + int(w/2)), y + int(h/2))
            cv.drawMarker(haystack, center, marker_color, marker_type)
        if show:
            cv.imshow('Matches', haystack)
            cv.waitKey()
    else:
        print('No matches :(')


def shift_camera_direction(direction='north', up=True):
    """ This function shifts the camera direction to a specific direction and can zoom out all the way."""
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

    def __init__(self, window_name=None, area=(0, 0, 1920, 1080)):

        # Determine hwnd (window name)
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception(f'Window not found: {window_name}')

        # account for the window border and titlebar and cut them off if window name
        if window_name:
            window_rect = win32gui.GetWindowRect(self.hwnd)
            print(window_rect)
            self.w = window_rect[2] - window_rect[0]
            self.h = window_rect[3] - window_rect[1]
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
        else:
            # area = ( x coordinate, y coordinate, width of area, height of area)
            self.w, self.h, self.cropped_x, self.cropped_y = area[2], area[3], area[0], area[1]

    def get_screenshot(self):
        # screenshot_name = "debug.bmp"  # set this
        # get the window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

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

        # drop the alpha channel, or cv.matchTemplate() will throw an error like:
        #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type()
        #   && _img.dims() <= 2 in function 'cv::matchTemplate'
        screencapture = screencapture[..., :3]

        # make image C_CONTIGUOUS to avoid errors that look like:
        #   File ... in draw_rectangles
        #   TypeError: an integer is required (got type tuple)
        # see the discussion here:
        # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
        screencapture = np.ascontiguousarray(screencapture)
        return screencapture

    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd):
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


class Vision:

    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None

    # constructor
    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):
        # load the image we're trying to match
        # https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

        # Save the dimensions of the needle image
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def find(self, haystack_img, threshold=0.5, debug_mode=None):
        # run the OpenCV algorithm
        result = cv.matchTemplate(haystack_img, self.needle_img, self.method)

        # Get the all the positions from the match result that exceed our threshold
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        # print(locations)

        # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
        # locations by using groupRectangles().
        # First we need to create the list of [x, y, w, h] rectangles
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)
        # Apply group rectangles.
        # The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
        # done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
        # in the result. I've set eps to 0.5, which is:
        # "Relative difference between sides of the rectangles to merge them into a group."
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        # print(rectangles)

        points = []
        if len(rectangles):
            # print('Found needle.')

            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv.MARKER_CROSS

            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:

                # Determine the center position
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                # Save the points
                points.append((center_x, center_y))

                if debug_mode == 'rectangles':
                    # Determine the box position
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    # Draw the box
                    cv.rectangle(haystack_img, top_left, bottom_right, color=line_color,
                                 lineType=line_type, thickness=2)
                elif debug_mode == 'points':
                    # Draw the center point
                    cv.drawMarker(haystack_img, (center_x, center_y),
                                  color=marker_color, markerType=marker_type,
                                  markerSize=40, thickness=2)

        if debug_mode:
            cv.imshow('Matches', haystack_img)
            # cv.waitKey()
            # cv.imwrite('result_click_point.jpg', haystack_img)

        return points
