'''All the functions for rationing/tracking crackers.'''

from settings import SYSTEM_DATA

def dispense_cracker(user):
    '''Main command for dispensing a cracker'''

    if SYSTEM_DATA['crackersLeft'] == 0:
        return False

    # TODO