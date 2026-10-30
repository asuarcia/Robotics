



from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_drive_smart = Motor(Ports.PORT16, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 398.98, 370, 195, MM, 1)
Claw_arm = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False)
Claw = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)

'''
# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()
'''


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

def autonomous():

    brain.screen.print("Aitor Suarez")
    Claw_arm.set_velocity(25, PERCENT)
    Claw_arm.spin_to_position(490, DEGREES)
    Claw_arm.spin_to_position(0, DEGREES)

    drivetrain.drive_for(FORWARD, 45, INCHES)
    drivetrain.turn_for(LEFT, 115, DEGREES)
    drivetrain.drive_for(FORWARD, 46, INCHES)
    Claw_arm.spin_to_position(300, DEGREES)
    Claw.spin_to_position(-200, DEGREES)
    Claw.spin_to_position(50, DEGREES)


    Claw_arm.spin_to_position(490, DEGREES) #Max when starting at bottom
   
    Claw.spin_to_position(-200, DEGREES) #Max open

    

autonomous()

