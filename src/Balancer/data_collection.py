'''
Roll: Lean forward and back
Pitch side to side:
Yaw: Prob up and down
'''

import vex
from vex import *

#--------------------Setup-----------------------------------------------------------------------------------------------------
brain = Brain()
motor_group_10_motor_a = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
motor_group_10_motor_b = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
motor_group_10 = MotorGroup(motor_group_10_motor_a, motor_group_10_motor_b)
Inertial = vex.Inertial(vex.Ports.PORT9)

#--------------------Calibration----------------------------------------------------------------------------------------------
inertial.calibrate()
wait(10, SECONDS)
'''
while inertial.is_calibrating():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("Inertial Sensor is Calibrating")
    wait(50, MSEC)
'''
#--------------------Measure position----------------------------------------------------------------------------------------

def data_collector(): # Function for SD card data collection and writing
    brain.timer.clear()

    while True:
        timer = brain.timer.time(MSEC)
            
        roll = inertial.orientation(OrientationType.ROLL, DEGREES)
        pitch = inertial.orientation(OrientationType.PITCH, DEGREES)
        yaw = inertial.orientation(OrientationType.YAW, DEGREES)
       
        line = "{}, {}, {}, {}\n".format(timer, roll, pitch, yaw)
        brain.sdcard.appendfile("data.csv", bytearray(line, "utf-8"))
        
        wait(0.1, SECONDS)

        if timer >= 30000:
            break


if brain.sdcard.is_inserted(): #SD card inserted: Run this
    line = "Time:, Roll:, Pitch:, Yaw:\n"
    brain.sdcard.savefile("data.csv", bytearray(line, "utf-8"))
    data_collector()
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("Data collection complete")
else: # No SD card: Tether 
    brain.timer.clear()
    while True:
            brain.screen.clear_screen()
            brain.screen.set_cursor(1,1)
            timer = brain.timer.time(MSEC)
                
            brain.screen.print("Time: {} Roll: {} Pitch: {} Yaw: {}".format(
    timer,
    inertial.orientation(OrientationType.ROLL, DEGREES),
    inertial.orientation(OrientationType.PITCH, DEGREES),
    inertial.orientation(OrientationType.YAW, DEGREES)
))
        
            wait(0.1, SECONDS)

            if timer >= 30000:
                break
