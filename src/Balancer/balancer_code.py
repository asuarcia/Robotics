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





'''