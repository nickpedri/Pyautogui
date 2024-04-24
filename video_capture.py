import os
import cv2 as cv
import functions as f
import time
from functions import WindowCapture, Vision

# initialize the WindowCapture class

wincap = WindowCapture()
# initialize the Vision class
vision_limestone = Vision('search_img.png')


def capture_runelite():

    loop_time = time.time()

    while True:

        # get an updated image of the game
        screenshot = wincap.get_screenshot()

        # display the processed image
        points = vision_limestone.find(screenshot, 0.45, 'rectangles')
        # points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

        # debug the loop rate
        print('FPS {}'.format(1 / (time.time() - loop_time)))
        loop_time = time.time()

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

    print('Done.')

capture_runelite()