import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
from picamera.exc import PiCameraError

class Recogniser:
    def __init__(self):

        # inits camera
        try:
            self.camera = PiCamera()
            self.camera.rotation = 180
        except (NameError, PiCameraError):
            pass

        # inits misc stuff for authentication
        try:
            self.face_recogniser = cv2.face.LBPHFaceRecognizer_create()

            self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        except (NameError, AttributeError):
            print("Could not load CV2, Prepare for errors...")


    def get_photograph(self):
        '''takes a photo and formats it for the login attempt'''
        # makes a RGB array reference to the camera (to be more efficient not having to convert between jpeg and arrays)
        rawCapture = PiRGBArray(self.camera)

        time.sleep(0.1) # gives time for the init

        self.capture(rawCapture, format="bgr") # captures the photo
        image = rawCapture.array # turns it straight into a nice array

        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # returns the grayscale version
