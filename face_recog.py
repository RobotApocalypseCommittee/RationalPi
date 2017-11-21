try:
    import cv2
except:
    print("CV2 Not Installed")
try:
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    from picamera.exc import PiCameraError
except ImportError:
    print("PiCamera Not Installed")
import os
import time

import numpy as np

import tools
from settings import SYSTEM_DATA


class FaceManager:
    def __init__(self):

        # inits camera
        try:
            self.camera = PiCamera()
            self.camera.rotation = 180
        except (NameError, PiCameraError) as e:
            print("CAMERA ERROR: " + str(e))
            pass

        # inits misc stuff for authentication
        try:
            self.face_recogniser = cv2.face.LBPHFaceRecognizer_create()

            self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        except (NameError, AttributeError):
            print("Could not load CV2, Prepare for errors...")

        self.trained_files = []

    def update(self):
        faceImages, faceIdList, faceFileNames = self.get_face_data() # gets the data

        self.face_recogniser.update(faceImages, np.array(faceIdList)) # does the updating

        self.trained_files.extend(faceFileNames)

    def get_face_data(self): # gets faces in the Face Storage folder and returns the faces and their ids
        faceImages = []
        faceIdList = []
        faceFileNames = []

        # gets all of the paths for the images
        image_paths = [
            'Face Storage/' + incomplete_image_path # adds the folder name to the path (to make the path work within the python file)
            for incomplete_image_path in os.listdir('Face Storage/') # for every photo in the Face Storage folder, get its name
            ]

        for image_path in image_paths:

            if image_path in self.trained_files:
                continue

            faceFileNames.append(image_path)

            # get the image and grayscale it (to make the numpy array work nicely)
            colorImage = cv2.imread(image_path)
            grayImage = cv2.cvtColor(colorImage, cv2.COLOR_BGR2GRAY) # Definitely needed (for some reason)

            faces = self.face_cascade.detectMultiScale(grayImage, 1.4)

            for (x, y, w, h) in faces:
                croppedImage = grayImage[y: y + h, x: x + w] # crops it to be only the face

                # Get the faceId of the image
                faceId = os.path.split(image_path)[1].split('.')[0]
                print(faceId)

                faceImages.append(croppedImage)
                faceIdList.append(int(faceId))

        # return the images list and labels list
        return faceImages, faceIdList, faceFileNames

    def load(self, filename):
        self.face_recogniser.read(filename)

    def train(self):
        faceImages, faceIdList, faceFileNames = self.get_face_data() # gets the data

        self.face_recogniser.train(faceImages, np.array(faceIdList)) # does the training

        print("Generating recog.xml")
        self.face_recogniser.write("recog.xml")
        
        self.trained_files.extend(faceFileNames)


    def get_photograph(self):
        '''takes a photo and formats it for the login attempt'''
        # makes a RGB array reference to the camera (to be more efficient not having to convert between jpeg and arrays)
        rawCapture = PiRGBArray(self.camera)

        time.sleep(0.1) # gives time for the init

        self.camera.capture(rawCapture, format="bgr") # captures the photo
        image = rawCapture.array # turns it straight into a nice array

        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # returns the grayscale version

    def authenticate(self):
        grayImageArray = self.get_photograph() # takes the photo

        faceList = self.face_cascade.detectMultiScale(grayImageArray, 1.4) # finds the faces

        id_list_confs = {} # starts the id dict (id:confidence)
        photo_dict = {} # starts the photo dict (id:photo array)

        for (x, y, w, h) in faceList: # for every face
            id_predicted, conf = self.face_recogniser.predict(grayImageArray[y: y + h, x: x + w]) # get the predidcted id and its confidence

            #cv2.imshow("Analysing face...", grayImageArray[y: y + h, x: x + w]) # look nice
            cv2.waitKey(20) # wait for a bit

            if conf > SYSTEM_DATA['confThreshold']: # if unconfident, put the confidence into the 0 key of the dict
                id_list_confs[0] = conf
            else: # else put the conficence in that user's id key in the dict (i.e. for person with id 5 and a face of confidence 15, it would look like 5:15)
                id_list_confs[id_predicted] = conf
                photo_dict[id_predicted] = grayImageArray[y: y + h, x: x + w]

        if np.any(faceList): # if there were any faces, return the id of the prediction with the lowest confidence (low confidence means it is very confident)
            winningKey = min(id_list_confs, key=id_list_confs.get)

            if id_list_confs[winningKey] < SYSTEM_DATA['saveImageConf']:
                tools.save_new_image(winningKey, photo_dict[winningKey])
                self.update()

            return winningKey, id_list_confs[winningKey]
        else: # otherwise, return 0 (no faces, unidentified)
            return False, 1000

FACE_MANAGER = FaceManager()

if __name__ == "__main__":
    FACE_MANAGER.train()
