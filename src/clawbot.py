import vex
from vex import *

# ----------------------------------------------------------------------------
# Initialization & Setup
# ----------------------------------------------------------------------------
brain = Brain()
controller_1 = Controller()

# Motors setup
# Adjust reverse flags (True/False) if any motor spins backwards
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
claw_motor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
claw_arm_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)

# Set claw stopping mode so it holds position when stopped
claw_motor.set_stopping(HOLD)
claw_motor.set_stopping(HOLD)

# Variable tracking
drivetrain_speed = 50  # Starting speed percentage (0 to 100)
min_speed = 10
max_speed = 100

# Button debouncing state flags for single-press actions
up_pressed_last = False
down_pressed_last = False
a_pressed_last = False
b_pressed_last = False


def update_controller_screen():
    """Helper function to print current drive speed on the controller display."""
    controller_1.screen.clear_row(1)
    controller_1.screen.set_cursor(1, 1)
    controller_1.screen.print("Drive Speed: " + str(drivetrain_speed) + "%")


# Initial screen render
update_controller_screen()

# ----------------------------------------------------------------------------
# Main Control Loop
# ----------------------------------------------------------------------------
while True:
    # ========================================================================
    # 1. Speed Adjustment (Up / Down Arrows)
    # ========================================================================
    up_currently_pressed = controller_1.buttonUp.pressing()
    down_currently_pressed = controller_1.buttonDown.pressing()

    # Increase speed on new press of UP arrow
    if up_currently_pressed and not up_pressed_last:
        drivetrain_speed = min(max_speed, drivetrain_speed + 5)
        update_controller_screen()

    # Decrease speed on new press of DOWN arrow
    if down_currently_pressed and not down_pressed_last:
        drivetrain_speed = max(min_speed, drivetrain_speed - 5)
        update_controller_screen()

    up_pressed_last = up_currently_pressed
    down_pressed_last = down_currently_pressed

    # ========================================================================
    # 2. Claw Control (Manual & Full Open/Close)
    # ========================================================================
    a_currently_pressed = controller_1.buttonA.pressing()
    b_currently_pressed = controller_1.buttonB.pressing()

    # (A) Full Open / Close (Button A / Button B)
    if a_currently_pressed and not a_pressed_last:
        # Spins to 0 degrees position (adjust target angle if needed)
        claw_motor.spin_to_position(0, DEGREES, 50, PERCENT, False)
    elif b_currently_pressed and not b_pressed_last:
        # Spins to closed position (adjust target angle for your claw mech)
        claw_motor.spin_to_position(180, DEGREES, 50, PERCENT, False)

    a_pressed_last = a_currently_pressed
    b_pressed_last = b_currently_pressed

    # (B) Manual Gradual Open / Close (L1 / R1)
    # Checks manual controls only if non-blocking auto movement isn't running
    if controller_1.buttonL1.pressing():
        claw_motor.spin(FORWARD, 40, PERCENT)
    elif controller_1.buttonR1.pressing():
        claw_motor.spin(REVERSE, 40, PERCENT)
    elif not claw_motor.is_spinning():
        claw_motor.stop()

    # ========================================================================
    # 3. Basic Movement (Left Joystick Arcade Drive)
    # ========================================================================
    # Axis 3 = Up/Down (Forward/Reverse), Axis 4 = Left/Right (Turning)
    forward_power = controller_1.axis3.position()
    turn_power = controller_1.axis4.position()

    # Calculate motor outputs scaled by current drivetrain_speed setting
    scale_factor = drivetrain_speed / 100.0
    left_power = (forward_power + turn_power) * scale_factor
    right_power = (forward_power - turn_power) * scale_factor

    left_motor.spin(FORWARD, left_power, PERCENT)
    right_motor.spin(FORWARD, right_power, PERCENT)

    # Short delay to reduce CPU load and prevent execution issues
    wait(20, MSEC)
