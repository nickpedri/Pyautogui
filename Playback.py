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
                pag.moveTo(action['pos'][0], action['pos'][1], duration=0.25)
                pag.mouseDown(action['pos'][0], action['pos'][1])
            elif action['type'] == 'clickUp':
                if pag.position() == (action['pos'][0], action['pos'][1]):
                    pag.mouseUp(action['pos'][0], action['pos'][1])
                # pag.moveTo(action['pos'][0], action['pos'][1], duration=0.25)
                else:
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

'''
script_dir = os.path.dirname(__file__)
filepath = os.path.join(script_dir, 'recordings', 'actions_test_01.json')
with open(filepath, 'r') as jsonfile:
    data = json.load(jsonfile)
for action in data:
    print(action['button'])
'''