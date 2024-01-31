import cv2 as cv
import pyautogui as pag
import time
from testing.randomizers import p, r


# Capturing a smaller piece of the screen is much faster
# start_time = time.time()
# screenshot2 = pag.screenshot('s1.png', region=(550, 370, 500, 500))
# end_time = time.time()


def locate_simon():
    timer = time.time()
    pag.screenshot('s1.png', region=(550, 370, 500, 500))
    simon_area = cv.imread('s1.png', cv.IMREAD_UNCHANGED)
    simon = cv.imread('../scripts/agility_pyramid/simon_templeton.png', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(simon_area, simon, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    simon_w = simon.shape[1] / 2
    simon_h = simon.shape[0] / 2

    simon_location = (max_loc[0] + 550 + simon_w, max_loc[1] + 370 + simon_h)
    # print(simon_location)
    print(time.time() - timer)
    return simon_location


def trade_with_simon():
    pag.moveTo(811 + p(-4, 4), 555 + p(-4, 4), r(0.25, 0.75))
    pag.click()
    time.sleep(6 + r(0.5, 0.9))

    start_time = time.time()
    elapsed_time = 0
    print('Searching for simon ', end='')

    while elapsed_time < 20:
        simon_movement = [locate_simon(), locate_simon()]
        if simon_movement[-1] == simon_movement[-2]:
            pag.moveTo(simon_movement[-1])
            pag.click()
            print('simon found!')
            # print(simon_movement)
            break
        elapsed_time = time.time() - start_time
        print('.', end='')
    if elapsed_time > 20:
        print('Could not locate simon.')
        # print(elapsed_time)
    else:
        time.sleep(6 + r(0.5, 0.9))
        pag.press('space')
        time.sleep(2 + r(0, 1))
        pag.press('1')
        time.sleep(2 + r(0, 1))
        print('Finished trading!')


def locate_start():
    pag.screenshot('s2.png', region=(0, 0, 1920, 1080))
    start_area = cv.imread('s2.png', cv.IMREAD_UNCHANGED)
    start_tile = cv.imread('start_tile.png', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(start_area, start_tile, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    estimated_start_loc = (max_loc[0], max_loc[1] - 20)
    return estimated_start_loc


def reset_position():
    pag.moveTo(locate_start())
    time.sleep(0.25)
    pag.click()
    time.sleep(5)
    pag.moveTo(974 + p(-4, 4), 536 + p(-4, 4), r(0.25, 0.75))
    pag.click()
    time.sleep(7)
    pag.moveTo(1037 + p(-4, 4), 506 + p(-4, 4), r(0.25, 0.75))
    pag.click()


# locate_simon()
# trade_with_simon()
# reset_position()
