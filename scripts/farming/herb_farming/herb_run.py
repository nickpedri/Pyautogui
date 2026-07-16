import functions as f
import pyautogui as pag
import time
import farm_functions as ff


def set_up():
    f.shift_camera_direction('north')
    pag.moveTo(1140 + f.p(0, 100), 500 + f.p(0, 100), f.r(0, 1))
    pag.scroll(-10000)
    pag.press('f2')


def open_bank(bank=None):
    if bank is None:
        bank = (944, 561)
    if f.is_bank_open():
        return
    f.move_click(*bank)
    pin = ['7', '3', '5', '7']
    time.sleep(f.r(1, 1.5))
    if f.is_bank_open():
        return None
    for n in pin:
        pag.press(n)
        time.sleep(f.r(1, 1.5))
    f.wait_until(f.is_bank_open)


def navigate_to_tab():
    f.move_click(640, 103)
    pag.moveTo(600 + f.p(5), 247 + f.p(5), f.r(0, 0.5))
    for i in range(5):
        pag.scroll(200)
        time.sleep(0.01)
    pag.click()


def tp_ardy():
    f.shift_click(1745, 766, wait=f.r(6, 7))
    ff.reposition_to_MMM()


def tp_catherby():
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(959, 356, wait_duration=f.r(4, 5))
    ff.reposition_to_MMM()
    f.move_click(996, 349,  wait_duration=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(973, 378,  wait_duration=f.r(3, 4))
    f.wait_until(lambda: f.on_tile('yellow'))


def tp_civ():
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.shift_click(959, 356, wait=f.r(5, 6))
    pag.press('6')
    time.sleep(3)
    ff.reposition_to_MMM()
    f.move_click(1300, 419,  wait_duration=f.r(5, 6))
    f.move_click(860, 460,  wait_duration=f.r(5, 6))
    f.move_click(838, 60,  wait_duration=f.r(8, 10))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(876, 121,  wait_duration=f.r(5, 6))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(1107, 559,  wait_duration=f.r(1, 2))
    f.wait_until(lambda: f.on_tile('green'))


def tp_fally():
    f.move_click(1800, 721)  # click gear tab
    f.shift_click(1822, 920, wait=f.r(5, 6))  # shift click tp
    pag.press('f2')
    ff.reposition_to_MMM()
    f.move_click(945, 316, wait_duration=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('red'))


def tp_fg():
    f.move_click(1800, 721)
    f.shift_click(1726, 802, wait=f.r(5, 6))
    pag.press('f2')
    ff.reposition_to_MMM()


def tp_harmony():
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.shift_click(959, 356, wait=f.r(5, 6))
    pag.press('3')
    time.sleep(3)
    ff.reposition_to_MMM()
    f.move_click(942, 994, wait_duration=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(651, 962, wait_duration=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))


def tp_hosidius():
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(889, 258, wait_duration=f.r(8, 10))
    ff.reposition_to_MMM()
    f.move_click(566, 961, wait_duration=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(775, 625, wait_duration=f.r(2, 3))
    f.wait_until(lambda: f.on_tile('green'))


def tp_mory():
    f.click_slot(4, wait=f.r(7, 8))
    ff.reposition_to_MMM()
    f.move_click(323, 378, wait_duration=f.r(8, 9))
    f.wait_until(lambda: f.on_tile('red'))
    f.move_click(97, 522, wait_duration=f.r(8, 9))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.move_click(750, 633, wait_duration=f.r(3, 4))
    f.wait_until(lambda: f.on_tile('green'))


def tp_troll():
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.shift_click(959, 356, wait=f.r(5, 6))
    pag.press('4')
    time.sleep(3)
    ff.reposition_to_MMM()


def tp_weiss():
    f.click_slot(1, wait=f.r(4, 5))
    f.wait_until(lambda: f.on_tile('yellow'))
    f.shift_click(959, 356, wait=f.r(5, 6))
    pag.press('5')
    time.sleep(3)
    ff.reposition_to_MMM()


def wait_for_sack(herb, delay=4):
    while True:
        option = f.identify_options({'pngs/pick.png': 'pass', 'pngs/inspect.png': 'continue',
                                     'pngs/dead_herb.png': 'clear'},
                                    xy=herb, search_window=(75, 15, 150, 60))
        # pag.move(f.p(-50, 50), f.p(-105, -75), f.r(0.1, 0.2))
        # print(option)
        if option != 'pass':
            break
        time.sleep(delay)

    if option == 'clear':
        f.move_click(*herb)
        time.sleep(delay)


click_map = {
    'ardy':  {'MMM': (1054, 504), 'f_tile': (989, 505), 'f_h': (1118, 505), 'm_h': (1180, 500), 'h_tile': (989, 505)},
    'cat':   {'MMM': (1052, 511), 'f_tile': (990, 505), 'f_h': (1118, 505), 'm_h': (1171, 508), 'h_tile': (989, 505)},
    'civ':   {'MMM': (1050, 450), 'f_tile': (990, 505), 'f_h': (856, 632),  'm_h': (932, 560),  'h_tile': (927, 564)},
    'fally': {'MMM': (980, 395),  'f_tile': (960, 477), 'f_h': (1070, 383), 'm_h': (1088, 312), 'h_tile': (957, 477)},
    'fg':    {'MMM': (1323, 590), 'f_tile': (962, 560), 'f_h': (248, 548),  'm_h': (600, 562),  'h_tile': (927, 564)},
    'har':   {'MMM': None,        'f_tile': None,       'f_h': None,        'm_h': (895, 740),  'h_tile': (927, 564)},
    'hos':   {'MMM': (835, 449),  'f_tile': (897, 505), 'f_h': (1030, 629), 'm_h': (960, 561),  'h_tile': (962, 561)},
    'mory':  {'MMM': (860, 625),  'f_tile': (927, 562), 'f_h': (1047, 455), 'm_h': (990, 502),  'h_tile': (990, 502)},
    'troll': {'MMM': None,        'f_tile': None,       'f_h': None,        'm_h': (697, 522),  'h_tile': (900, 505)},
    'weiss': {'MMM': None,        'f_tile': None,       'f_h': None,        'm_h': (1070, 700), 'h_tile': (992, 536)}}


def farm(location='ardy', flower=True, herb=True):
    global click_map

    patch = click_map[location]
    if flower:
        f.move_click(*patch['MMM'], wait_duration=f.r(1, 2))  # harvest plant from mm tile
        f.wait_until(lambda: f.on_tile('blue'))
        time.sleep(f.r(3, 4))
        f.click_slot(5)  # select compost
        f.move_click(*patch['f_tile'], wait_duration=f.r(4, 5))  # compost
        f.click_slot(9)
        f.move_click(*patch['f_tile'], wait_duration=f.r(3, 4))  # plant seed
    if herb:
        if flower:
            f.move_click(*patch['f_h'], wait_duration=f.r(2, 3))
        else:
            f.move_click(*patch['m_h'], wait_duration=f.r(2, 3))
        f.wait_until(lambda: f.on_tile('green'))
        wait_for_sack(patch['h_tile'])
        f.click_slot(5)  # select compost
        f.move_click(*patch['h_tile'], wait_duration=f.r(4, 5))  # compost
        f.click_slot(10)
        f.move_click(*patch['h_tile'], wait_duration=f.r(3, 4))


patches = [['ardy',  tp_ardy, True, True],
           ['cat',   tp_catherby, True, True],
           ['civ',   tp_civ, True, True],
           ['fally', tp_fally, True, True],
           ['fg',    tp_fg, True, True],
           ['har',   tp_harmony, False, True],
           ['hos',   tp_hosidius, True, True],
           ['mory',  tp_mory, True, True],
           ['troll', tp_troll, False, True],
           ['weiss', tp_weiss, False, True]]


def patch_farming(location_details, flower_only=False, herb_only=False):
    location = location_details[0]
    tp = location_details[1]
    flower_patch = location_details[2]
    if herb_only:
        flower_patch = False
    herb_patch = location_details[3]
    if flower_only:
        herb_patch = False

    if flower_patch is True or herb_patch is True:
        tp()
        farm(location, flower_patch, herb_patch)
        ff.bank_items()


def herb_flower_run(current_items):
    open_bank()
    ff.item_up(current_items=current_items, items_to_equip='advanced')
    for p in patches:
        # print(f'Starting herb/flower run {n} at {datetime.datetime.now()}!')
        patch_farming(p)
        # print(f'Herb/flower run {n} finished at {datetime.datetime.now()}!')


def flower_run(current_items):
    open_bank()
    ff.item_up(current_items=current_items, items_to_equip='advanced')
    for p in patches:
        # print(f'Starting flower run {n} at {datetime.datetime.now()}!')
        patch_farming(p, flower_only=True)
        # print(f'Flower run {n} finished at {datetime.datetime.now()}!')


def herb_run(current_items):
    open_bank()
    ff.item_up(current_items=current_items, items_to_equip='advanced')
    for p in patches:
        # print(f'Starting flower run {n} at {datetime.datetime.now()}!')
        patch_farming(p, herb_only=True)
        # print(f'Flower run {n} finished at {datetime.datetime.now()}!')
