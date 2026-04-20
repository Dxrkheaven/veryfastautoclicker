# autoclicker.py

import pyautogui as click
import keyboard
import time

click.PAUSE = 0  # more stable than 0

clicking = False
delay = 0.001       # safer than 0.001
click_type = "left"  # left or right


def set_delay(new_delay):
    global delay
    try:
        delay = float(new_delay)
        print("Delay:", delay)
    except:
        print("Invalid delay input")


def set_click_type(new_type):
    global click_type
    click_type = new_type
    print("Click Type:", click_type)


def toggle():
    global clicking
    clicking = not clicking
    print("Clicking:", clicking)


def run():
    keyboard.add_hotkey("F6", toggle)

    while True:
        if clicking:
            click.click(button=click_type)
            time.sleep(delay)
        else:
            # prevents CPU from being maxed when idle
            time.sleep(0.05)


if __name__ == "__main__":
    run()