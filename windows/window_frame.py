from Tkinter import *
from buttons.quit_button import quit_app




def init_main(master, resume=False):

    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    welcome_screen = Frame(master, background='#0D1321')
    welcome_screen.pack(expand=1, fill=BOTH)

    total_rows = int(screen_height/9)
    total_cols = int(screen_width/16)
    for i in range(total_cols):
        welcome_screen.grid_columnconfigure(i, minsize=16)

    for i in range(total_rows):
        welcome_screen.grid_rowconfigure(i, minsize=9)

    print welcome_screen.grid_size()
    game_label = Label(welcome_screen,
                       text='Cellular Automata Game',
                       fg='white',
                       font=('Courier', 48),
                       background='#0D1321')

    #game_label.grid(row=total_rows/2, column=0)

    button_column_span = 3
    button_width = button_column_span * 16
    start_column = total_cols/2 - button_column_span

    resume_game_button = Button(welcome_screen, text='Resume game', width=button_width)
    resume_game_button.grid(row=total_rows/3, column=start_column)

    new_game_button = Button(welcome_screen, text='New game', width= button_width)
    new_game_button.grid(row=total_rows/3+2, column=start_column)
    #new_game_button.pack()

    options_button = Button(welcome_screen, text='Options', width= button_width)
    options_button.grid(row=total_rows/3+4, column=start_column)
    #options_button.pack()

    quit_button = Button(welcome_screen, text='Quit', width= button_width, command=quit_app)
    quit_button.grid(row=total_rows/3+6, column=start_column)
    #quit_button.pack()


def init_transition(type, master):
    print 'It will transition'
