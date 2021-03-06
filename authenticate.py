from face_recog import FACE_MANAGER
from settings import SYSTEM_DATA, FINGERPRINT_SENSOR

def authenticate_face():
    user, conf = FACE_MANAGER.authenticate()
    print("User = " + str(user) + " Conf = " + str(conf))
    if not user:
        return False, None
    elif conf > SYSTEM_DATA['fingerprintConf']:
        return False, user
    else:
        return True, user

def authenticate_finger():
    resp = FINGERPRINT_SENSOR.identify_person()
    if resp == None:
        return False, None
    else:
        return True, resp+1

def verif_finger(user):
    resp = FINGERPRINT_SENSOR.verify_person(user-1)
    
    return resp