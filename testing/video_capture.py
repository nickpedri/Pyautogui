import os
import cv2 as cv
import functions as f


os.chdir(os.path.dirname(os.path.abspath(__file__)))


def capture_runelite():
    wincap = f.WindowCapture('RuneLite - Crad Booper')

    while True:

        screenshot = f.take_screenshot()  # Capture screenshot
        cv.imshow('Computer Vision', screenshot)

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


capture_runelite()
