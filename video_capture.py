import os
import cv2 as cv
import functions as f
import time


os.chdir(os.path.dirname(os.path.abspath(__file__)))


def capture_runelite():
    # wincap = f.WindowCapture('Runelite - Crad Booper')
    wincap = f.WindowCapture()

    while True:
        t = time.time()
        screenshot = wincap.capture_window()  # Capture screenshot
        # screenshot = f.take_screenshot()  # Capture screenshot
        matches = f.find_spots('search_img.png', 0.70, area=(1000, 800, 920, 280))
        if matches:
            rectangles = f.create_rectangles('search_img.png', matches)
            f.draw_rectangles(screenshot, rectangles, False)
        cv.imshow('Computer Vision', screenshot)
        print(f'{round(1/(time.time() - t))} fps')

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


capture_runelite()
