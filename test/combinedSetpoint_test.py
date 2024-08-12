from premium.blue import *
from premium.osModules import *

import time

# init smd-blue
BATCH_ID = 0xFF
SERIAL_PORT = USB_serial_port()

print(SERIAL_PORT)

m = Master(SERIAL_PORT, 115200)
m.attach(Blue(BATCH_ID))
m.attach(Blue(1))

pos = 0
i = 0

m.set_variables(1, [[Index.TorqueEn, 1]])
while True:
    pos = int(input("Enter position: "))
    time_traj = 10
    m.set_variable_combined([Index.GoalPosition, Index.Trajectory_time],[[123,pos,123],[1,time_traj,5]], 3)
    time.sleep(0.005)  
    
    values = m.get_variables(1, [Index.TestValue_i_1, Index.TestValue_i_2, Index.TestValue_i_3])
    current_pos = values[0]

    while abs(current_pos - pos) > 10:
        values = m.get_variables(1, [Index.TestValue_i_1, Index.TestValue_i_2, Index.TestValue_i_3])
        current_pos = values[0]
        print(values)
        pass
