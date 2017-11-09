'''Main settings and singleton/constants defined here'''

try:
    from picamera import PiCamera
except ImportError:
    pass

from serial.serialutil import SerialException
import cv2

from fingerprint_scanner import FingerprintScanner
from rational_utils.data_manager import SavedDict

# inits camera
try:
    CAMERA = PiCamera()
    CAMERA.rotation = 180
except NameError:
    pass

SYSTEM_DATA = SavedDict("data.json")

# inits misc stuff for authentication
try:
    FACE_RECOGNISER = cv2.face.LBPHFaceRecognizer_create()

    FACE_CASCADE = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
except (NameError, AttributeError):
    print("Could not load CV2, Prepare for errors...")

try:
    FINGERPRINT_SENSOR = FingerprintScanner(SYSTEM_DATA['deviceName'])
except SerialException:
    FINGERPRINT_SENSOR = None

TRAINED_FILES = []
