'''Motor control'''

import RPi.GPIO as GPIO
import serial
from time import sleep

class motorController:
    
    def __init__(self, motors = [], steppers = [], servos = []):
        
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
            #Find port on pi first
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
        #write commands to the arduino controlling servos via serial
        command = identity + angle + "X"
        ser.write(str.encode(command))
    
    def setStep(self, identity, steps):
        stepper = self.steppers[identity]

        for pin, i in stepper, steps:
            GPIO.output(pin, i)

    def stepRotate(self, identity, direction, steps, delay = 50):
        
            for rotations in range(0, steps):
                if direction == 1:
                    for step in self.stepCycle:
                        self.setStep(identity, step)
                        time.sleep(delay / 1000)
                
                else:
                    for step in reversed(self.stepCycle):
                        self.setStep(identity, step)
                        time.sleep(delay / 1000)

    def shutdown(self):
        ser.close()


        
    
