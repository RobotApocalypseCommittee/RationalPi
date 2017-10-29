from rational_motors.mcp23017 import MCP23017

class JoeBoard:
    def __init__(self):
        self.pins = MCP23017()
        # TODO: Implement
