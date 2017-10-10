'''A temporary file for testing the gui(since package relative paths are dodge)'''
import tkinter as tk
from rational_gui import controller, verificationScreen, hudScreen, lockedScreen, fingerprintScreen

cont = controller.Controller()

cont.add_page(verificationScreen.VerificationScreen)
cont.add_page(hudScreen.HudScreen)
cont.add_page(lockedScreen.LockedScreen)
cont.add_page(fingerprintScreen.FingerprintScreen)

cont.show_page("FingerprintScreen")
tk.mainloop()
