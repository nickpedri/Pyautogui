import cv2 as cv
import pyautogui as pag
import time


# Capturing a smaller piece of the screen is much faster
start_time = time.time()
screenshot2 = pag.screenshot('s2.png', region=(550, 370, 500, 500))
end_time = time.time()
print(end_time - start_time)

s1 = cv.imread('s2.png', cv.IMREAD_UNCHANGED)
cv.imshow('full screen', s1)
cv.waitKey()
