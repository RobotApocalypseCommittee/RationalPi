'''A temporary file for testing the gui(since package relative paths are dodge)'''
import tkinter as tk

from settings import CONTROLLER
from rational_gui import controller, verificationScreen, hudScreen, lockedScreen, fingerprintScreen

CONTROLLER = controller.Controller()

CONTROLLER.add_page(verificationScreen.VerificationScreen)
CONTROLLER.add_page(hudScreen.HudScreen)
CONTROLLER.add_page(lockedScreen.LockedScreen)
CONTROLLER.add_page(fingerprintScreen.FingerprintScreen)

CONTROLLER.show_page("VerificationScreen")
tk.mainloop()
