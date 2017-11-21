'''All the stuff for preparing a cracker(will have to spill into other files).'''

from rational_motors.motor_driver import JoeBoard
import time

class Choreographer:
    STEPS = 513
    CONVEYOR_SCALE = 1
    POUR_STEPS = 125
    def __init__(self):
        self.board = JoeBoard(6, 1000)
        self.is_pouring = False
        self.board.add_stepper(0, 1)
        self.board.add_stepper(2, 3)
        self.board.add_stepper(4, 5)

    def rotate_top(self, angle, direction):
        steps = round(self.STEPS*(angle/360))
        self.board.step_stepper(0, steps, direction)

    def move_conveyor(self, distance, direction):
        steps = round(distance*self.CONVEYOR_SCALE)
        self.board.step_stepper(1, steps, distance)

    def set_sauce(self, activeRaw=False):
        if activeRaw:
            self.is_pouring = True
            self.board.step_stepper(2, 125, 1)
        else:
            self.is_pouring = False
            self.board.step_stepper(2, 125, -1)

    def calibrate(self, is_raw):
        pass

    def prepare_cracker(self):
        self.rotate_top(90, 1)
        time.sleep(1)
        self.move_conveyor(90, 1)
        time.sleep(1)
        self.rotate_top(90, 1)
        timesleep(1)
        self.set_sauce(True)
        time.sleep(5)
        self.set_sauce(False)
        time.sleep(5)
        self.rotate_top(90, 1)
        time.sleep(2)


CHOREOGRAPHER = Choreographer()






    

