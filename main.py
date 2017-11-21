'''A temporary file for testing the gui(since package relative paths are dodge)'''
import tkinter as tk

import tools
from rational_gui import pages
from rational_gui.controller import CONTROLLER
from face_recog import FACE_MANAGER

FACE_MANAGER.load("recog.xml")

for page in pages:
    try:
        CONTROLLER.add_page(page)
    except Exception as e:
        print("Could not start: {}".format(page.__name__))
        raise e


CONTROLLER.show_page("LockedScreen")
tk.mainloop()
