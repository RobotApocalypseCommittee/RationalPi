from tkinter import *

#verification class
class VerificationScreen(Frame):
    def __init__(self, root=None):
        #basic setup things
        frame = Frame.__init__(self, root)
        self.width = 800
        self.height = 460
        self.grid()
        self.master.title("Template as this will be fullscreen")

        #background things
        bg_lbl = Label(root, image=verificationBg)
        bg_lbl.image = verificationBg
        bg_lbl.place(x=0, y=0)
        
        #face guidance image
        place_face_here = Label(image=face_outline)
        place_face_here.image = face_outline
        place_face_here.grid(row=1, column=1, padx=10, pady=140)

        #picam placeholder image
        placeholder_lbl = Label(image=placeholder)
        placeholder_lbl.image = placeholder
        placeholder_lbl.grid(row=1, column=2, padx=100)

        #instructions image
        instructions_lbl = Label(image=instructions)
        instructions_lbl.image = instructions
        instructions_lbl.grid(row=1, column=3, padx=10, pady=0)

        #take photo image
        take_photo_button = Button(root, image=take_photo, command=test, bg="blue", activebackground="red", bd=0)
        take_photo_button.place(x=330, y=320)

