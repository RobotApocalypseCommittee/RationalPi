import time

import cv2

import tools
from picamera.array import PiRGBArray

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

def take_registration_photo(userId, camera): # takes and saves ONE of a user's registration photos
    # see line 50 onwards
    rawCapture = PiRGBArray(camera)

    time.sleep(0.1)

    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array()

    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(grayImage, 1.4) # gets the faces for this image

    # If face is detected, save that specific face
    for (x, y, w, h) in faces:
        croppedImage = grayImage[y: y + h, x: x + w] # crops it to be only the face

        tools.save_new_image(userId, croppedImage)