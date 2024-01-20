#import pyautogui as pag  # Use pag to control mouse
#import random  # Use random to add randomness to movements
import time  # Use time to time mouse movements


# Create a simple countdown loop
def countdown(seconds=10):
    print(f'Starting', end='')
    for s in range(1, seconds + 1):
        print('.', end='')
        time.sleep(1)
    print(' now!')


# Create loop that will repeat 10 times to test simple mouse movement
#def test_mouse_move():
    #print('function called')
    #for n in range(1, 11):
        #pag.FAILSAFE = True  # Turn on failsafe
        #rx = random.randint(-10, 10)  # Create x variable randomness
        #ry = random.randint(-10, 10)  # Create y variable randomness
        #print(f' {n}.)   {rx}, {ry}')  # Print x and y randomness
        #pag.moveTo(1920 / 2 + rx, 540 + ry)  # Move mouse to location with random increments
        #time.sleep(0.50)  # Wait a half second between moves

def test_loop():
    for n in range(1, 4):
        print(n)


countdown(3)
test_loop()
# test_mouse_move()
