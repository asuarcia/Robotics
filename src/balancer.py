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


def data_collector():
    brain.timer.clear()

    while True:
        timer = brain.timer.time(MSEC)
            
        roll = inertial.orientation(OrientationType.ROLL, DEGREES)
        pitch = inertial.orientation(OrientationType.PITCH, DEGREES)
        yaw = inertial.orientation(OrientationType.YAW, DEGREES)
       
        line = f"{timer} {roll}, {timer} {pitch}, {timer} {yaw}\n"
        brain.sdcard.appendfile("data.csv", bytearray(line, "utf-8"))
        
        wait(0.1, SECONDS)

        if timer >= 30000:
            break




if brain.sdcard.is_inserted():
    line = f"Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}\n"
    brain.sdcard.savefile("data.csv", bytearray(line, "utf-8"))
    data_collector()
    brain.screen.clear_screen()
    brain.screen.print("Data collection complete")
else:
    brain.screen.print("Insert SD card")



