#!/usr/bin/python
from Tkinter import *

from buttons.init_buttons import place_button
game = Tk()
# Code to add widgets will go here...
game.attributes("-fullscreen", True)
game.configure(background='#0D1321')

def raise_frame(frame):
    frame.tkraise()

f1 = Frame(game)
f2 = Frame(game)
f3 = Frame(game)
f4 = Frame(game)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
Label(f1, text='FRAME 1').pack()
place_button(f1)

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()
place_button(f2)

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')
place_button(f3)


Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()
place_button(f4)

raise_frame(f1)

print game.winfo_screenwidth()
print game.winfo_screenheight()

mainloop()
