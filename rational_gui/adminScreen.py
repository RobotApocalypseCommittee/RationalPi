import tkinter as tk
import threading
import queue

from rational_gui.images import get_imagepath
from rational_gui.page import Page
from controller import CONTROLLER
from settings import REGISTER_QUEUE

try:
    import tkinter_funcs
except ImportError:
    pass

#locked screen class
class AdminScreen(Page):
    def __init__(self, parent):
        #setup things
        super().__init__(parent)

        adminBg = tk.PhotoImage(file=get_imagepath("adminBg")) # TODO
        registerButtonImage = tk.PhotoImage(file=get_imagepath("registerButton")) # TODO

        self.width = 800
        self.height = 480
        self.grid()

        #background things
        bg_lbl = tk.Label(self, image=adminBg)
        bg_lbl.image = adminBg
        bg_lbl.place(x=-2, y=-2)

        #textinput thing
        self.name_strvar = tk.StringVar()
        name_input = tk.Entry(self, width=30, textvariable=self.name_strvar)
        name_input.grid(row=0, column=0)

        #register button things
        register_button = tk.Button(self, image=registerButtonImage, command=self.handleRegister,
                                    bg="black", activebackground="black", bd=0, highlightthickness=0)

        register_button.image = registerButtonImage
        register_button.grid(row=1, column=0)
        
        print("Admin screen opened")

    def handleRegister(self):
        name = self.name_strvar.get()

        registerThread = threading.Thread(None, lambda name=name: tkinter_funcs.register_user(name))
        registerThread.start()

        self.checkFinish(registerThread)
        
    def checkFinish(self, thread):
        if thread.is_alive():
            CONTROLLER.after(500, lambda thread=thread: self.checkFinish(thread))
        else:
            try:
                resp = REGISTER_QUEUE.get(block=False)
            except queue.Empty:
                resp = False

            if not resp:
                print("WARNING, REGISTRATION SOMEHOW FAILED")

            CONTROLLER.show_page("LockedScreen")