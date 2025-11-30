import time
import functions as f
import pyautogui as pag
import os


project_dir = os.path.dirname(__file__)

north = (1807, 41)
east = (1867, 106)
south = (1806, 169)
west = (1744, 105)

hosidius_orange = (144, 94, 27)


def find_courier_route():
    pag.moveTo(100, 100)
    options = ((616, 395), (729, 395), (837, 395), (956, 395), (616, 550), (729, 550), (837, 550), (956, 550))
    hosidius_delivery = list()
    for opt in options:
        if f.check_pixel_color_in_area((*opt, 70, 1), hosidius_orange):
            hosidius_delivery.append(opt)
    print(f'Courier routes found at {hosidius_delivery[0]} and {hosidius_delivery[1]}.')
    return hosidius_delivery


def reset_ship():  ## reset ship orientation at the port. start from ledger tile
    f.move_right_click(322, 879)
    option = f.find('customize_boat.png', (150, 679, 350, 300))
    f.move_click(option[0], option[1])
    time.sleep(8.5 + f.r())
    f.move_click(945, 301, wait_duration=f.r(3.5, 4.5))
    f.move_click(950, 500, wait_duration=f.r(3.5, 4.5))
    gangplank = f.find('gangplank.png', (1530, 300, 400, 200))
    f.move_click(gangplank[0], gangplank[1])
    time.sleep(15 + f.r(2, 3))
    print('Boat position reset')


def sail_to_hosidius():
    f.move_click(*east, wait_duration=0)
    time.sleep(25)
    f.move_click(*south, move_duration=f.r(0.40, 0.45), wait_duration=0)
    time.sleep(115)
    f.move_click(*west, move_duration=f.r(0.40, 0.45), wait_duration=0)
    time.sleep(73.8)
    f.move_click(*north, move_duration=f.r(0.40, 0.45), wait_duration=0)
    time.sleep(30)
    f.move_click(*east)
    time.sleep(f.r(6, 7))


def sail_to_port_piscarilius():
    f.move_click(*south, wait_duration=0)
    time.sleep(24)
    f.move_click(*east, move_duration=f.r(0.40, 0.45), wait_duration=0)
    time.sleep(74)
    f.move_click(*north, move_duration=f.r(0.40, 0.45), wait_duration=0)
    time.sleep(113)
    f.move_click(*west, move_duration=f.r(0.40, 0.45), wait_duration=0)
    time.sleep(28)
    f.move_click(*north)
    time.sleep(f.r(6, 7))
    f.move_click(*west)
    time.sleep(f.r(6, 7))


def unload_hosidius():
    f.move_click(1002, 518, wait_duration=f.r(3, 4))  ## open storage
    f.move_click(624, 385, wait_duration=f.r(1.5, 2))  ## withdraw crate
    f.move_click(1053, 647, wait_duration=f.r(3.5, 4))  ##  deboard
    f.move_click(917, 351, wait_duration=f.r(7, 8))  ##  deposit crate
    f.move_click(911, 523, wait_duration=f.r(1.5, 2.5))  ## take new crate
    f.move_click(944, 826, wait_duration=f.r(7, 8))  ## reboard
    f.move_click(1033, 536, wait_duration=f.r(3, 4))  ## deposit new crate
    f.move_click(968, 538, wait_duration=f.r(1.5, 2))  ## open cargo
    f.move_click(624, 385, wait_duration=f.r(1.5, 2.5))  ## take new crate
    f.move_click(1053, 647, wait_duration=f.r(3.5, 4))  ##  deboard
    f.move_click(917, 351, wait_duration=f.r(7, 8))  ##  deposit crate
    f.move_click(911, 523, wait_duration=f.r(2.5, 3))  ## take new crate
    for n in range(1, 6):
        pag.press('space')
        time.sleep(f.r(1, 2))
    f.move_click(911, 523, wait_duration=f.r(2, 2.5))  ## take new crate second time to get past dialogue
    f.move_click(944, 826, wait_duration=f.r(7, 8))  ## reboard
    f.move_click(1033, 536, wait_duration=f.r(3, 4))  ## deposit new crate
    f.move_click(820, 543, wait_duration=f.r(4, 5))  ## get back on helm


def complete_trip():
    f.move_click(1043, 413, wait_duration=f.r(6, 7))  #disembark
    f.move_click(700, 478, wait_duration=f.r(4, 5))  #walk to ledger
    reset_ship()
    f.play_actions('port_piscarilius_reset.json', project_dir)
    time.sleep(f.r(9, 11))
    for n in range(1, 6):
        pag.press('space')
        time.sleep(f.r(1, 2))
    f.move_click(1044, 484)
    time.sleep(f.r(3, 4))
    courier_route = find_courier_route()
    f.move_click(*courier_route[0], wait_duration=f.r(1, 2))
    f.move_click(1031, 588, wait_duration=f.r(1, 2))
    f.move_click(*courier_route[1], wait_duration=f.r(1, 2))
    f.move_click(1031, 588, wait_duration=f.r(1, 2))


def main():
    sail_to_hosidius()
    unload_hosidius()
    sail_to_port_piscarilius()
    complete_trip()


sail_to_port_piscarilius()
complete_trip()
