import time

import cv2
from picamera.array import PiRGBArray

from settings import FACE_CASCADE, CAMERA, FINGERPRINT_SENSOR, CONTROLLER
import tools

def take_registration_photo(userId): # takes and saves ONE of a user's registration photos
    # see line 50 onwards
    rawCapture = PiRGBArray(CAMERA)

    time.sleep(0.1)

    CAMERA.capture(rawCapture, format="bgr")
    image = rawCapture.array()

    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(grayImage, 1.4) # gets the faces for this image

    # If face is detected, save that specific face
    for (x, y, w, h) in faces:
        croppedImage = grayImage[y: y + h, x: x + w] # crops it to be only the face

        tools.save_new_image(userId, croppedImage)

def take_fingerprint(enrollNumber):
    CONTROLLER.show_page("FingerprintEnroll") # TODO This screen does not yet exist, but it will 
    # (also, maybe seperating the enrolls could provide a better registration, but we'll cross that later)

    FINGERPRINT_SENSOR.enroll_person(enrollNumber)
