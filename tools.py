import os

import cv2
import numpy as np
from PIL import Image

from settings import FACE_RECOGNISER, FACE_CASCADE

def get_face_data(): # gets faces in the Face Storage folder and returns the faces and their ids
    faceImages = []
    faceIdList = []

    # gets all of the paths for the images
    image_paths = [
        'Face Storage/' + incomplete_image_path # adds the folder name to the path (to make the path work within the python file)
        for incomplete_image_path in os.listdir('Face Storage/') # for every photo in the Face Storage folder, get its name
        ]

    for image_path in image_paths:
        # get the image and grayscale it (to make the numpy array work nicely)
        colorImage = cv2.imread(image_path)
        image = cv2.cvtColor(colorImage, cv2.COLOR_BGR2GRAY) # Definitely needed (for some reason)

        # Get the faceId of the image
        faceId = os.path.split(image_path)[1].split('.')[0]
        print(faceId)

        faceList = FACE_CASCADE.detectMultiScale(image, 1.4)

        for (x, y, w, h) in faceList:
            realImage = image[y: y + h, x: x + w]

            faceImages.append(realImage)
            faceIdList.append(int(faceId))

    # return the images list and labels list
    return faceImages, faceIdList

def do_training(): # trains the recogniser (done at startup)
    faceImages, faceIdList = get_face_data() # gets the data

    FACE_RECOGNISER.train(faceImages, np.array(faceIdList)) # does the training

def update(): # TODO
    return

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
