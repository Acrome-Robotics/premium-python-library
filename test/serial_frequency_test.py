import time
from SMD_blue_test_library.blue import *


def current_milli_time():
    return round(time.time() * 1000)
 

SERIAL_PORT = "COM6"

m = Master(SERIAL_PORT)
m.attach(Blue(0))

times = []

for i in range(0,10000):
    current = current_milli_time()
    m.set_variables(0,[[Index.GoalSpeed, i]])
    times.append(current_milli_time() - current)


print(times)

'''
c= 0
for i in times:
    print(i)
    c+=1
    if c > 1000:
        break
'''

