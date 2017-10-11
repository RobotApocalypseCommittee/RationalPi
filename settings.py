import json

from picamera import PiCamera
import cv2

# inits tkinter container
CONTROLLER = None

# inits camera
CAMERA = PiCamera()
CAMERA.rotation = 180

# gets the list of users
with open('user_data.json', 'r') as userFile:
    USER_DICT = json.load(userFile)
    USER_DICT = {int(key):val for key, val in USER_DICT.items()}

# inits misc stuff for authentication
FACE_RECOGNISER = cv2.face.LBPHFaceRecognizer_create()

FACE_CASCADE = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

CONF_THRESHOLD = 1000

SAVE_IMAGE_CONF = 15

FINGERPRINT_CONF = 15

DEVICE_NAME = '/dev/ttyUSB0'
