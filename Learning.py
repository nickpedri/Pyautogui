import pyautogui as pag  # Use pag to control mouse
import random  # Use random to add randomness to movements
import time  # Use time to time mouse movements

# Create loop that will repeat 10 times to test simple mouse movement
for n in range(1, 11):
    rx = random.randint(-5, 5)
    ry = random.randint(-5, 5)
    print(f' {n}.)   {rx}, {ry}')
    pag.moveTo(900 + rx, 900 + ry)
    time.sleep(.25)
