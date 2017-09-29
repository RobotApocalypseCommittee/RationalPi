'''All the functions for validating users.'''

# imports!
import os
import time

import cv2
import numpy as np
from picamera import PiCamera
from picamera.array import PiRGBArray
from PIL import Image

SAVE_IMAGE_CONF = 15

# sets path to the xml cascade which finds hwere the faces actually are
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

def take_login_photo(): # takes a photo and formats it for the login attempt
    # inits the camera and makes a RGB array reference to it (to be more efficient not having to convert between jpeg and arrays)
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)

    time.sleep(0.1) # gives time for the init

    camera.capture(rawCapture, format="bgr") # captures the photo
    image = rawCapture.array() # turns it straight into a nice array

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # returns the grayscale version

def authenticate_face(recogniser): # returns the (predicted) user id from a face (0 means unidentified)
    grayImageArray = take_login_photo() # takes the photo

    faceList = faceCascade.detectMultiScale(grayImageArray, 1.4) # finds the faces

    id_list_confs = {} # starts the id dict (id:confidence)
    photo_dict = {} # starts tho photo dict (id:photo array)

    for (x, y, w, h) in faces: # for every face
        id_predicted, conf = recognizer.predict(grayImageArray[y: y + h, x: x + w]) # get the predidcted id and its confidence
            
        cv2.imshow("Analysing face...", predict_image[y: y + h, x: x + w]) # look nice
        cv2.waitKey(20) # wait for a bit

        if conf > 50: # if unconfident, put the confidence into the 0 key of the dict
            id_list_confs[0] = conf
        else: # else put the conficence in that user's id key in the dict (i.e. for person with id 5 and a face of confidence 15, it would look like 5:15)
            id_list_confs[id_predicted] = conf
            photo_dict[id_predicted] = grayImageArray[y: y + h, x: x + w]

    if len(faces): # if there were any faces, return the id of the prediction with the lowest confidence (low confidence means it is very confident)
        winningKey = min(id_list_confs, key=id_list_confs.get)

        if id_list_confs[winningKey] < SAVE_IMAGE_CONF:
            save_new_image(winningKey, photo_dict[winningKey])
        
        return winningKey, id_list_confs[winningKey]
    else: # otherwise, return 0 (no faces, unidentified)
        return 0