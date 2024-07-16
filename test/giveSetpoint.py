import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pynput import keyboard
import time
from SMD_blue_test_library.blue import *

def precise_sleep(duration):
    start = time.perf_counter()
    while (time.perf_counter() - start) < duration:
        pass


# init smd-blue
SERIAL_PORT = "COM6"
m = Master(SERIAL_PORT)
m.attach(Blue(0))




while True:
    user_input = input("Enter an integer to send via serial (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    try:
        value = int(user_input)
        m.set_variables(0, [[Index.GoalPosition, int(value)]])
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Exited the loop.")