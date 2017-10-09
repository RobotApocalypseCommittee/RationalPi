'''A temporary file for testing the gui(since package relative paths are dodge)'''
import tkinter as tk
from rational_gui import controller, verificationScreen, hudScreen, lockedScreen

cont = controller.Controller()

cont.add_page(verificationScreen.VerificationScreen)
cont.add_page(hudScreen.HudScreen)
cont.add_page(lockedScreen.LockedScreen)

cont.show_page("LockedScreen")
tk.mainloop()
