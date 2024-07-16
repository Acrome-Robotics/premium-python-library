import serial
import time
from numba import jit

# Seri portu aç
ser = serial.Serial('/dev/ttyUSB0', 9600)

@jit(nopython=True)
def send_setpoint():
    # 10 ms'de bir setpoint gönder
    while True:
        start_time = time.time()
        
        # Setpoint verisini oluştur
        setpoint = "SP:100\n"  # Örnek setpoint verisi
        
        # Setpoint verisini seri port üzerinden gönder
        ser.write(setpoint.encode())
        
        # 10 ms bekle
        end_time = time.time()
        time_to_wait = 0.01 - (end_time - start_time)
        if time_to_wait > 0:
            time.sleep(time_to_wait)

# Setpoint gönderme fonksiyonunu çalıştır
send_setpoint()
