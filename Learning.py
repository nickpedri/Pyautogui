import pyautogui as pag  # Use pag to control mouse
import random  # Use random to add randomness to movements
import time  # Use time to time mouse movements


# Create a simple countdown loop
def countdown(seconds=10):
    print(f'Starting', end='')
    for s in range(1, seconds + 1):
        print('.', end='')
        time.sleep(1)
    print(' now!')


# Create loop that will repeat 10 times to test simple mouse movement
def test_mouse_move():
    for n in range(1, 6):
        pag.FAILSAFE = True  # Turn on failsafe
        rx = random.randint(-10, 10)  # Create x variable randomness
        ry = random.randint(-10, 10)  # Create y variable randomness
        print(f' {n}.)   {rx}, {ry}')  # Print x and y randomness
        pag.moveTo(1920 / 2 + rx, 540 + ry, .5)  # Move mouse to location with random increments
        time.sleep(0.50)  # Wait a half second between moves


# Create function to press keys for a specific amount of time
def press(key, how_long):
    pag.keyDown(key)  # Press key down
    time.sleep(how_long)  # Time to wait
    pag.keyUp(key)  # Release key


countdown(1)
#test_mouse_move()
#press('Up', 1)
#press('right', 1)


def r(a=0.55, b=0.75):
    return random.uniform(a, b)


def p(a, b):
    return random.randint(a, b)

def shift_camera_direction(direction='north'):
    if direction is 'north':
        pag.click(1725)
    pag.rightClick(1725, 52)
    time.sleep(r())
    print(r())
    pag.move(0, 15, r())
    print(r())
    pag.move(0, 15, r())
    print(r())
    pag.move(0, 15, r())
    print(r())


shift_camera_direction()
