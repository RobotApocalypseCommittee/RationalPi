import tkinter as tk

class Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

    def render(**kwargs):
        '''Receives render data through kwargs, and has to change values.'''
        pass