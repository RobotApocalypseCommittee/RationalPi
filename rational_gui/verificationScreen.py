import tkinter as tk

from rational_gui.images import get_imagepath
from rational_gui.page import Page
from rational_gui.controller import CONTROLLER
import authenticate
import queue
import threading
from rational_utils.thread_tools import wait_for_thread

try:
    import tkinter_funcs
except ImportError:
    pass

#verification class
class VerificationScreen(Page):
    def __init__(self, parent):
        #basic setup things
        super(VerificationScreen, self).__init__(parent)
        self.grid()

        verificationBg = tk.PhotoImage(file=get_imagepath("verificationBg"))
        face_outline = tk.PhotoImage(file=get_imagepath("positionFace"))
        placeholder = tk.PhotoImage(file=get_imagepath("placeholder"))
        instructions = tk.PhotoImage(file=get_imagepath("plspositionboi"))
        
        self.take_photo_img = tk.PhotoImage(file=get_imagepath("newCamera"))

        #background things
        bg_lbl = tk.Label(self, image=verificationBg)
        bg_lbl.image = verificationBg
        bg_lbl.place(x=-2, y=-2)
        
        #face guidance image
        place_face_here = tk.Label(self, image=face_outline, borderwidth=0)
        place_face_here.image = face_outline
        place_face_here.place(x=10, y=170)

        #picam placeholder image
        self.instruction_text = tk.StringVar()
        self.instruction_text.set("Get Ready for Photo")
        placeholder_lbl = tk.Label(self, textvariable=self.instruction_text, borderwidth=0)

        placeholder_lbl.place(x=304, y=170)

        #instructions image
        instructions_lbl = tk.Label(self, image=instructions, borderwidth=0)
        instructions_lbl.image = instructions
        instructions_lbl.place(x=510, y=200)
        
        self.thread_queue = queue.Queue()

    def on_auth_end(self):
        result = self.thread_queue.get()

        CONTROLLER.show_page("FingerprintScreen", result)
        
    def verithread(self):
        for i in range(5, 0, -1):
            self.instruction_text.set("Photo taken in "+ str(i) + " seconds.")
        success, user = authenticate.authenticate_face()
        if success:
            self.thread_queue.put(user)
        else:
            self.thread_queue.put(False)


    def render(self):
        thread = threading.Thread(target=self.verithread)
        thread.start()
        wait_for_thread(thread, self.on_auth_end)


