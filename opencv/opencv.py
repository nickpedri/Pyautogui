import cv2 as cv
import numpy as np

simon_area = cv.imread('simon_area.png', cv.IMREAD_UNCHANGED)
simon = cv.imread('simon_templeton.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(simon_area, simon, cv.TM_CCOEFF_NORMED)

# cv.imshow('Result', result)
# cv.waitKey()

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

simon_w = simon.shape[1]
simon_h = simon.shape[0]

# Calculate the bottom right corner of the rectangle to draw
top_left = max_loc
bottom_right = (top_left[0] + simon_w, top_left[1] + simon_h)

# Draw a rectangle on our screenshot to highlight where we found the needle.
# The line color can be set as an RGB tuple
cv.rectangle(simon_area, top_left, bottom_right, color=(0, 0, 255), thickness=2, lineType=cv.LINE_4)

# cv.imwrite('result.jpg', simon_area)
cv.imshow('rectangle_on_simon', simon_area)
cv.waitKey()
