import vex
from vex import *

# Setup
brain = Brain()
left_motor = vex.Motor(vex.Ports.PORT5, vex.GearSetting.RATIO_18_1, False)
right_motor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
inertial = vex.Inertial(vex.Ports.PORT6)

# Calibration
inertial.calibrate()
while inertial.is_calibrating():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("Inertial Sensor is Calibrating")
    wait(50, MSEC)

# Measure position

def data_collector(): # Function for SD card data collection and writing
    brain.timer.clear()

    while True:
        timer = brain.timer.time(MSEC)
            
        roll = inertial.orientation(OrientationType.ROLL, DEGREES)
        pitch = inertial.orientation(OrientationType.PITCH, DEGREES)
        yaw = inertial.orientation(OrientationType.YAW, DEGREES)
       
        line = f"{timer}, {roll}, {pitch}, {yaw}\n"
        brain.sdcard.appendfile("data.csv", bytearray(line, "utf-8"))
        
        wait(0.1, SECONDS)

        if timer >= 30000:
            break

roll = inertial.orientation(OrientationType.ROLL, DEGREES)
pitch = inertial.orientation(OrientationType.PITCH, DEGREES)
yaw = inertial.orientation(OrientationType.YAW, DEGREES)


if brain.sdcard.is_inserted(): #SD card inserted: Run this
    line = f"Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}\n"
    brain.sdcard.savefile("data.csv", bytearray(line, "utf-8"))
    data_collector()
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("Data collection complete")
else: # No SD card: Tether 
    brain.timer.clear()
    while True:
            timer = brain.timer.time(MSEC)
                
            print(f"Time: {timer} Roll: {inertial.orientation(OrientationType.ROLL, DEGREES)}")
            print(f"Time: {timer} Pitch: {inertial.orientation(OrientationType.PITCH, DEGREES)}")
            print(f"Time: {timer} Yaw: {inertial.orientation(OrientationType.YAW, DEGREES)}")
        
            wait(0.1, SECONDS)

            if timer >= 30000:
                break


