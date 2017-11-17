import time

from settings import SYSTEM_DATA, FINGERPRINT_SENSOR, REGISTER_QUEUE
from rational_gui.controller import CONTROLLER

import authenticate
import register
import tools

# ////////////////////////////////// #
# Functions for authenticating users #
# ////////////////////////////////// #

def login_button_func():
    user, conf = authenticate.authenticate_face()

    if not user or conf > SYSTEM_DATA['fingerprintConf']:
        CONTROLLER.show_page("FingerprintScreen")
    else:
        CONTROLLER.show_page("HudScreen", user)

def fingerprint_verif_func(user):

    verif = FINGERPRINT_SENSOR.verify_person(user-1)

    if verif:
        CONTROLLER.show_page("HudScreen", user)
    elif verif is None:
        CONTROLLER.after(500, fingerprint_verif_func)
    else:
        CONTROLLER.show_page("LockedScreen",
                             {'notification':'Login attempt failed, please try again. View the help page for more info.'})

# /////////////////////////////// #
# Functions for registering users #
# /////////////////////////////// #

def register_user(newUserName):
    newUser = next(a for a, b in enumerate(sorted(list(SYSTEM_DATA['userDict'].keys())), 1) if a != b)

    if newUser > 20 or newUserName in SYSTEM_DATA['userDict'].values() or newUserName == "":
        REGISTER_QUEUE.put(False)
        return False

    SYSTEM_DATA['userDict'][newUser] = newUserName

    CONTROLLER.show_page("FaceEnroll") # TODO

    for i in range(10): # 10 is arbitrary, this is up for change

        # say some tkinter thing about getting ready (and maybe a countdown) and looking SLIGHTLY different each time

        register.take_registration_photo(newUser) # take and save the picture

        time.sleep(2) # wait a bit
    
    CONTROLLER.show_page("FingerprintEnroll") # TODO This screen does not yet exist, but it will

    FINGERPRINT_SENSOR.enroll_person(newUser-1) # -1 because they start at 0

    SYSTEM_DATA.save()

    tools.update() # retrain

    REGISTER_QUEUE.put(True)
    return True
