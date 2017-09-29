import json
import time
import tkinter as tk

import authenticate
import register
import tools

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
    
    def write_slogan(self):
        print("Tkinter is easy to use!")

    def authenticate_user(self):
        user, conf = authenticate.authenticate_face(face_recogniser)

        if conf > FINGERPRINT_CONF:
            result = authenticate.authenticate_fingerprint(user)

    def register_user(self):
        highestUser = max(userDict)

        newUser = highestUser + 1

        # ask for input somehow (I CANNOT do this now)
        newUserName = input('What would you like to be called? ')

        userDict[newUser] = newUserName

        for i in range(8): # 8 is arbitrary, this is up for change
            # say some tkinter thing about getting ready (and maybe a countdown) and looking SLIGHTLY different each time

            register.take_registration_photo(newUser) # take and save the picture

            time.sleep(1) # wait a bit

        with open('user_data.json', 'w') as userFile: # update the json file
            json.dump(userDict, userFile)
        
        authenticate.do_training(face_recognizer) # retrain

with open('user_data.json', 'r') as userFile:
    userDict = json.load(userFile)
    userDict = {int(key):val for key,val in userDict.items()}

face_recognizer = cv2.face.LBPHFaceRecognizer_create() # create the recogniser
tools.do_training(face_recogniser) # train it

root = tk.Tk()

root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
app = App(root)


root.mainloop()
