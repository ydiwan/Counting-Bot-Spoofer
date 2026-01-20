#!/usr/bin/env python3
"""
type_numbers_infinite.py

Type numbers starting at `start_number`, increment by `step` each time,
press Enter, wait `between_entries` seconds, and repeat forever until you stop it.

Usage:
    python type_numbers_infinite.py

Make sure to click the target text box during the initial_wait countdown so it is focused.
Move your mouse to the upper-left corner to abort (pyautogui failsafe), or Ctrl+C in the terminal.
"""

import time
import pyautogui

# -------- USER CONFIG ----------
start_number = 1       # first number to type
step = 2               # how much to increase each iteration
initial_wait = 5.0     # seconds to give you time to click the target box
between_entries = 1.0  # seconds to wait AFTER pressing Enter before next number
typing_interval = 0.01 # delay between keystrokes (numbers are short so small is fine)
# --------------------------------

pyautogui.FAILSAFE = True  # move mouse to top-left to abort immediately

def main():
    print("=== type_numbers_infinite.py ===")
    print(f"You have {initial_wait} seconds to click the text box that should receive input...")
    print("Move the mouse to the upper-left corner to abort, or press Ctrl+C in terminal.")
    time.sleep(initial_wait)

    n = start_number
    try:
        iteration = 0
        while True:
            iteration += 1
            text = str(n)
            print(f"[{iteration}] Typing: {text}")
            # For a small string like a number, typing is reliable:
            pyautogui.typewrite(text, interval=typing_interval)
            pyautogui.press("enter")
            # Increment for next loop
            n += step
            time.sleep(between_entries)
    except KeyboardInterrupt:
        print("\nStopped by user (KeyboardInterrupt).")
    except pyautogui.FailSafeException:
        print("\nAborted via mouse to top-left (pyautogui FAILSAFE).")
    finally:
        print("Goodbye.")

if __name__ == "__main__":
    main()
