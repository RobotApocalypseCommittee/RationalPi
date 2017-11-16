'''For scanning fingerprint.'''
import tkinter as tk
import tkinter.font

from rational_gui.images import get_imagepath
from rational_gui.page import Page
from rational_gui.controller import CONTROLLER
try:
    from tkinter_funcs import fingerprint_verif_func
except ImportError:
    fingerprint_verif_func = print
    pass


class FingerprintScreen(Page):
    def __init__(self, parent):
        super(FingerprintScreen, self).__init__(parent)
        self.width = 800
        self.height = 480
        self.grid()


        verificationBg = tk.PhotoImage(file=get_imagepath("verificationBg"))

        #background things
        bg_lbl = tk.Label(self, image=verificationBg)
        bg_lbl.image = verificationBg
        bg_lbl.place(x=0, y=0)
        info_label = tk.Label(self, font=("Helvetica", 16), text="Your face has been recognised and you must now present your finger.",
            wraplength=200)
        info_label.grid(row=0, column=0, padx=500, pady=150)

        CONTROLLER.after(0, fingerprint_verif_func)