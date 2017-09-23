import tkinter as tk

import authenticate

class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.button = tk.Button(frame, 
                             text="QUIT", fg="red",
                             command=quit)
        self.button.pack(side=tk.LEFT)

        self.slogan = tk.Button(frame,
                             text="Hello",
                             command=self.write_slogan)
        self.slogan.pack(side=tk.LEFT)

        self.auth = tk.Button(frame,
                            text='Authenticate',
                            command=self.authenticate_user)
        self.auth.pack(side=tk.BOTTOM)
    
    def write_slogan(self):
        print("Tkinter is easy to use!")

    def authenticate_user(self):
        print(authenticate.authenticate_face(recogniser))

recognizer = cv2.face.LBPHFaceRecognizer_create()
authenticate.do_training(recogniser)

root = tk.Tk()

root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
app = App(root)


root.mainloop()
