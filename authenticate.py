'''All the functions for validating users.'''

# imports!
import os
import time

import cv2
import numpy as np
from PIL import Image

from picamera import PiCamera
from picamera.array import PiRGBArray

# sets path to the xml cascade which finds hwere the faces actually are
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

def get_face_data(): # gets faces in the Face Storage folder and returns the faces and their ids
    images = [] 
    labels = []

    # gets all of the paths for the images
    image_paths = [
        'Face Storage\\' + incomplete_image_path # adds the folder name to the path (to make the path work within the python file)
        for incomplete_image_path in os.listdir('Face Storage') # for every photo in the Face Storage folder, get its name
        ]
    
    for image_path in image_paths:
        # get the image and grayscale it (to make the numpy array work nicely)
        colorImage = cv2.imread(image_path)
        image = cv2.cvtColor(colorImage, cv2.COLOR_BGR2GRAY) # Definitely needed (for some reason)
        
        # Get the faceId of the image
        faceId = os.path.split(image_path)[1].split('.')[0]

        faceImages.append(image)
        faceIdList.append(faceId)

    # return the images list and labels list
    return faceImages, faceIdList

def do_training(recogniser): # trains the recogniser (done at startup, after a registration and every few mins)
    faceImages, faceIdList = get_face_data() # gets the data

    recognizer.train(faceImages, np.array(faceIdList)) # does the training

def take_login_photo(): # takes a photo and formats it for the login attempt
    # inits the camera and makes a RGB array reference to it (to be more efficient not having to convert between jpeg and arrays)
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)

    time.sleep(0.1) # gives time for the init

    camera.capture(rawCapture, format="bgr") # captures the photo
    image = rawCapture.array() # turns it straight into a nice array

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # returns the grayscale version

def save_new_image(userId, faceImage):
    # Gets the highest version number of the user's photo
    try:
        highestVersion = max(
            [
                int(filename.split('.')[1]) # turns the part that is the version into an int
                for filename in os.listdir('Face Storage') # gets all of the files in the folder
                if filename.startswith(str(userId)) # but only if they start with our user's user id
            ]
            ) # and so gets the maximum of these
    except ValueError: # if this is the first photo then make -1 the lowest photo (so 1.0 is the first)
        highestVersion = -1

    Image.fromarray(faceImage).save('Face Storage\\{}.{}.jpg'.format(userId, highestVersion+1))

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

        if id_list_confs[winningKey] < 15:
            save_new_image(winningKey, photo_dict[winningKey])
        
        return winningKey
    else: # otherwise, return 0 (no faces, unidentified)
        return 0

def take_registration_photo(userId): # takes and saves ONE of a user's registration photos
    camera = PiCamera() # see line 50 onwards
    rawCapture = PiRGBArray(camera)

    time.sleep(0.1)

    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array()

    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(grayImage, 1.4) # gets the faces for this image

    # If face is detected, save that specific face
    for (x, y, w, h) in faces:
        croppedImage = grayImage[y: y + h, x: x + w] # crops it to be only the face

        save_new_image(userId, croppedImage)