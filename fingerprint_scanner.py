import enum
import serial
import binascii
import sys


class Command(enum.Enum):
    OPEN = 0x01,
    CLOSE = 0x02,
    CHANGE_LED = 0x12,
    GET_ENROLL_COUNT = 0x20,
    CHECK_ENROLLED = 0x21,
    ENROLL_START = 0x22,
    ENROLL1 = 0x23,
    ENROLL2 = 0x24,
    ENROLL3 = 0x25,
    IS_PRESS_FINGER = 0x26,
    DELETE_ID = 0x40,
    IDENTIFY = 0x51


class FingerprintScanner:
    def __init__(self, port):
        self._ser = serial.Serial(port, baudrate=9600, timeout=2)
        self._open()

    def print_error(self, string, stopping=True):
        print("[ERROR] "+ string)
        if stopping:
            self.close()
    
    def _open(self):
        retval = self._do_command(Command.OPEN)
        if not retval:
            self.print_error("Cannot open fingerprint sensor.")
    
    def _do_command(self, command_id, data=0):
        command = bytearray([0x55, 0xAA, 0x01, 0x00])
        command.extend(data.to_bytes(4, byteorder='little'))
        command.extend(command_id.to_bytes(2, byteorder='little'))
        command.extend((sum(command)).to_bytes(2, byteorder='little'))
        if (self._ser.is_open):
            self._ser.write(command)
            response = self._ser.read(12)
            if (int.from_bytes(response[8:10], byteorder='little') == 0x30):
                return True
            else:
                return False # TODO: Add error code strings...
        else:
            self.print_error("Cannot write to serial, port closed.")
    def change_led(self, state = True):
        if state:
            senddata = 1
        else:
            senddata = 0
        retval = self._do_command(Command.CHANGE_LED, senddata)
    


