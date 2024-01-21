import pyautogui as pag
from time import sleep
import os
import json


def initialize_pag():
    pag.FAILSAFE = True  # Turn on failsafe
    print('Pyautogui failsafe enabled!')