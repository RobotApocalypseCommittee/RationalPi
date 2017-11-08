from gpiozero import PWMOutputDevice
from rational_motors.mcp23017 import MCP23017

class JoeSlot:
    def __init__(self, pwm_pin, control_pins, supply_voltage, mcp=MCP23017):
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
        return self._speed
    @speed.setter
    def speed(self, value):
        if value <= 1 and value >= 0:
            self._speed = value
            self.pwm_pin.value = self._scale_factor*value
        else:
            print("Invalid speed.")
    @property
    def direction(self):
        return self._direction
    @direction.setter
    def direction(self, value):
        if value == 0:
            self.mcp.output(self.control_pins[0], 0)
            self.mcp.output(self.control_pins[0], 0)
        elif value == 1:
            self.mcp.output(self.control_pins[0], 0)
            self.mcp.output(self.control_pins[0], 1)
        elif value == -1:
            self.mcp.output(self.control_pins[0], 1)
            self.mcp.output(self.control_pins[0], 0)
        else:
            print("Invalid direction")

    
    


class JoeBoard:
    FORWARD = 1
    BACKWARD = -1
    STOPPED = 0
    PINS = [(4, 0, 1), (17, 2, 3), (18, 5, 4), (22, 6, 7), (23, 8, 9), (24, 10, 11)]
    def __init__(self, supply_voltage):
        self.pins = MCP23017()
        self.slots = []
        for pin_set in self.PINS:
            self.slots.append(JoeSlot( 
                pin_set[0], 
                pin_set[1:], 
                supply_voltage,
                self.pins
            ))
        self.supply_voltage = supply_voltage


        
