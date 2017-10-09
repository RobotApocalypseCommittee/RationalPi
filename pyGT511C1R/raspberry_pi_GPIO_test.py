'''
Created on 08/04/2014

@author: jeanmachuca

SAMPLE CODE:

This script is a test for device connected to GPIO port in raspberry pi

For test purpose:

Step 1:
Connect the TX pin of the fingerprint GT511C3 to RX in the GPIO

Step 2:
Connect the RX pin of the fingerprint GT511C3 to TX in the GPIO

Step 3:
Connect the VCC pin of the fingerprint GTC511C3 to VCC 3,3 in GPIO

Step 4:
Connect the Ground pin of fingerprint GT511C3 to ground pin in GPIO


This may be works fine, if don't, try to change the fingerprint baud rate with baud_to_115200.py sample code


'''
import FPS
import sys

DEVICE_GPIO = '/dev/serial0'
FPS.BAUD = 115200
FPS.DEVICE_NAME = DEVICE_GPIO

if __name__ == '__main__':
    fps =  FPS.FPS_GT511C3(device_name=DEVICE_GPIO,baud=115200,timeout=2,is_com=False)
    fps.UseSerialDebug = False
    for i in range(5):
        print("BLINK")
        fps.SetLED(True) # Turns ON the CMOS LED
        FPS.delay(1) # wait 1 second
        fps.SetLED(False)
        FPS.delay(1)

    fps.Close() # Closes serial connection
    pass
