from face_recog import FACE_MANAGER
from settings import SYSTEM_DATA, FINGERPRINT_SENSOR

def authenticate_face():
    user, conf = FACE_MANAGER.authenticate()
    print("User = " + str(user) + " Conf = " + str(conf))
    if not user or conf > SYSTEM_DATA['fingerprintConf']:
        return False, 'noot'
    else:
        return True, user#

def authenticate_finger():
    resp = FINGERPRINT_SENSOR.identify_person()
    if resp == None:
        return False, None
    else:
        return True, resp+1