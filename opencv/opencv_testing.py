import cv2 as cv
import pyautogui as pag
import time


# Capturing a smaller piece of the screen is much faster
# start_time = time.time()
# screenshot2 = pag.screenshot('s1.png', region=(550, 370, 500, 500))
# end_time = time.time()


def locate_simon():
    pag.screenshot('s1.png', region=(550, 370, 500, 500))
    simon_area = cv.imread('s1.png', cv.IMREAD_UNCHANGED)
    simon = cv.imread('simon_templeton.png', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(simon_area, simon, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    simon_w = simon.shape[1] / 2
    simon_h = simon.shape[0] / 2

    simon_location = (max_loc[0] + 550 + simon_w, max_loc[1] + 370 + simon_h)
    # print(simon_location)
    return simon_location


start_time = time.time()
elapsed_time = 0

while elapsed_time < 10:
    pag.moveTo(locate_simon())
    elapsed_time = time.time() - start_time
    print(elapsed_time)
