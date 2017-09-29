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
        locked_lbl.grid(row = 1, column = 1, padx = 380, pady = 100)
        
        submit_button = Button(root, text = "Submit")
        submit_button.grid(row = 2, column = 1)

        print("Locked Screen Initialised.")


class verificationScreen(Frame):
    def __init__(self, root=None):
        frame = Frame.__init__(self, root)
        self.width = 800
        self.height = 460
        self.grid()
        self.master.title("Template as this will be fullscreen.")

        photoData = PhotoImage(file="C:/Users/bhuvan21/Desktop/gui/facialrecog.gif")
        place_face_here = Label(image = photoData)
        place_face_here.image = photoData
        place_face_here.grid(row = 1, column = 1, padx = 10)
        
        photoData = PhotoImage(file="C:/Users/bhuvan21/Desktop/gui/placeholder.gif")
        place_face_here = Label(image = photoData)
        place_face_here.image = photoData
        place_face_here.grid(row = 1, column = 2, padx = 10)

        info = Label(root, text = "Pls do a good thing.", bg = "white")
        info.grid(row = 1, column = 3, padx = 10)

        take_photo_button = Button(text = "Take Photo")
        take_photo_button.grid(row = 2, column = 2, pady = 30)


class hudScreen(Frame):
    def __init__(self, root=None):
        frame = Frame.__init__(self, root)
        self.width = 800
        self.height = 460
        self.grid()
        self.master.title("Template as this will be fullscreen.")
        crackers = {}
        
        photoData = PhotoImage(file="C:/Users/bhuvan21/Desktop/gui/personpic.gif")
        place_face_here = Label(image = photoData)
        place_face_here.image = photoData
        place_face_here.grid(row = 2, column = 1, padx = 20)

        info = Label(root, text = "Yeeto Burrito.", bg = "white")
        info.grid(row = 2, column = 2, padx = 10)

        lock_button = Button(text = "Lock")
        lock_button.grid(row = 1, column = 3, padx = 430, pady = 20)

        dispense_button = Button(text = "Dispense")
        dispense_button.grid(row = 3, column = 1, padx = 20, pady = 20)

        refill_button = Button(text = "Refill")
        refill_button.grid(row = 3, column = 2, padx = 20, pady = 20)

        photoData = PhotoImage(file="C:/Users/bhuvan21/Desktop/gui/cracker.gif")
        crackers = Label(image = photoData)
        crackers.image = photoData
        crackers.grid(row = 2, column = 3, padx = 20)
            
        
#locked = lockedScreen(root)
#verify = verificationScreen(root)
hud = hudScreen(root)




mainloop()
