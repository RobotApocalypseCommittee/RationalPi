import tkinter as tk

from rational_gui.images import get_imagepath
from rational_gui.page import Page
from rational_gui.controller import CONTROLLER


#hud class
class HudScreen(Page):
    def __init__(self, parent):
        #setup things
        super().__init__(parent)
        self.width = 800
        self.height = 480
        self.grid()
        crackers = {}

        hudBg = tk.PhotoImage(file=get_imagepath("hudBg"))
        cracker_holder = tk.PhotoImage(file=get_imagepath("crackerHolder"))
        cracker = tk.PhotoImage(file=get_imagepath("cracker2"))

        # This is going to have to be changed...
        person_pic = tk.PhotoImage(file=get_imagepath("personpic"))

        #background things
        bg_lbl = tk.Label(self, image=hudBg)
        bg_lbl.image = hudBg
        bg_lbl.place(x=-2, y=-2)


        #picture of respective person logged in
        person_pic = person_pic.subsample(3, 3)
        person_lbl = tk.Label(self, image=person_pic)
        person_lbl.image = person_pic
        person_lbl.place(x=370, y=30)

        #info label
        info = tk.Label(self, text="You have x crackers left today!", bg="black", foreground="white")
        info.place(x=320, y=420)

        #lock button stuff
        lock_button = tk.Button(self, text="Lock", bg="black", activebackground="black", fg="white", command=lambda: CONTROLLER.show_page("LockedScreen"))
        lock_button.place(x=740, y=20)

        #dispense button stuff
        dispense_button = tk.Button(self, text="Dispense", bg="black", activebackground="black", fg="white")
        dispense_button.place(x=370, y=300)

        #refill button things
        refill_button = tk.Button(self, text="Refill", bg="black", activebackground="black", fg="white")
        refill_button.place(x=20, y=420)

        #crackers image things
        person_lbl = tk.Label(self, image=cracker_holder, bd=0)
        person_lbl.image = cracker_holder
        person_lbl.place(x=20, y=30)

        #temporary variable so you can see that it still works with less crackers (try changing it)
        cracker_count = 14
        cry = 348
        for i in range(cracker_count):
            crackers = tk.Label(self, image=cracker, bd=0)
            crackers.image = cracker
            crackers.place(x=35, y=cry)
            cry -= 23
