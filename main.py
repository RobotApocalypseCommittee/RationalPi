import json
import time
import tkinter as tk

import cv2

import authenticate
import register
import tools
from picamera import PiCamera

FINGERPRINT_CONF = 15

class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.button = tk.Button(frame,
                                text="QUIT", fg="red",
                                command=quit)
        self.button.pack(side=tk.LEFT)

        self.slogan = tk.Button(frame,
                                text="Hello",
                                command=self.write_slogan)
        self.slogan.pack(side=tk.LEFT)

        self.auth = tk.Button(frame,
                              text='Authenticate',
                              command=self.authenticate_user)
        self.auth.pack(side=tk.BOTTOM)

    @staticmethod
    def write_slogan():
        print("Tkinter is easy to use!")

    @staticmethod
    def authenticate_user():
        user, conf = authenticate.authenticate_face(FACE_RECOGNISER, CAMERA)

        if conf > FINGERPRINT_CONF:
            result = authenticate.authenticate_fingerprint(user)

    @staticmethod
    def register_user():
        highestUser = max(userDict)

        newUser = highestUser + 1

        # ask for input somehow (I CANNOT do this now)
        newUserName = input('What would you like to be called? ')

        userDict[newUser] = newUserName

        for i in range(8): # 8 is arbitrary, this is up for change
            # say some tkinter thing about getting ready (and maybe a countdown) and looking SLIGHTLY different each time

            register.take_registration_photo(newUser, CAMERA) # take and save the picture

            time.sleep(1) # wait a bit

        with open('user_data.json', 'w') as userFile: # update the json file
            json.dump(userDict, userFile)

        tools.do_training(FACE_RECOGNISER) # retrain

CAMERA = PiCamera()
CAMERA.rotation = 180
time.sleep(2)

with open('user_data.json', 'r') as userFile:
    userDict = json.load(userFile)
    userDict = {int(key):val for key, val in userDict.items()}

FACE_RECOGNISER = cv2.face.LBPHFaceRecognizer_create() # create the recogniser
tools.do_training(FACE_RECOGNISER) # train it

root = tk.Tk()

root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)
app = App(root)


root.mainloop()
