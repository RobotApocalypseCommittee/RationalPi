from tkinter import *

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