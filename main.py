'''A temporary file for testing the gui(since package relative paths are dodge)'''
import tkinter as tk

import tools
from rational_gui import verificationScreen, hudScreen, lockedScreen, fingerprintScreen, refillScreen, adminScreen
from rational_gui.controller import CONTROLLER

tools.do_comp_training()

CONTROLLER.add_page(verificationScreen.VerificationScreen)
CONTROLLER.add_page(hudScreen.HudScreen)
CONTROLLER.add_page(lockedScreen.LockedScreen)
CONTROLLER.add_page(fingerprintScreen.FingerprintScreen)
CONTROLLER.add_page(refillScreen.RefillScreen)

try:
    CONTROLLER.add_page(adminScreen.AdminScreen)
except Exception:
    pass

CONTROLLER.show_page("LockedScreen")
tk.mainloop()
