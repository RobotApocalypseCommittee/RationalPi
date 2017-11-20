'''All the functions for rationing/tracking crackers.'''
from datetime import datetime

from settings import SYSTEM_DATA

def can_dispense_cracker(user):
    '''Main command for dispensing a cracker'''

    if SYSTEM_DATA['crackersLeft'] == 0:
        return False

    lastCracker = datetime.strptime(SYSTEM_DATA['userDict'][user]["lastCracker"], "%Y-%m-%dT%H:%M:%S")
    if lastCracker + datetime.timedelta(hours=12) > datetime.today():
        return False

    return True

def update_cracker_data(user):
    SYSTEM_DATA['crackersLeft'] -= 1

    timeNow = datetime.today().strftime("%Y-%m-%dT%H:%M:%S")
    SYSTEM_DATA['userDict'][user]["lastCracker"] = timeNow

    SYSTEM_DATA.save()