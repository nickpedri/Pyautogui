import pyautogui as pag
import time
import os
import json
from randomizers import p, r


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
    previous_position = None
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, 'recordings', filename)
    with open(filepath, 'r') as jsonfile:
        data = json.load(jsonfile)
        for index, action in enumerate(data):
            if action['button'] == 'Key.f10':
                break
            # Perform action
            elif action['type'] == 'KeyDown':
                key = action['button']
                key = key[4:] if key[:4] == 'Key.' else key
                pag.keyDown(key)
            elif action['type'] == 'KeyUp':
                key = action['button']
                key = key[4:] if key[:4] == 'Key.' else key
                pag.keyDown(key)
            elif action['type'] == 'clickDown':
                previous_position = (action['pos'][0], action['pos'][1])
                pag.moveTo(action['pos'][0] + p(), action['pos'][1] + p(), duration=r(0.25, 0.70))
                pag.mouseDown()
            elif action['type'] == 'clickUp':
                print(previous_position)
                if previous_position == (action['pos'][0], action['pos'][1]):
                    pag.mouseUp(action['pos'][0], action['pos'][1])
                # pag.moveTo(action['pos'][0], action['pos'][1], duration=0.25)
                else:
                    pag.moveTo(action['pos'][0], action['pos'][1], duration=r(0.25, 1.00))
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

'''
script_dir = os.path.dirname(__file__)
filepath = os.path.join(script_dir, 'recordings', 'actions_test_01.json')
with open(filepath, 'r') as jsonfile:
    data = json.load(jsonfile)
for action in data:
    print(action['button'])
'''