from premium.blue import *
from premium.osModules import *

import time

# init smd-blue
BATCH_ID = 0xFF
SERIAL_PORT = USB_serial_port()

print(SERIAL_PORT)

m = Master(SERIAL_PORT, 115200)
m.attach(Blue(BATCH_ID))

pos = 0
i = 0

while True:
    m.set_variable_combined([Index.GoalPosition, Index.Trajectory_time, Index.Trajectory_accel],[[123,123,4],[1,2,5],[50,223,25]], 3)
    time.sleep(1)
    m.set_variable_combined([Index.GoalPosition, Index.Trajectory_time, Index.Trajectory_accel],[[123,2500,4],[1,19,5],[50,11111,25]], 3)
    time.sleep(1)
    i = 0
