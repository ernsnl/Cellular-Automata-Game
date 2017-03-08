from Tkinter import *

class Game_Button(Button):
    def __init__(self, master ,text, function):
        Button.__init__(self, master=master, text=text, command=function)
        self.pack()
