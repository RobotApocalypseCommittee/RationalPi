import tkinter as tk

from rational_gui.images import get_imagepath
from rational_gui.page import Page


#hud class
class HudScreen(Page):
    def __init__(self, parent, controller):
        #setup things
        super().__init__(parent, controller)
        self.width = 800
        self.height = 460
        self.grid()
        crackers = {}

        hudBg = tk.PhotoImage(file=get_imagepath("hudBg"))
        cracker_pic = tk.PhotoImage(file=get_imagepath("cracker"))

        # This is going to have to be changed...
        person_pic = tk.PhotoImage(file=get_imagepath("personpic"))

        #background things
        bg_lbl = tk.Label(self, image=hudBg)
        bg_lbl.image = hudBg
        bg_lbl.place(x=0, y=0)


        #picture of respective person logged in
        person_lbl = tk.Label(self, image=person_pic)
        person_lbl.image = person_pic
        person_lbl.grid(row=2, column=1, padx=20)

        #info label
        info = tk.Label(self, text="Yeeto Burrito", bg="black", foreground="white")
        info.grid(row=2, column=2, padx=10)

        #lock button stuff
        lock_button = tk.Button(self, text="Lock", bg="black", activebackground="black", fg="white")
        lock_button.grid(row=1, column=5, padx=170, pady=15)

        #dispense button stuff
        dispense_button = tk.Button(self, text="Dispense", bg="black", activebackground="black", fg="white")
        dispense_button.grid(row=3, column=2, padx=20, pady=20)

        #refill button things
        refill_button = tk.Button(self, text="Refill", bg="black", activebackground="black", fg="white")
        refill_button.grid(row=3, column=3, padx=20, pady=20)

        #crackers image things
        crackers = tk.Label(self, image=cracker_pic)
        crackers.image = cracker_pic
        crackers.grid(row=2, column=4, padx=20)
