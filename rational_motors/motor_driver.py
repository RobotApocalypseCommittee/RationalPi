from gpiozero import PWMOutputDevice, DigitalOutputDevice
from rational_motors.mcp23017 import MCP23017
import time

class JoeSlot:
    def __init__(self, mcp: MCP23017, pwm_pin, control_pins, supply_voltage, pwm=True):
        self.mcp = mcp
        self.supply_voltage = supply_voltage
        self.control_pins = control_pins
        self.pwm = pwm
        if self.pwm:
            self.pwm_pin = PWMOutputDevice(pwm_pin)
        else:
            self.pwm_pin = DigitalOutputDevice(pwm_pin)
            self.pwm_pin.on()
        self.mcp.setup(self.control_pins[0], 0)
        self.mcp.setup(self.control_pins[1], 0)
        self._scale_factor = 1
        self._speed = 1
        self._direction = 0
   
    @property
    def voltage(self):
        return self._scale_factor*self.supply_voltage
    @voltage.setter
    def voltage(self, value):
        if self.pwm:
            if value <= self.supply_voltage:
                self._scale_factor = round((value/self.supply_voltage), 3)
            else:
                print("Cannot set higher than supply!")
        else:
            print("Can't set speed for non-pwm pin.")

    @property
    def speed(self):
        '''Gets speed'''
        return self._speed
    @speed.setter
    def speed(self, value):
        '''Sets speed as pwm value.'''
        if self.pwm:
            if value <= 1 and value >= 0:
                self._speed = value
                self.pwm_pin.value = self._scale_factor*value
            else:
                print("Invalid speed.")
        else:
            print("Can't set speed for non-pwm pin.")
    @property
    def direction(self):
        '''Get direction'''
        return self._direction
    @direction.setter
    def direction(self, value):
        '''Sets the directional control pins.'''
        if value == 0:
            self.mcp.output(self.control_pins[0], 0)
            self.mcp.output(self.control_pins[1], 0)
            self._direction = 0
        elif value == 1:
            self.mcp.output(self.control_pins[0], 0)
            self.mcp.output(self.control_pins[1], 1)
            self._direction = 1
        elif value == -1:
            self.mcp.output(self.control_pins[0], 1)
            self.mcp.output(self.control_pins[1], 0)
            self._direction = -1
        else:
            print("Invalid direction")





class JoeBoard:
    FORWARD = 1
    BACKWARD = -1
    STOPPED = 0
    PINS = [(4, 0, 1), (17, 2, 3), (18, 5, 4), (22, 6, 7), (23, 8, 9), (24, 10, 11)]
    STEPPER_STEPS = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    def __init__(self, supply_voltage, stepper_delay=1000):
        self.pins = MCP23017()
        self.slots = [None, None, None, None, None, None]
        self.supply_voltage = supply_voltage
        self.motors = []
        self.steppers = []
        self.delay = stepper_delay

    @property
    def used_slots(self):
        used = self.motors
        for stepper in self.steppers:
            used.extend(stepper)
        return used

    def set_pwm_slot(self, slot, direction, speed):
        if 0 <= slot <= 5 and self.slots[slot] and self.slots[slot].pwm:
            self.slots[slot].direction = direction
            self.slots[slot].speed = speed
        else:
            print("Invalid Slot for PWM slot change.")

    def set_slot(self, slot, direction):
        if 0 <= slot <= 5 and self.slots[slot] and not self.slots[slot].pwm:
            self.slots[slot].direction = direction
        else:
            print("Invalid Slot for non PWM slot change.")

    def init_slot(self, slot, pwm=True):
        self.slots[slot] = JoeSlot(
            self.pins,
            self.PINS[slot][0],
            self.PINS[slot][1:],
            self.supply_voltage,
            pwm
        )

    def add_motor(self, slot, voltage=None):
        if 0 <= slot <= 5 and slot not in self.used_slots:
            self.init_slot(slot, True)
            if voltage:
                self.slots[slot].voltage = voltage
            self.motors.append(slot)

    def set_motor(self, mot_no, direction, speed):
        slot = self.motors[mot_no]
        self.slots[slot].speed = speed
        self.slots[slot].direction = direction

    def add_stepper(self, slot1, slot2):
        if not (0 <= slot1 <= 5 and slot1 not in self.used_slots):
            print("Slot1 is invalid")
            return
        if not (0 <= slot2 <= 5 and slot2 not in self.used_slots):
            print("Slot2 is invalid")
            return
        if slot1 == slot2:
            print("Needs different slots!")
            return
        self.init_slot(slot1, False)
        self.init_slot(slot2, False)
        self.steppers.append([slot1, slot2])
    
    def _set_stepper_step(self, stepper, step):
        stepslots  = self.steppers[stepper]
        for i in range(2):
            self.set_slot(stepslots[i], step[i])

    def step_stepper(self, stepper, times=1, direction=1):
        if not (direction is 1 or direction is -1):
            print("Bad Direction")
        if not (len(self.steppers) > stepper):
            print("That isnt a stepper.")
        for _ in range(times):
            for i in range(0, 4, direction):
                self._set_stepper_step(stepper, self.STEPPER_STEPS[i])
                time.sleep(self.delay/1000)

    


    


