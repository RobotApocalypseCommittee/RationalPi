from tkinter import *

root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(800, 460))
root.configure(background='white')


class lockedScreen(Frame):
    def __init__(self, root=None):
        frame = Frame.__init__(self, root)
        self.width = 800
        self.height = 460
        self.grid()
        self.master.title("Template as this will be fullscreen.")
        locked_lbl = Label(root, text = "LOCKED", bg = "white")
        locked_lbl.grid(row = 1, column = 1, sticky = E)
        


        
        print("Locked Screen Initialised.")





locked = lockedScreen(root)
locked.pack()





mainloop()
