import time
import digit_extractor as de
import functions as f
import pyautogui as pag


bank = (950, 500)
vial = (742, 471)

# herbs dictionary contains name of herb, xy of bank location, and quantity
herbs = {'guam':         [(889, 142), 61],
         'marrentil':    [(985, 142), 10],
         'tarromin':     [(889, 178), 3948],
         'harralander':  [(985, 177), 2557],
         'ranarr':       [(889, 216), 1534],
         'toadflax':     [(985, 216), 502],
         'irit':         [(889, 250), 3834],
         'avantoe':      [(985, 250), 2452],
         'kwuarm':       [(889, 286), 1322],
         'snapdragon':   [(985, 286), 550],
         'cadantine':    [(889, 321), 1578],
         'lantadyme':    [(985, 321), 1453],
         'dwarf_weed':   [(889, 359), 2068]}
         #'torstol':      [(985, 359), 605]}


def make_unf_potions(herb):
    f.move_click(*herb, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
    f.move_click(*vial, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.45))
    pag.press('esc')
    time.sleep(f.r(0.2, 0.3))
    inv = f.create_inv(28)
    f.move_click(*inv['Slot 14'], wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.3, 0.5))
    f.move_click(*inv['Slot 15'], wait_duration=f.r(1, 1.5), move_duration=f.r(0.1, 0.2))
    pag.press('space')
    f.wait_until(lambda: f.slot_empty(28))
    f.move_click(*bank, wait_duration=f.r(1, 1.5))
    f.move_click(1004, 825, wait_duration=f.r(0.05, 0.1), move_duration=f.r(0.2, 0.35))


def parse_herbs(test=False):
    for name, data in zip(herbs.keys(), herbs.values()):
        xy = data[0]
        quantity = data[1]
        if test:
            print(f'{quantity} {name}s')
            pag.moveTo(*xy)
        return name, xy, quantity


def create_herbs_grid():
    t = f.create_inv_grid(tl=(854, 118), br=(1004, 370), rows=7, columns=3)  # creates item list location
    t = {k: v for i, (k, v) in enumerate(t.items()) if i % 3 != 1}  # cuts it down to 14 slots
    # rename slots to herbs
    new_herbs = {}
    for slot, h in zip(t.values(), herbs.keys()):
        new_herbs[h] = slot
    return new_herbs


def herb_amounts():
    grid = create_herbs_grid()
    quantities = {}
    for herb in herbs.keys():
        h = grid[herb]
        img = f.take_screenshot(area=(h[0]-5, h[1]-20, 35, 13), save_img=False, img_name='herb.png')
        quantity = de.read_digits(img)
        quantities[herb] = quantity
    # print(quantities)
    return quantities


def main():
    # extract data from herbs dictionary
    quantities = herb_amounts()
    for name, data in zip(herbs.keys(), herbs.values()):
        xy = data[0]
        quantity = quantities[name]
        print(f'{quantity} {name}s')

        if quantity > 200:
            loops = round((quantity - 50)/14)
            for n in range(1, loops + 1):
                make_unf_potions(xy)

        else:
            print(f'Skipping {name}')


main()
