import farm_functions as ff
import functions as f
from herb_farming import herb_run as hr
from berry import berry_run as br
from cactus import cactus as c
from bird_famring import birdhouses as b
from coconut import coconut as nut

import datetime
import time
import os
import json


SCHEDULE_FILE = "farm_schedule.json"

INTERVALS = {"berry":     80 * 60,
             "herb":      80 * 60,
             "flower":    20 * 60,
             "cactus":    75 * 60,
             "birdhouse": 50 * 60,
             "coconut":   4 * 3600}


def create_new_schedule():
    now = time.time()
    fresh_schedule = {"berry": now, "herb": now, "flower": now, "cactus": now, "birdhouse": now, "coconut": now}
    return fresh_schedule


def save_schedule(schedule):
    with open(SCHEDULE_FILE, "w") as file:
        json.dump(schedule, file, indent=4)


def load_schedule():
    # creates fresh schedule if none exists
    if not os.path.exists(SCHEDULE_FILE):
        return create_new_schedule()
    # Tries to load existing file
    try:
        with open(SCHEDULE_FILE, "r") as file:
            return json.load(file)
    # Creates new schedule if it cannot open existing one
    except (json.JSONDecodeError, OSError):
        print("Could not load schedule. Starting fresh.")
        return create_new_schedule()


def record_run(schedule, farm_name):
    schedule[farm_name] = time.time() + INTERVALS[farm_name]
    save_schedule(schedule)


##--## FARM MANAGER ##--## FARM MANAGER ##--## FARM MANAGER ##--## FARM MANAGER ##--## FARM MANAGER

def farm_master_manager_coordinator(run_time=12):

    start_time = time.time()
    print(f'Starting farm run manager at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}!')
    print()

    # Load in due times
    due_times = load_schedule()

    # Create master key for loop logic
    KEY = {"herb":      {"due": due_times["herb"],      "function": hr.herb_run,     "count": 0,  "items": 'advanced'},
           "flower":    {"due": due_times["flower"],    "function": hr.flower_run,   "count": 0,  "items": 'advanced'},
           "cactus":    {"due": due_times["cactus"],    "function": c.cactus_run,    "count": 0,  "items": 'basic'},
           "berry":     {"due": due_times["berry"],     "function": br.berry_run,    "count": 0,  "items": 'basic'},
           "birdhouse": {"due": due_times["birdhouse"], "function": b.bird_run,      "count": 0,  "items": 'birdhouse'},
           "coconut":   {"due": due_times["coconut"],   "function": nut.coconut_run, "count": 0,  "items": 'coconut'}}
    current_inv = None

    f.log_in()
    ff.set_up()
    ff.open_bank()
    current_inv = ff.gear_up(gear=True)
    # Run while loop for x amount of time
    while time.time() - start_time < run_time * 3600:
        # Update ran-check every loop
        something_ran = False

        herb_due = time.time() >= KEY["herb"]["due"]
        flower_due = time.time() >= KEY["flower"]["due"]

        ## HANDLING SPECIAL FLOWER HERB CASE ##
        if herb_due and flower_due:
            print(f"Starting herb/flower run at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            off = f.logged_off()
            f.log_in()
            if off:
                ff.set_up()

            hr.herb_flower_run(current_items=current_inv)
            current_inv = 'advanced'
            something_ran = True
            print(f"Finished herb/flower run at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print()
            for farm_name in ["herb", "flower"]:
                KEY[farm_name]["count"] += 1
                record_run(due_times, farm_name)
                KEY[farm_name]["due"] = due_times[farm_name]

        ## HANDLE NORMAL EVENTS
        for farm_name, farm_data in KEY.items():
            if farm_name in ["herb", "flower"] and herb_due and flower_due:
                continue
            if time.time() >= farm_data["due"]:
                print(f"Starting {farm_name} run at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

                off = f.logged_off()
                f.log_in()
                if off:
                    ff.set_up()
                farm_data["function"](current_items=current_inv)
                current_inv = farm_data['items']
                something_ran = True
                print(f"Finished {farm_name} run at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print()
                farm_data["count"] += 1
                record_run(due_times, farm_name)
                farm_data["due"] = due_times[farm_name]

        if something_ran:
            upcoming = sorted(KEY.items(), key=lambda item: item[1]["due"])

            print("Upcoming farm runs:")
            for farm_name, farm_data in upcoming:
                timestamp = farm_data["due"]
                formatted_time = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
                print(f"Next {farm_name} run at {formatted_time}")

            print()

            for farm_name, farm_data in KEY.items():
                print(f"Total {farm_name} runs: {farm_data['count']}")

            print()
        else:
            if not(f.logged_off()):
                f.log_out()

        time.sleep(60)


farm_master_manager_coordinator(24)
