'''For scanning fingerprint.'''
import tkinter as tk
import tkinter.font

from rational_gui.images import get_imagepath
from rational_gui.page import Page


class FingerprintScreen(Page):
    def __init__(self, parent, controller):
        super(FingerprintScreen, self).__init__(parent, controller)
        self.width = 800
        self.height = 460
        self.grid()


        verificationBg = tk.PhotoImage(file=get_imagepath("verificationScreen"))

        #background things
        bg_lbl = tk.Label(self, image=verificationBg)
        bg_lbl.image = verificationBg
        bg_lbl.place(x=0, y=0)
        info_label = tk.Label(self, font=("Helvetica", 16), text="Your face was not good enough. Please place your finger on the scanner.",
            wraplength=200)
        info_label.grid(row=0, column=0, padx=500, pady=150)