import sys
from button import Game_Button

def quit_app():
    sys.exit(1)

def get_quit_button(screen):
    return Game_Button(screen, text="Quit", function=quit_app)
