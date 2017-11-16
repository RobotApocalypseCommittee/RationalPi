import tkinter as tk

from rational_gui.images import get_imagepath
from rational_gui.page import Page

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
        resp = tkinter_funcs.register_user(self.name_strvar.get())
        if not resp:
            errorRoot = tk.Tk()
            errorRoot.wm_title('Error')

            errorFrame = tk.Frame(errorRoot)
            errorFrame.pack()

            errorLabel = tk.Label(errorFrame, text="Error, registering failed", fg='red')
            errorLabel.grid(row=0, column=0)

            errorButton = tk.Button(errorFrame, text='Ok', command=errorRoot.destroy)
            errorButton.grid(row=1, column=0)

            errorRoot.mainloop()
