'''All the stuff for preparing a cracker(will have to spill into other files).'''

from rational_motors.motor_driver import JoeBoard

class Choreographer:
    def __init__(self):
        self.board = JoeBoard(6, 1000)
        self.board.add_stepper(0, 1)
        self.board.add_stepper(2, 3)
        self.board.add_stepper(4, 5)
    def rotate_top(self, steps, direction):
        self.board.step_stepper(0, steps, direction)

    

