'''All the stuff for preparing a cracker(will have to spill into other files).'''

from rational_motors.motor_driver import JoeBoard
import time

class Choreographer:
    STEPS = 513
    CONVEYOR_SCALE = 1
    POUR_STEPS = 125
    def __init__(self):
        self.board = JoeBoard(6)
        self.is_pouring = False
        self.board.add_stepper(0, 1)
        self.board.add_stepper(2, 3)
        self.board.add_motor(4)

    def rotate_top(self, angle, direction):
        steps = round(self.STEPS*(angle/360))
        self.board.step_stepper(0, steps, direction)

    def move_conveyor(self, distance, direction):
        steps = round(distance*self.CONVEYOR_SCALE)
        self.board.step_stepper(1, steps, direction)

    def pour_sauce(self, duration):
        self.board.set_motor(0, 1, 1)
        time.sleep(duration)
        self.board.set_motor(0, 0, 0)

    def calibrate(self, is_raw):
        pass

    def prepare_cracker(self, cheese, sauce):
        # Collect Cracker
        self.rotate_top(90, 1)
        time.sleep(1)
        self.rotate_top(90, 1)
        if cheese:
            # Dispense Cheese
            self.move_conveyor(90, 1)
            time.sleep(1)
        # Move cracker along
        self.rotate_top(90, 1)
        time.sleep(1)
        if sauce:
            # Dispense Sauce
            self.pour_sauce(2)
        # Move cracker along
        self.rotate_top(90, 1)
        time.sleep(2)


CHOREOGRAPHER = Choreographer()






    

