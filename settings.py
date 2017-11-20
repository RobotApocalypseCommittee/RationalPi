'''Main settings and singleton/constants defined here'''

try:
    from picamera import PiCamera
    from picamera.exc import PiCameraError
except ImportError:
    pass

from serial.serialutil import SerialException
import cv2

from fingerprint_scanner import FingerprintScanner, FingerprintException
from rational_utils.data_manager import SavedDict

# inits camera
try:
    CAMERA = PiCamera()
    CAMERA.rotation = 180
except (NameError, PiCameraError):
    pass

SYSTEM_DATA = SavedDict("data.json")


try:
    FINGERPRINT_SENSOR = FingerprintScanner(SYSTEM_DATA['deviceName'])
except SerialException:
    FINGERPRINT_SENSOR = None

TRAINED_FILES = []

