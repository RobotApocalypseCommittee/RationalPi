import tkinter as tk

from rational_gui.controller import CONTROLLER
from rational_gui.images import get_imagepath
from rational_gui.page import Page

#dispense screen class
class DispenseScreen(Page):
    def __init__(self, parent):
        #setup things
        super().__init__(parent)

        dispenseBg = tk.PhotoImage(file=get_imagepath("dispenseScreen"))
        #lockedButton = tk.PhotoImage(file=get_imagepath("unlockTest"))

        self.width = 800
        self.height = 480
        self.grid()

        #background things
        bg_lbl = tk.Label(self, image=dispenseBg)
        bg_lbl.image = dispenseBg
        bg_lbl.place(x=-2, y=-2)

       
        
        print("Dispense Screen Initialised")
