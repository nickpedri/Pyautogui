import os
import cv2 as cv
import functions as f


os.chdir(os.path.dirname(os.path.abspath(__file__)))

f.WindowCapture.list_window_names()

wincap = f.WindowCapture('RuneLite - Crad Booper')

while True:

    screenshot = f.WindowCapture.capture_window(wincap)  # Capture screenshot
    cv.imshow('Computer Vision', screenshot)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


