import json

try:
    from picamera import PiCamera
except ImportError:
    pass

import cv2

from fingerprint_scanner import FingerprintScanner

# inits camera
try:
    CAMERA = PiCamera()
    CAMERA.rotation = 180
except NameError:
    pass

# gets the list of users
with open('user_data.json', 'r') as userFile:
    USER_DICT = json.load(userFile)
    USER_DICT = {int(key):val for key, val in USER_DICT.items()}

with open('misc_data.json', 'r') as miscFile:
    _stored_vars = json.load(miscFile)
    CRACKERS_LEFT = int(_stored_vars['crackersLeft'])
    # whatever else gets added (if anything...)

# inits misc stuff for authentication
try:
    FACE_RECOGNISER = cv2.face.LBPHFaceRecognizer_create()

    FACE_CASCADE = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
except (NameError, AttributeError):
    print("Could not load CV2, Prepare for errors...")

CONF_THRESHOLD = 1000

SAVE_IMAGE_CONF = 15

FINGERPRINT_CONF = 15

DEVICE_NAME = '/dev/ttyAMA0'

FINGERPRINT_SENSOR = FingerprintScanner(DEVICE_NAME)

TRAINED_FILES = []
