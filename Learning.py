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


#test_mouse_move()
#press('Up', 1)
#press('right', 1)


# Create a function to generate a random number between a and b
def r(a=0.55, b=0.75):  # Define function and define numbers
    return random.uniform(a, b)  # Return numbers


# Create function to return random integers between a and b
def p(a=-3, b=3):  # Define function and define numbers
    return random.randint(a, b)  # Return integers


def shift_camera_direction(direction='north'):
    pag.FAILSAFE = True  # Turn on failsafe
    pag.moveTo(1725 + p(-5, 5), 52 + p(-5, 5), r())
    time.sleep(r(0.15, 0.80))
    if direction == 'north':
        pag.click()
    if direction == 'east':
        pag.rightClick()
        time.sleep(r(0.10, 0.30))
        pag.move(0, 42 + p(), r())
        time.sleep(r(0.10, 0.30))
        pag.click()
    if direction == 'south':
        pag.rightClick()
        time.sleep(r(0.10, 0.30))
        pag.move(0, 57 + p(), r())
        time.sleep(r(0.10, 0.30))
        pag.click()
    if direction == 'west':
        pag.rightClick()
        time.sleep(r(0.10, 0.30))
        pag.move(0, 72 + p(), r())
        time.sleep(r(0.10, 0.30))
        pag.click()
    time.sleep(r(0.25, 1.5))


countdown(3)

directions = ['north', 'east', 'south', 'west']
for d in directions:
    shift_camera_direction(d)

