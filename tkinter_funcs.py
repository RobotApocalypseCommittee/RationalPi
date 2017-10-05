import time
import json

from settings import FACE_RECOGNISER, FINGERPRINT_CONF, CAMERA, USER_DICT
import authenticate
import register
import tools

def authenticate_user():
    user, conf = authenticate.authenticate_face()

    if conf > FINGERPRINT_CONF:
        if not authenticate.authenticate_fingerprint(user):
            user = 0
    
    return user

def register_user():
    highestUser = max(USER_DICT)

    newUser = highestUser + 1

    # ask for input somehow (I CANNOT do this now)
    newUserName = input('What would you like to be called? ')

    USER_DICT[newUser] = newUserName

    for i in range(8): # 8 is arbitrary, this is up for change
        # say some tkinter thing about getting ready (and maybe a countdown) and looking SLIGHTLY different each time

        register.take_registration_photo(newUser) # take and save the picture

        time.sleep(1) # wait a bit

    with open('user_data.json', 'w') as userFile: # update the json file
        json.dump(USER_DICT, userFile)

    tools.update() # retrain
    