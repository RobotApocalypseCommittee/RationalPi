'''Motor control'''

import RPi.GPIO as GPIO
import serial
from time import sleep

class motorController:
    
    def __init__(self, motors = [], steppers = [], servos = []):
        #a motor of any kind comprises of a list of the relevant pins.
        #thus, motors could be passed as [ [0, 1], [2, 3] ]
        #and steppers could be [ [0, 1, 2, 3], [4, 5, 6, 7] ]
        #a servo is just a single pin, thus
        # [0, 1, 2, 3]
        
        self.motors = motors
        self.steppers = steppers
        self.stepCycle = [
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 0, 1]
        ]

        self.allPins = motors + steppers

        for pin in self.allPins:
            GPIO.setup(pin, GPIO.output)

        if len(servos) > 0:
            self.servos = servos
            ser = serial.Serial()
            ser.baud = 9600
            #TODO Find port on pi first
            # ser.port = 
            ser.open()

    def setMotor(self, identity, direction):
        #get motor
        motor = self.motors[identity]

        #2 will stop the motor
        if direction == 2:
            GPIO.output(motor[0], 0)
            GPIO.output(motor[1], 0)
            return

        #otherwise rotate the motor
        GPIO.output(motor[direction], 1) #set one pin in one direction, and set the other pin
        GPIO.output(motor[1 - direction], 0) #in the opposite

    

    def setServo(self, identity, angle):
        #write commands to the arduino controlling servos via serial in format
        command = identity + angle + "X" #e.g 190X
        ser.write(str.encode(command))
    
    def setStep(self, identity, steps):
        #get stepper
        stepper = self.steppers[identity]

        #set all gpio pins to equivalent value in steps
        for pin, i in stepper, steps:
            GPIO.output(pin, i)

    def stepRotate(self, identity, direction, steps, delay = 50):
        #Rotate the stepper motor

            for rotations in range(0, steps): #The number of steps to rotate
                #Forward rotation
                if direction == 1:
                    for step in self.stepCycle: #set stepper motor to appropriate value in cycle
                        self.setStep(identity, step)
                        time.sleep(delay / 1000) #sleep before next step; speed of motor
                
                else:
                    for step in reversed(self.stepCycle):
                        self.setStep(identity, step)
                        time.sleep(delay / 1000)

    def shutdown(self):
        #clean up things
        ser.close()
        #TODO: reset servos and motors


        
    
