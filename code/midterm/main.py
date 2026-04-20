from lib.sensor_module import RoomSensor

sensors = [
    RoomSensor("Kitchen", 31, 72, 180),
    RoomSensor("Bedroom", 24, 50, 300),
    RoomSensor("Balcony", 18, 65, 150)
]

comfortable= 0
normal = 0
warning= 0

for sensor in sensors:
    sensor.show_info()
    
    comfort = sensor.comfort_level()
    light = sensor.light_status()
    
    print("Comfort Level:", comfort)
    print("Light Status:", light)
    print() 
    
    
    if comfort == "Comfortable":
        comfortable += 1
    elif comfort == "Warning":
        warning += 1
    else:
        normal+= 1


print("Comfortable:", comfortable)
print("Normal:", normal)
print("Warning:", warning)