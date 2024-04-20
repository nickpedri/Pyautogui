import os
import cv2 as cv
import functions as f
import time


os.chdir(os.path.dirname(os.path.abspath(__file__)))


def capture_runelite():
    # wincap = f.WindowCapture('RuneLite - Crad Booper')

    while True:
        t = time.time()
        screenshot = f.take_screenshot()  # Capture screenshot
        cv.imshow('Computer Vision', screenshot)
        print(f'{round(1/(time.time() - t))} fps')

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


capture_runelite()
