import time
import tkinter as tk

from settings import FACE_RECOGNISER
import gui
import tools

time.sleep(2) # allows time for the camera to set up for the first time

tools.do_training() # train the recogniser

# init the root window
root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(800, 460))
root.configure(background='white')

window = gui.HudScreen(root)

root.mainloop()
