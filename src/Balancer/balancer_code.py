'''
Roll: Lean forward and back
Pitch side to side:
Yaw: Turning
'''

import vex
from vex import *

#--------------------Setup-----------------------------------------------------------------------------------------------------
brain = Brain()
motor_group_10_motor_a = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
motor_group_10_motor_b = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO_18_1, False)
motor_wheels = vex.MotorGroup(motor_group_10_motor_a, motor_group_10_motor_b)
inertial = vex.Inertial(vex.Ports.PORT9)

#--------------------Calibration----------------------------------------------------------------------------------------------
inertial.calibrate()

while inertial.is_calibrating():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("Inertial Sensor is Calibrating")
    wait(50, MSEC)

#--------------------Controllers---------------------------------------------------------------------------------------------

# P (Proportion)--------------------------------

target = 0.95 #Balance point (If doesn't work then: 0.9-1.2)
Kp = 0.5 # Test for num in volts/degree (to move one degree use x volts)


def read_roll():
    roll = inertial.orientation(vex.OrientationType.ROLL, DEGREES)
    return roll

def calc_output(error):
    output = Kp * error
    return output





while True:
    roll = read_roll()
    error  = target - roll
    output = calc_output(error)

    if output > 12:
        output = 12
    elif output < -12:
        output = -12

    if abs(roll) >=  35:
        motor_wheels.stop()
        break

    motor_wheels.spin(FORWARD, output, VOLT)  

    wait(10, MSEC)

''' 
Finding Kp

1. Wheels in the air first. Lean the robot forward and back. The wheels should drive toward the lean. If they go the wrong way, flip the sign before you go any further.
2. Start with Kp = 0.5. Hold the robot upright on the floor, let go, and keep a hand ready to catch it.
3. Watch what it does:
   - Lazy: it slowly tips over without fighting → double Kp.
   - Rocks back and forth: that's the sweet spot. Stop here.
   - Shakes violently or jitters: too high → go back halfway to your last value.
4. Repeat step 3, changing only Kp, until it rocks back and forth on its own for a few seconds.
5. Write that number down. That's your Kp, and you'll keep it when you add D.

Tips
- Change one thing at a time.
- Start every test from the same position, held upright at the balance point.
- If it always drifts off in one direction, your target is a little off. Nudge it by about 0.1–0.2 toward the side it falls to.
- Expect it to rock and still fall. Rocking means P is working, and D is what stops the rocking.

Choosing Kp

Kp is in volts per degree. Think it through: if Kp = 1, how many degrees of tilt before you hit the 12 V limit?
 Start smaller than you think, around 0.5. Raise it when the robot is too lazy, lower it when it's too twitchy.


'''




