import pyautogui as pag
import time
import os
import json


def initialize_pag():
    pag.FAILSAFE = True  # Turn on failsafe
    print('Pyautogui failsafe enabled!')


def countdown(seconds=10):
    print(f'Starting', end='')
    for s in range(1, seconds + 1):
        print('.', end='')
        time.sleep(1)
    print(' now!')


def play_actions(filename):
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, 'recordings', filename)
    with open(filepath, 'r') as jsonfile:
        data = json.load(jsonfile)
        for index, action in enumerate(data):
            if action['button'] == 'Key.esc':
                break
            # Perform action
            if action['type'] == 'KeyDown':
                pag.KeyDown(action['button'])
            elif action['type'] == 'KeyUp':
                pag.KeyUp(action['button'])
            elif action['type'] == 'clickDown':
                pag.moveTo(action['pos'][0], action['pos'][1], duration=0.25)
                pag.mouseDown(action['pos'][0], action['pos'][1])
            elif action['type'] == 'clickUp':
                pag.moveTo(action['pos'][0], action['pos'][1], duration=0.25)
                pag.mouseUp(action['pos'][0], action['pos'][1])

            # Sleep until next action
            try:
                next_action = data[index + 1]
            except IndexError:
                break
            elapsed_time = next_action['time'] - action['time']
            if elapsed_time >= 0:
                time.sleep(elapsed_time)
            else:
                raise Exception('Unexpected action ordering.')


def main():
    countdown(3)
    initialize_pag()
    play_actions('actions_test_01.json')


main()


