from tkinter import *

'''
BHUVAN, KEYWORD ASSIGNMENT ARGUMENTS DO NOT HAVE SPACES E.G.
x = 'cheese'
y = func(nooter=x)
NOT
y = func(nooter = x)
THANK YOU
'''

root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(800, 460))
root.configure(background='white')



FILEPATH = "images/"


def test():
    print("BOI PRESSED")


def initializePhotos():
    global lockedBg, lockedButton, facial_guidance, placeholder, verificationBg, face_outline, instructions, take_photo, person_pic, cracker_pic
    lockedBg = PhotoImage(file=FILEPATH+"lockedScreen.gif")
    lockedButton = PhotoImage(file=FILEPATH+"unlockTest.png")
    placeholder = PhotoImage(file=FILEPATH+"placeholder.gif")
    verificationBg = PhotoImage(file=FILEPATH+"verificationScreen.gif")
    face_outline = PhotoImage(file=FILEPATH+"outline.gif")
    instructions = PhotoImage(file=FILEPATH+"instructions.png")
    take_photo = PhotoImage(file=FILEPATH+"camera.png")
    person_pic = PhotoImage(file=FILEPATH+"personpic.gif")
    cracker_pic = PhotoImage(file=FILEPATH+"cracker.gif")


class lockedScreen(Frame):
    def __init__(self, root=None):
        frame = Frame.__init__(self, root)
        self.width = 800
        self.height = 460
        self.grid()
        self.master.title("Template as this will be fullscreen")

        bg_lbl = Label(root, image=lockedBg)
        bg_lbl.image = lockedBg
        bg_lbl.place(x=0, y=0)

        submit_button = Button(root, image=lockedButton, command=test, bg="black", activebackground="black", bd=0)
        submit_button.grid(row=1, column=1, padx=322, pady=142)
        
        print("Locked Screen Initialised")


class verificationScreen(Frame):
    def __init__(self, root=None):
        frame = Frame.__init__(self, root)
        self.width = 800
        self.height = 460
        self.grid()
        self.master.title("Template as this will be fullscreen")

        bg_lbl = Label(root, image=verificationBg)
        bg_lbl.image = verificationBg
        bg_lbl.place(x=0, y=0)
        
        place_face_here = Label(image=face_outline)
        place_face_here.image = face_outline
        place_face_here.grid(row=1, column=1, padx=10, pady=140)


        placeholder_lbl = Label(image=placeholder)
        placeholder_lbl.image = placeholder
        placeholder_lbl.grid(row=1, column=2, padx=100)

        instructions_lbl = Label(image=instructions)
        instructions_lbl.image = instructions
        instructions_lbl.grid(row=1, column=3, padx=10, pady=0)

        take_photo_button = Button(root, image=take_photo, command=test, bg="blue", activebackground="red", bd=0)
        take_photo_button.place(x=330, y=320)


class hudScreen(Frame):
    def __init__(self, root=None):
        frame = Frame.__init__(self, root)
        self.width = 800
        self.height = 460
        self.grid()
        self.master.title("Template as this will be fullscreen")
        crackers = {}

        place_face_here = Label(image=person_pic)
        place_face_here.image = person_pic
        place_face_here.grid(row=2, column=1, padx=20)

        info = Label(root, text="Yeeto Burrito", bg="white")
        info.grid(row=2, column=2, padx=10)

        lock_button = Button(text="Lock")
        lock_button.grid(row=1, column=3, padx=430, pady=20)

        dispense_button = Button(text="Dispense")
        dispense_button.grid(row=3, column=1, padx=20, pady=20)

        refill_button = Button(text="Refill")
        refill_button.grid(row=3, column=2, padx=20, pady=20)

        crackers = Label(image=cracker_pic)
        crackers.image = cracker_pic
        crackers.grid(row=2, column=3, padx=20)


initializePhotos()

#locked = lockedScreen(root)
#verify = verificationScreen(root)
hud = hudScreen(root)




mainloop()
