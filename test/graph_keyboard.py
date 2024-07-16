import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pynput import keyboard

# Başlangıç değerleri
position = 0
velocity = 0
acceleration = 1

# Verileri saklamak için listeler
positions = [position]
velocities = [velocity]
times = [0]
time = 0

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

# Grafik güncelleme işlevi
def update(frame):
    global position, velocity, time
    
    time += 1
    position += velocity
    
    positions.append(position)
    velocities.append(velocity)
    times.append(time)
    
    ax1.clear()
    ax2.clear()
    
    ax1.plot(times, positions, label='Position')
    ax1.set_ylabel('Position')
    ax1.set_xlabel('Time')
    ax1.legend()
    
    ax2.plot(times, velocities, label='Velocity', color='r')
    ax2.set_ylabel('Velocity')
    ax2.set_xlabel('Time')
    ax2.legend()

# Grafik ayarları
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ani = animation.FuncAnimation(fig, update, interval=100)

plt.tight_layout()
plt.show()

# Dinleyiciyi durdurmak için programı bitirmek gerekebilir
listener.stop()
