import tkinter as tk

from rational_gui.images import get_imagepath
from rational_gui.page import Page

#import tkinter_funcs

#locked screen class
class LockedScreen(Page):
    def __init__(self, parent, controller):
        #setup things
        super().__init__(parent, controller)

        lockedBg = tk.PhotoImage(file=get_imagepath("lockedScreen"))
        lockedButton = tk.PhotoImage(file=get_imagepath("unlockTest"))

        self.width = 800
        self.height = 460
        self.grid()

        #background things
        bg_lbl = tk.Label(self, image=lockedBg)
        bg_lbl.image = lockedBg
        bg_lbl.place(x=0, y=0)

        #submit button things
        submit_button = tk.Button(self, image=lockedButton, command=lambda: controller.show_page("VerificationScreen"), bg="black", activebackground="black", bd=0)
        submit_button.image = lockedButton
        submit_button.grid(row=1, column=1, padx=322, pady=142)
        
        print("Locked Screen Initialised")
