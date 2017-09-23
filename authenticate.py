'''All the functions for validating users.'''

import os
import cv2
import time
import numpy as np
from PIL import Image
from picamera.array import PiRGBArray
from picamera import PiCamera

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

def get_face_data():
    images = [] 
    labels = []

    image_paths = ['Face Storage\\' + incomplete_image_path for incomplete_image_path in os.listdir('Face Storage')]
    
    for image_path in image_paths:
        
        image_pil = Image.open(image_path).convert('L')
        
        image = np.array(image_pil, 'uint8')
        
        # Get the faceId of the image
        faceId = os.path.split(image_path)[1].split('user')[1]

        # Detect the face in the image
        faces = faceCascade.detectMultiScale(image, 1.4)

        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            faceImages.append(image[y: y + h, x: x + w])
            faceIdList.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(20)

    # clean up
    cv2.destroyAllWindows()

    # return the images list and labels list
    return faceImages, faceIdList

def do_training(recogniser):
    faceImages, faceIdList = get_face_data()

    recognizer.train(faceImages, np.array(faceIdList))

def take_login_photo():
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)

    time.sleep(0.1)

    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array()

    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

def authenticate_face(recogniser):
    grayImageArray = take_login_photo()

    faceList = faceCascade.detectMultiScale(grayImageArray, 1.4)

    id_list_confs = {}

    for (x, y, w, h) in faces:
        id_predicted, conf = recognizer.predict(grayImageArray[y: y + h, x: x + w])
            
        cv2.imshow("Analysing face...", predict_image[y: y + h, x: x + w])
        cv2.waitKey(20)

        if conf > 50:
            id_list[0] = conf
        else:
            id_list[id_predicted] = conf

    if len(faces):
        return min(d, key=d.get)
    else:
        return 0