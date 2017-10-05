from tkinter import *

import tkinter_funcs

FILEPATH = "images/"

#high-quality test function
def test():
    print("BOI PRESSED")

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
        submit_button = Button(root, image=lockedButton, command=test, bg="black", activebackground="black", bd=0)
        submit_button.grid(row=1, column=1, padx=322, pady=142)
        
        print("Locked Screen Initialised")

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


#hud class
class HudScreen(Frame):
    def __init__(self, root=None):
        #setup
        frame = Frame.__init__(self, root)
        self.width = 800
        self.height = 460
        self.grid()
        self.master.title("Template as this will be fullscreen")
        crackers = {}

        #background things
        bg_lbl = Label(root, image=hudBg)
        bg_lbl.image = hudBg
        bg_lbl.place(x=0, y=0)


        #picture of respective person logged in
        person_lbl = Label(image=person_pic)
        person_lbl.image = person_pic
        person_lbl.grid(row=2, column=1, padx=20)

        #info label
        info = Label(root, text="Yeeto Burrito", bg="black", foreground="white")
        info.grid(row=2, column=2, padx=10)

        #lock button stuff
        lock_button = Button(text="Lock", bg="black", activebackground="black", fg="white")
        lock_button.grid(row=1, column=5, padx=170, pady=15)

        #dispense button stuff
        dispense_button = Button(text="Dispense", bg="black", activebackground="black", fg="white")
        dispense_button.grid(row=3, column=2, padx=20, pady=20)

        #refill button things
        refill_button = Button(text="Refill", bg="black", activebackground="black", fg="white")
        refill_button.grid(row=3, column=3, padx=20, pady=20)

        #crackers image things
        crackers = Label(image=cracker_pic)
        crackers.image = cracker_pic
        crackers.grid(row=2, column=4, padx=20)

# inits the photos
lockedBg = PhotoImage(file=FILEPATH+"lockedScreen.gif")
lockedButton = PhotoImage(file=FILEPATH+"unlockTest.png")
placeholder = PhotoImage(file=FILEPATH+"placeholder.gif")
verificationBg = PhotoImage(file=FILEPATH+"verificationScreen.gif")
face_outline = PhotoImage(file=FILEPATH+"outline.gif")
instructions = PhotoImage(file=FILEPATH+"instructions.png")
take_photo = PhotoImage(file=FILEPATH+"camera.png")
person_pic = PhotoImage(file=FILEPATH+"personpic.gif")
cracker_pic = PhotoImage(file=FILEPATH+"cracker.gif")
hudBg = PhotoImage(file=FILEPATH+"hudBg.png")

if __name__ == '__main__':
    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(800, 460))
    root.configure(background='white')
    
    #locked = LockedScreen(root)
    #verify = VerificationScreen(root)
    hud = HudScreen(root)




    mainloop()
