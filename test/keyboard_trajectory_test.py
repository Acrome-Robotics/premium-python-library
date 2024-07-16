from pynput import keyboard
import time
from SMD_blue_test_library.blue import *

import time

def precise_sleep(duration):
    start = time.perf_counter()
    while (time.perf_counter() - start) < duration:
        pass


# init smd-blue
SERIAL_PORT = "COM6"
m = Master(SERIAL_PORT)
m.attach(Blue(0))

# Başlangıç değerleri
position = 0
velocity = 0
acceleration = 1000  # Daha küçük adımlarla hız değişimi
interval = 1  # Güncelleme aralığını 10 milisaniyeye düşürdük

# Zaman takibi
start_time = time.perf_counter()

# Klavye tuşlarına basma işlemlerini yakalamak için işlevler
def on_press(key):
    global velocity
    try:
        if key.char == 'd':  # Sağ tuşu (d)
            velocity += acceleration
        elif key.char == 'a':  # Sol tuşu (a)
            velocity -= acceleration
    except AttributeError:
        pass

# Klavye dinleyicisini başlat
listener = keyboard.Listener(on_press=on_press)
listener.start()

def update_serial():
    global position, velocity, start_time
    
    current_time = time.perf_counter() - start_time
    position += velocity * (interval / 1000)  # Zamanı milisaniyeye çeviriyoruz
    
    # Pozisyonu seri port üzerinden gönder
    m.set_variables(0, [[Index.GoalPosition, int(position)]])


# Sürekli güncelleme döngüsü
try:
    while True:
        print(position)
        precise_sleep(0.001)
        update_serial()

except KeyboardInterrupt:
    listener.stop()
