from picamera import PiCamera
import time

x = PiCamera()
x.rotation = 180

def do_it(user):
    for i in range(10):
        time.sleep(2)
        x.capture('Face Storage/{}.{}.jpg'.format(user, i))
        print('Capture taken')
