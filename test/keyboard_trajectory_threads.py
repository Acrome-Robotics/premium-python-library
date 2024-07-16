import threading
from pynput import keyboard
import time
from SMD_blue_test_library.blue import *

# Precise sleep function
def precise_sleep(duration):
    start = time.perf_counter()
    while (time.perf_counter() - start) < duration:
        pass

# Initialize SMD-blue
SERIAL_PORT = "COM6"
m = Master(SERIAL_PORT)
m.attach(Blue(0))

# Initial values
position = 0
velocity = 0
acceleration = 1000
interval = 1  # Update interval in milliseconds

# Keyboard press handling function
def on_press(key):
    global velocity
    try:
        if key.char == 'd':  # Right key (d)
            velocity += acceleration
        elif key.char == 'a':  # Left key (a)
            velocity -= acceleration
    except AttributeError:

# Function to update serial communication
def update_serial():
    global position, velocity, start_time

    while True:
        precise_sleep(0.002)
        current_time = time.perf_counter() - start_time
        position += velocity * (interval / 1000)  # Convert time to milliseconds

        # Send position via serial port
        m.set_variables(0, [[Index.GoalPosition, int(position)]])
        print(position)

# Start keyboard listener thread
def start_keyboard_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

# Start time tracking
start_time = time.perf_counter()

# Create and start threads
keyboard_thread = threading.Thread(target=start_keyboard_listener)
update_thread = threading.Thread(target=update_serial)

keyboard_thread.start()
update_thread.start()

keyboard_thread.join()
update_thread.join()