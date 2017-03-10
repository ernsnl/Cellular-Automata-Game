from Tkinter import *
from windows.window_frame import init_main

game = Tk()

game.attributes("-fullscreen", True)
game.configure(background='#0D1321')

screen_width = game.winfo_screenwidth()
screen_height = game.winfo_screenheight()

# TO DO Get the Save File

init_main(game)

mainloop()
