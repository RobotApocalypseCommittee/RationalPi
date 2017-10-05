import time
import tkinter as tk

from settings import FACE_RECOGNISER
import rational_gui.gui
import rational_gui.lockedScreen
import tools

time.sleep(2) # allows time for the camera to set up for the first time

tools.do_training() # train the recogniser

# init the root window
root = tk.Tk()
rational_gui.gui.init_photos()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(800, 460))
root.configure(background='white')

window = rational_gui.lockedScreen.LockedScreen(root)

root.mainloop()
