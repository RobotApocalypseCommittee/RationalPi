import os

import cv2
import numpy as np
from PIL import Image




def save_new_image(userId, faceImage):
    # Gets the highest version number of the user's photo
    try:
        highestVersion = max(
            [
                int(filename.split('.')[1]) # turns the part that is the version into an int
                for filename in os.listdir('Face Storage') # gets all of the files in the folder
                if filename.startswith(str(userId)) # but only if they start with our user's user id
            ]
            ) # and so gets the maximum of these
    except ValueError: # if this is the first photo then make -1 the lowest photo (so 1.0 is the first)
        highestVersion = -1

    Image.fromarray(faceImage).save('Face Storage\\{}.{}.jpg'.format(userId, highestVersion+1))

