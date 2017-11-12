from gpiozero import PWMOutputDevice
from rational_motors.mcp23017 import MCP23017
import time

class JoeSlot:
    def __init__(self, mcp: MCP23017, pwm_pin, control_pins, supply_voltage):
        self.mcp = mcp
        self.supply_voltage = supply_voltage
        self.control_pins = control_pins
        self.pwm_pin = PWMOutputDevice(pwm_pin)
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
        if value <= self.supply_voltage:
            self._scale_factor = round((value/self.supply_voltage), 3)
        else:
            print("Cannot set higher than supply!")

    @property
    def speed(self):
        '''Gets speed'''
        return self._speed
    @speed.setter
    def speed(self, value):
        '''Sets speed as pwm value.'''
        if value <= 1 and value >= 0:
            self._speed = value
            self.pwm_pin.value = self._scale_factor*value
        else:
            print("Invalid speed.")
    @property
    def direction(self):
        '''Get direction'''
        return self._direction
    @direction.setter
    def direction(self, value):
        '''Sets the directional control pins.'''
        if value == 0:
            self.mcp.output(self.control_pins[0], 0)
            self.mcp.output(self.control_pins[0], 0)
            self._direction = 0
        elif value == 1:
            self.mcp.output(self.control_pins[0], 0)
            self.mcp.output(self.control_pins[0], 1)
            self._direction = 0
        elif value == -1:
            self.mcp.output(self.control_pins[0], 1)
            self.mcp.output(self.control_pins[0], 0)
            self._direction = 0
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
        self.slots = []
        for pin_set in self.PINS:
            self.slots.append(JoeSlot(
                self.pins, 
                pin_set[0], 
                pin_set[1:], 
                supply_voltage
            ))
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

    def set_slot(self, slot, direction, speed):
        if 0 <= slot <= 5:
            self.slots[slot].direction = direction
            self.slots[slot].speed = speed
        else:
            print("Only 6 slots.")

    def add_motor(self, slot, voltage=None):
        if 0 <= slot <= 5 and slot not in self.used_slots:
            if voltage:
                self.slots[slot].voltage = voltage
            self.motors.append(slot)

    def set_motor(self, mot_no, direction, speed):
        slot = self.motors[mot_no]
        self.slots[slot].speed = speed
        self.slots[slot].direction = direction

    def add_stepper(self, slot1, slot2, voltage=None):
        if not (0 <= slot1 <= 5 and slot1 not in self.used_slots):
            print("Slot1 is invalid")
            return
        if not (0 <= slot2 <= 5 and slot2 not in self.used_slots):
            print("Slot2 is invalid")
            return
        if slot1 == slot2:
            print("Needs different slots!")
            return
        if voltage:
            self.slots[slot1].voltage = voltage
            self.slots[slot2].voltage = voltage
        self.steppers.append([slot1, slot2])
    
    def _set_stepper_step(self, stepper, step):
        stepslots  = self.steppers[stepper]
        for i in range(2):
            self.slots[stepslots[i]] = step[i]

    def step_stepper(self, stepper, times=1):
        if not (len(self.steppers) > stepper):
            print("That isnt a stepper.")
        for _ in range(times):
            for i in range(4):
                self._set_stepper_step(stepper, self.STEPPER_STEPS[i])
                time.sleep(self.delay/1000)

    


    


