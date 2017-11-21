'''For scanning fingerprint.'''
import tkinter as tk
import tkinter.font

from rational_gui.images import get_imagepath
from rational_gui.page import Page
from rational_gui.controller import CONTROLLER
import authenticate
import threading, queue
from rational_utils.thread_tools import wait_for_thread


class FingerprintScreen(Page):
    def __init__(self, parent):
        super(FingerprintScreen, self).__init__(parent)
        self.width = 800
        self.height = 480
        self.grid()


        verificationBg = tk.PhotoImage(file=get_imagepath("verificationBg"))

        #background things
        bg_lbl = tk.Label(self, image=verificationBg)
        bg_lbl.image = verificationBg
        bg_lbl.place(x=0, y=0)
        info_label = tk.Label(self, font=("Helvetica", 16), 
            text="Sorry, we could not recognise your face, please now try the fingerprint.",
            wraplength=200)
        info_label.grid(row=0, column=0, padx=500, pady=150)
    
    def on_auth_end(self):
        result = self.thread_queue.get()
        if not result:
            CONTROLLER.show_page("LockedScreen")
        else:
            CONTROLLER.show_page("HudScreen", result)

    def verithread(self):
        if self.user:
            success = authenticate.verif_finger(self.user)
            if success:
                self.thread_queue.put(self.user)
            else:
                self.thread_queue.put(False)
        else:
            success, user = authenticate.authenticate_finger()
            if success:
                self.thread_queue.put(user)
            else:
                self.thread_queue.put(False)


    def render(self, data=False):
        self.user = data
        self.thread_queue = queue.Queue()
        thread = threading.Thread(target=self.verithread)
        thread.start()
        wait_for_thread(thread, self.on_auth_end)