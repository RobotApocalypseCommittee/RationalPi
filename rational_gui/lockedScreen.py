from tkinter import *

#locked screen class
class LockedScreen(Frame):
    def __init__(self, root=None):
        #setup things
        frame = Frame.__init__(self, root)
        self.width = 800
        self.height = 460
        self.grid()
        self.master.title("Template as this will be fullscreen")

        #background things
        bg_lbl = Label(root, image=lockedBg)
        bg_lbl.image = lockedBg
        bg_lbl.place(x=0, y=0)

        #submit button things
        submit_button = Button(root, image=lockedButton, command=tkinter_funcs.login_button_func, bg="black", activebackground="black", bd=0)
        submit_button.grid(row=1, column=1, padx=322, pady=142)
        
        print("Locked Screen Initialised")