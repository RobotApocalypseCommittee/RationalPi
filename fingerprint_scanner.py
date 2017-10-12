import enum
import serial
import binascii
import sys
import time

class ResponsePacket:
    def __init__(self, data):
        self.data = data
        self.ok = (int.from_bytes(data[8:10], 'little') == 0x30)
        self.parameter = int.from_bytes(data[4:8], 'little')

class FingerprintException(Exception):
    pass

class Command:
    OPEN = 0x01
    CLOSE = 0x02
    CHANGE_LED = 0x12
    GET_ENROLL_COUNT = 0x20
    CHECK_ENROLLED = 0x21
    ENROLL_START = 0x22
    ENROLL1 = 0x23
    ENROLL2 = 0x24
    ENROLL3 = 0x25
    IS_PRESS_FINGER = 0x26
    DELETE_ID = 0x40
    IDENTIFY = 0x51
    CAPTURE = 0x60


class FingerprintScanner:
    errors = {
        0x1003: "ID out of range",
        0x1004: "ID is not used",
        0x1005: "ID is already used",
        0x1006: "Communication Error",
        0x1007: "1:1 Verification Error",
        0x1008: "1:N Identification Error",
        0x1009: "The database is full",
        0x100A: "The database is empty",
        0x100B: "Invalid order of enrollment",
        0x100C: "Too bad fingerprint",
        0x100D: "Enrollment Failure",
        0x100E: "Command not supported",
        0x100F: "Device Error",
        0x1010: "Capturing is cancelled",
        0x1011: "Invalid Parameter",
        0x1012: "Finger is not pressed",
        
    }
    def __init__(self, port):
        self._ser = serial.Serial(port, baudrate=9600, timeout=2)
        self._open()
        self.led = False
    
    def _open(self):
        retval = self._do_command(Command.OPEN)
        if not retval:
            raise"Cannot open fingerprint sensor.")

    def _revert_led(self):
        senddata = 1 if self.led else 0
        self._do_command(Command.CHANGE_LED, senddata)
    
    def _do_command(self, command_id, data=0):
        command = bytearray([0x55, 0xAA, 0x01, 0x00])
        command.extend(data.to_bytes(4, byteorder='little'))
        command.extend(command_id.to_bytes(2, byteorder='little'))
        command.extend((sum(command)).to_bytes(2, byteorder='little'))
        if (self._ser.is_open):
            self._ser.write(command)
            response_data = self._ser.read(12)
            response = ResponsePacket(response_data)
            if (response.ok):
                return response
            else:
                return response # TODO: Add error code strings...
        else:
            self.print_error("Cannot write to serial, port closed.")
    def change_led(self, state = True, preserve=True):
        senddata = 1 if state else 0
        self.led = state if preserve else self.led
        self._do_command(Command.CHANGE_LED, senddata)

    def is_finger_pressed(self):
        self.change_led(True, False)
        resp = self._do_command(Command.IS_PRESS_FINGER)
        self._revert_led()
        if (resp.parameter == 0):
            return True
        else:
            return False

    def capture_finger(self, slow=True):
        senddata = 1 if slow else 0
        self.change_led(True, False)
        resp = self._do_command(Command.CAPTURE, senddata)
        self._revert_led
        return resp

    def count_enrolled(self):
        resp = self._do_command(Command.GET_ENROLL_COUNT)
        return resp.parameter

    def determine_next_id(self):
        next_id = 20
        for i in range(20):
            if not self._do_command(Command.CHECK_ENROLLED, i).ok:
                next_id = i
                break
        if id == 20:
            self.print_error("No more space for people.")
        else:
            return next_id

    
    def enroll_person(self):
        person_id = self.determine_next_id()
        self._do_command(Command.ENROLL_START, person_id)
        for i in range(3):
            self.change_led()
            while not self.is_finger_pressed(): time.sleep(0.1)
            resp = self.capture_finger()
            if not resp.ok:
                print(resp.parameter)
            resp = self._do_command(Command.ENROLL1 + i)
            if not resp.ok:
                print(resp.parameter)
            self.change_led(False)
            while self.is_finger_pressed(): time.sleep(0.1)
        return person_id

    def delete_person(self, id):
        resp = self._do_command(Command.DELETE_ID, id)
        return resp.ok

    def identify_person(self):
        self.change_led(True, False)
        self.capture_finger()
        resp = self._do_command(Command.IDENTIFY)
        self._revert_led()
        if resp.ok:
            return resp.parameter
        else:
            return False
    def close(self):
        self._ser.close()

            






