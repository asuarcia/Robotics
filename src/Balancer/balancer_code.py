'''
Roll: Lean forward and back
Pitch side to side:
Yaw: Prob up and down
'''

import vex
from vex import *

#--------------------Setup-----------------------------------------------------------------------------------------------------
brain = Brain()
left_motor = vex.Motor(vex.Ports.PORT5, vex.GearSetting.RATIO_18_1, False)
right_motor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
inertial = vex.Inertial(vex.Ports.PORT9)

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
#--------------------Controllers---------------------------------------------------------------------------------------------

# P (Proportion)--------------------------------

''' 
1. Read ROLL

2. Calculate error (E = target (balance point) - current (position/inertial reading))

3. Calculate output (Kp x Error) (Motor output)

4. Clamp output to never go past motor limit

5. Send output to motor

6. Wait then repeat (~10 MS)

Sure, a setpoint of 0 is a fine starting assumption. Once you have the real number it's a one-line change.

The idea

P control means one thing: push back in proportion to how far you're tipped.

- Error: how far you are from where you want to be, setpoint - roll.
- Output: Kp × error. Tipped 2° gives a small push; tipped 10° gives a big push.
- Kp: the "how hard to react" knob. That's the number you'll tune.

What your loop needs to do, in order

1. Read roll.
2. Calculate the error.
3. Calculate the output.
4. Clamp the output so it never goes past the motor's limit.
5. Send the output to both motors.
6. Wait about 10 ms, then repeat.

Put these before the loop: a SETPOINT constant, a KP constant, and a sensor calibration that waits until it finishes.

Things you'll need to know

- Use voltage, not velocity. motor.spin(FORWARD, value, VOLT) takes −12 to 12. Velocity mode runs VEX's own hidden controller underneath yours and adds lag. Voltage gives your P controller direct control.
- Negative values work. A negative voltage with FORWARD spins the motor backward, so you don't need an if/else for direction.
- No SD logging inside this loop yet. Earlier we noted that appendfile every loop is slow. Here, slow means the robot falls over.
- Add a safety cutoff. If abs(roll) goes over about 40°, the robot has fallen. Stop the motors so the wheels don't spin wildly on the floor.

Choosing Kp

Kp is in volts per degree. Think it through: if Kp = 1, how many degrees of tilt before you hit the 12 V limit? Start smaller than you think, around 0.5. Raise it when the robot is too lazy, lower it when it's too twitchy.

What to expect

- The sign may be backwards. If you tilt the robot by hand and the wheels move away from the lean, flip the sign of the output. That's the one-line fix we'd have found with the CSV.
- P alone probably won't balance it. Expect it to rock back and forth and overshoot. That's normal, and it's the reason D exists, which is the next lesson.

Write it up, save it, and tell me when you want me to look it over. I'll point out problem lines and give hints, not rewrites.



'''