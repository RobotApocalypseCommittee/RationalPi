'''All the functions for rationing/tracking crackers.'''

from settings import CRACKERS_LEFT

def dispense_cracker(user):
    '''Main command for dispensing a cracker'''

    if CRACKERS_LEFT == 0:
        return False

    # TODO