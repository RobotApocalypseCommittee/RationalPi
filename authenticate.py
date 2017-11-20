from face_recog import FACE_MANAGER
from settings import SYSTEM_DATA

def authenticate_face():
    user, conf = FACE_MANAGER.authenticate()
    print("User = " + str(user) + " Conf = " + str(conf))
    if not user or conf > SYSTEM_DATA['fingerprintConf']:
        return False, 'noot'
    else:
        return True, user