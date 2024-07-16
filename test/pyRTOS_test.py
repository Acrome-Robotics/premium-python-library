import pyRTOS
import serial
import time

# Seri portu aç
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Setpoint gönderme görevini tanımla
def send_setpoint_task(self):s
    while True:
        # Setpoint verisini oluştur
        setpoint = "SP:100\n"  # Örnek setpoint verisi
        
        # Setpoint verisini seri port üzerinden gönder
        ser.write(setpoint.encode())
        
        # 10 ms bekle
        yield [pyRTOS.timeout(10)]

# Görevleri tanımla
task1 = pyRTOS.Task(send_setpoint_task)

# RTOS'u başlat
pyRTOS.add_task(task1)
pyRTOS.start()
