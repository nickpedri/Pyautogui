import time
import functions as f
import pyautogui as pag


def afk(duration=60, xy=(1767, 718), frequency=60):
    ratio = 60/frequency  # gives you reps per minute
    loops = round(duration * ratio)
    print(loops)

    for n in range(1, loops + 1):
        f.move_click(*xy)
        time.sleep(f.r(frequency-5, frequency+5))


def afk_but_better(duration=30, xy=[(943, 545)], frequency=[60]):
    """
    Takes in duration in minutes for script, and also two lists.One of the xy coordinates,
    and frequency of clicks

    duration: minutes the script should run for
    xy: list of tuples containing x and y mouse coordinates
    frequency: list of integers containing seconds to wait between each click
    """

    # Check that both lists are equal length for proper pairing.
    if len(xy) != len(frequency):
        raise ValueError("xy and frequency must be the same length")

    # Activate pag failsafe
    pag.FAILSAFE = True

    # zip the two lists together
    tasks = list(zip(xy, frequency))

    # Create start and end time for script
    start = time.monotonic()
    end_time = start + duration * 60

    # Track when xy coordinates should be clicked next
    next_click_times = []
    for (pos, interval) in tasks:
        next_click_times.append(start + interval)

    # Main loop

    while time.monotonic() < end_time:
        now = time.monotonic()

        # Check each task and click if it's due
        for i, ((x, y), interval) in enumerate(tasks):
            if now >= next_click_times[i]:
                f.move_click(x, y)

                # Schedule that task's next click
                next_click_times[i] += interval

        # IMPORTANT ---- This will slow down the script, so it doesn't go pedal to the metal
        time.sleep(0.1)


afk_but_better(15, [(947, 471), (1788, 771)], [15, 160])



