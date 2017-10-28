import time

from settings import SYSTEM_DATA, FINGERPRINT_SENSOR
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
    else:
        CONTROLLER.show_page("LockedScreen", {'notification':'Login attempt failed, please try again. View the help page for more info.'})

# /////////////////////////////// #
# Functions for registering users #
# /////////////////////////////// #

def register_user():
    newUser = next(a for a, b in enumerate(sorted(list(SYSTEM_DATA['userDict'].keys())), 1) if a != b)

    if newUser > 20:
        # TODO some error pop up box on tkinter, but either way, this fails
        return

    # ask for input somehow (I CANNOT do this now)
    newUserName = input('What would you like to be called? ')

    SYSTEM_DATA['userDict'][newUser] = newUserName

    for i in range(8): # 8 is arbitrary, this is up for change
        # say some tkinter thing about getting ready (and maybe a countdown) and looking SLIGHTLY different each time

        register.take_registration_photo(newUser) # take and save the picture

        time.sleep(1) # wait a bit
    
    register.take_fingerprint(newUser-1) # -1 because they start at 0

    SYSTEM_DATA.save()

    tools.update() # retrain
