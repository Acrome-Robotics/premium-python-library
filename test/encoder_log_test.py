import keyboard
import json
import time
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
time_traj = 10


m.set_variables(1, [[Index.TorqueEn, 1]])
# Verileri depolamak için bir liste oluşturuyoruz
error_list = []
current_position_list = []
target_list = []
encoder_list = []

# Sürekli olarak veri ekleme işlemi yapan bir fonksiyon
def add_data():
    while True:
        # Burada zaman damgasını veri olarak ekliyoruz, ancak bu veriyi isteğinize göre değiştirebilirsiniz.

        values = m.get_variables(1, [Index.TestValue_i_1, Index.TestValue_i_2, Index.TestValue_i_3, Index.TestValue_i_4])
        current_position_list.append(values[0])
        target_list.append(values[1])
        error_list.append(values[2])
        encoder_list.append(values[3])

        #print(f"Added data: {current_time}")

        # Klavyeden 'q' tuşuna basıldığında döngüyü kırıyoruz
        if keyboard.is_pressed('y'):
            pos = int(input("Enter position: "))
            m.set_variable_combined([Index.GoalPosition, Index.Trajectory_time],[[123,pos,123],[1,time_traj,5]], 3)


        if keyboard.is_pressed('q'):
            break


    save_data_to_json()

# Verileri bir JSON dosyasına kaydeden fonksiyon
def save_data_to_json():
    # JSON formatına uygun olarak verileri bir dictionary içinde topluyoruz
    data = {
        "targets": target_list,
        "errors": error_list,
        "current_poses": current_position_list,
        "encoder": encoder_list
    }

    # Verileri JSON dosyasına kaydediyoruz
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Data saved to data.json")


# Ana işlemi başlatmak için bir fonksiyon
def main():
    print("Press 'q' to stop and save data.")
    add_data()

if __name__ == "__main__":
    main()
