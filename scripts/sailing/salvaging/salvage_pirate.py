import time
import functions as f
import pyautogui as pag
import os


project_dir = os.path.dirname(__file__)


def create_grid(tl, br, rows, columns):
    grid = {}
    x = int((br[0] - tl[0]) / columns)
    y = int((br[1] - tl[1]) / rows)
    count = 0
    for row in range(tl[1], br[1], y):
        for column in range(tl[0], br[0], x):
            count += 1
            grid[f'Slot {count}'] = int(round(column + y/2)), int(round(row + x/2))
    return grid


inv = create_grid(tl=(1676, 741), br=(1860, 1000), rows=7, columns=4)


def display_dict(dic):
    for entry in dic:
        print(entry, ':', dic[entry])


def test_grid(grid):
    for slot in grid:
        a, b = grid[slot][0], grid[slot][1]
        pag.moveTo(a, b)
        time.sleep(0.20)


# display_dict(inv)
# test_grid(inv)

for n in range(1, 150):
    f.play_actions('dump_trash.json', project_dir)
    time.sleep(f.r(20, 30))
    f.play_actions('clean_salvage.json', project_dir)
    time.sleep(f.r(10, 15))


