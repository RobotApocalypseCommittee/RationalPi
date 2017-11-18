import smbus

def change_bit(number, bit, value):
    if value:
        return number | (1<<bit)
    else:
        return number & ~(1<<bit)

def get_bit(number,bit):
    return 1 if (number & (1 << bit)) else 0

class MCP23017:
    # IODIR, OLAT, GPIO
    PORT_ADDRESSES = [
        [0x00, 0x14, 0x12],
        [0x01, 0x15, 0x13]
    ]

    def __init__(self, address=0x20, port=1):
        self.bus = smbus.SMBus(port) # Rev 2 Pi uses 1
        self.address = address
        self.port_statuses = [[0,0,0], [0,0,0]] # Yes, it is ugly, I agree

    def _get_port(self, pin_no):
        port =  0 if pin_no < 8 else 1
        pin = pin_no if port==0 else pin_no-8
        return port, pin
    
    def setup(self, pin_no, direction):
        port, pin = self._get_port(pin_no)
        direction_byte = self.port_statuses[port][0]
        direction_byte = change_bit(direction_byte, pin, direction)
        self.port_statuses[port][0] = direction_byte
        register_address = self.PORT_ADDRESSES[port][0]
        self.bus.write_byte_data(self.address,register_address, direction_byte)

    def output(self, pin_no, state):
        port, pin = self._get_port(pin_no)
        output_byte = self.port_statuses[port][1]
        if get_bit(self.port_statuses[port][0], pin):
            print("Cannot write to input pin.")
        else:
            output_byte = change_bit(output_byte, pin, state)
            self.port_statuses[port][1] = output_byte
            register_address = self.PORT_ADDRESSES[port][0]
            self.bus.write_byte_data(self.address, register_address, output_byte)
    
    def input(self, pin_no):
        port, pin = self._get_port(pin_no)
        if not get_bit(self.port_statuses[port][0], pin):
            print("Cannot read from output pin.")
        else:
            input_byte = self.bus.read_byte_data(
                self.address, 
                self.PORT_ADDRESSES[port][2]
            )
            self.port_statuses[port][2] = input_byte
            return get_bit(input_byte, pin)