# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       casuro                                                       #
# 	Created:      9/28/2026, 8:56:24 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

import vex
from vex import *

brain = Brain()

# Define the 2 rear motors
left_motor = vex.Motor(vex.Ports.PORT1, False)
right_motor = vex.Motor(vex.Ports.PORT10, True)

# Define the Inertial Sensor (Port 2)
inertial_sensor = vex.Inertial(vex.Ports.PORT2)

# Configure SmartDrive
# Parameters: (Left Motor, Right Motor, Inertial Sensor, Wheel Travel, Track Width, Wheel Base, Units, External Gear Ratio)
drivetrain = SmartDrive(
    left_motor,
    right_motor,
    inertial_sensor,
    319.19,
    295,
    200,
    DistanceUnits.MM,
    1
)

def autonomous():
    # Calibrate the gyro before driving
    inertial_sensor.calibrate()
    while inertial_sensor.is_calibrating():
        wait(20, MSEC)

    drivetrain.drive_for(FORWARD, 228, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 96, INCHES)
    drivetrain.turn_for(LEFT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 96, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 138, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 132, INCHES)
    drivetrain.turn_for(LEFT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 132, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 120, INCHES)
    drivetrain.turn_for(LEFT, 2, TURNS)

autonomous()


'''
import vex
from vex import *

# Initialize the Brain
brain = Brain()

# Define the 2 rear motors
left_motor = vex.Motor(vex.Ports.PORT1, False)
right_motor = vex.Motor(vex.Ports.PORT10, True)

# Configure the 2-Motor Drivetrain
# Parameters: (Left Motor, Right Motor, Wheel Travel, Track Width, Units, External Gear Ratio)
drivetrain = DriveTrain(left_motor, right_motor, 319.19, 295, 1)

def autonomous():

    drivetrain.drive_for(FORWARD, 228, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 96, INCHES)
    drivetrain.turn_for(LEFT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 96, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 138, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 132, INCHES)
    drivetrain.turn_for(LEFT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 132, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 120, INCHES)
    drivetrain.turn_for(LEFT, 2, TURNS)

    
autonomous()

'''

