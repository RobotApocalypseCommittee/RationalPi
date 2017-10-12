import time
import json

from settings import FINGERPRINT_CONF, USER_DICT, FINGERPRINT_SENSOR
from rational_gui.controller import CONTROLLER
import authenticate
import register
import tools

# ////////////////////////////////// #
# Functions for authenticating users #
# ////////////////////////////////// #

def login_button_func():
    user, conf = authenticate.authenticate_face()

    if not user or conf > FINGERPRINT_CONF:
        CONTROLLER.show_page("FingerprintScreen")
    else:
        CONTROLLER.show_page("HudScreen", user)

def fingerprint_verif_func(user):

    verif = FINGERPRINT_SENSOR.verify_person(user-1)

    if verif:
        CONTROLLER.show_page("HudScreen", user)
    else:
        CONTROLLER.show_page("LockedScreen", {'notification':'Login attempt failed, please try again. View the help page for more info.'})

# /////////////////////////////// #
# Functions for registering users #
# /////////////////////////////// #

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
