from premium.blue import *
from premium.blue.osModules import *

import time

# init smd-blue
BATCH_ID = 0xFF
SERIAL_PORT = USB_serial_port()

print(SERIAL_PORT)

m = Master(SERIAL_PORT)
m.attach(Blue(BATCH_ID))


i = 0
while True:
    m.set_variables_combined(Index.GoalPosition, [12,i,200,300], 4)
    i += 1
    print(i)
    time.sleep(0.01)





