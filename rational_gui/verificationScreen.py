import tkinter as tk

from rational_gui.images import get_imagepath
from rational_gui.page import Page

import tkinter_funcs


#verification class
class VerificationScreen(Page):
    def __init__(self, parent, controller):
        #basic setup things
        super(VerificationScreen, self).__init__(parent, controller)
        self.width = 800
        self.height = 460
        self.grid()

        verificationBg = tk.PhotoImage(file=get_imagepath("verificationScreen"))
        face_outline = tk.PhotoImage(file=get_imagepath("outline"))
        placeholder = tk.PhotoImage(file=get_imagepath("placeholder"))
        instructions = tk.PhotoImage(file=get_imagepath("instructions"))
        self.take_photo_img = tk.PhotoImage(file=get_imagepath("camera"))

        #background things
        bg_lbl = tk.Label(self, image=verificationBg)
        bg_lbl.image = verificationBg
        bg_lbl.place(x=0, y=0)
        
        #face guidance image
        place_face_here = tk.Label(self, image=face_outline)
        place_face_here.image = face_outline
        place_face_here.grid(row=1, column=1, padx=10, pady=140)

        #picam placeholder image
        placeholder_lbl = tk.Label(self, image=placeholder)
        placeholder_lbl.image = placeholder
        placeholder_lbl.grid(row=1, column=2, padx=100)

        #instructions image
        instructions_lbl = tk.Label(self, image=instructions)
        instructions_lbl.image = instructions
        instructions_lbl.grid(row=1, column=3, padx=10, pady=0)

        #take photo image
        take_photo_button = tk.Button(self, command=self.handle_authenticate, image=self.take_photo_img, bg="blue", activebackground="red", bd=0)
        take_photo_button.place(x=330, y=320)

    def handle_authenticate(self):
        user = tkinter_funcs.authenticate_user()

        if not user:
            self.controller.show_page("FingerprintScreen")
        else:
            self.controller.show_page("HudScreen", user)