import tkinter as tk

from rational_gui.images import get_imagepath
from rational_gui.page import Page

try:
    import tkinter_funcs
except ImportError:
    pass

#verification class
class VerificationScreen(Page):
    def __init__(self, parent):
        #basic setup things
        super(VerificationScreen, self).__init__(parent)
        self.width = 800
        self.height = 460
        self.grid()

        verificationBg = tk.PhotoImage(file=get_imagepath("verificationBg"))
        face_outline = tk.PhotoImage(file=get_imagepath("positionFace"))
        placeholder = tk.PhotoImage(file=get_imagepath("placeholder"))
        instructions = tk.PhotoImage(file=get_imagepath("instructions"))
        self.take_photo_img = tk.PhotoImage(file=get_imagepath("newCamera"))

        #background things
        bg_lbl = tk.Label(self, image=verificationBg)
        bg_lbl.image = verificationBg
        bg_lbl.place(x=-2, y=-2)
        
        #face guidance image
        place_face_here = tk.Label(self, image=face_outline, borderwidth=0)
        place_face_here.image = face_outline
        place_face_here.place(x=10, y=170)

        #picam placeholder image
        placeholder_lbl = tk.Label(self, image=placeholder, borderwidth=0)
        placeholder_lbl.image = placeholder
        placeholder_lbl.place(x=304, y=170)

        #instructions image
        instructions_lbl = tk.Label(self, image=instructions, borderwidth=0)
        instructions_lbl.image = instructions
        instructions_lbl.place(x=646, y=170)

        #take photo image
        try:
            take_photo_button = tk.Button(self, command=tkinter_funcs.authenticate_user, image=self.take_photo_img, bg="black", activebackground="black", bd=0, highlightthickness = 0)
        except NameError:
            take_photo_button = tk.Button(self, command=lambda: print('noot'), image=self.take_photo_img, bg="black", activebackground="black", bd=0)
        take_photo_button.place(x=350, y=368)