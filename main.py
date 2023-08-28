"""Tourni bot Version 2.1 NOT FUNCTIONAL)"""

from tkinter import *
from tkinter import messagebox
import multiprocessing
import sys
import bot

class Gui:
    # Inital GUI setup
    def __init__(self, parent):
        self.first_startup = Frame(parent)
        self.main_page = Frame(parent)
        self.bot_ison = False

        # Widgets for first time startup page
        self.state_lbl = Label(self.first_startup, text="Bot is offline")
        self.token_entry = Entry(self.first_startup)
        self.mod_entry = Entry(self.first_startup)
        self.token_lbl = Label(self.first_startup, text="Token")
        self.mod_lbl = Label(self.first_startup, text="Moderator role")
        self.apply_butt = Button(self.first_startup, text="Apply bot values", command=self.onclick_apply_botval)
        self.run_butt = Button(self.first_startup, text="Run Bot", command=self.onclick_run_bot)
        self.state_lbl.grid(row=5, column=0)
        self.token_entry.grid(row=0, column=0)
        self.token_lbl.grid(row=0, column=1)
        self.mod_entry.grid(row=1, column=0)
        self.mod_lbl.grid(row=1, column=1)
        self.apply_butt.grid(row=3, column=1)
        self.run_butt.grid(row=4, column=1)

        try:
            f = open("prefrences.txt", "x")
            print("GUI | FIRST TIME STARTUP: beginning first time start up")
            self.first_startup.pack()
            f.close()
        except FileExistsError:
            print("GUI | RETURNING STARTUP: CONTINUE")
            bot_process.start()
            f.close()

    # Function sets bot values to the prefrences file
    def onclick_apply_botval(self):
        print("GUI | ENTRY GET: ", self.token_entry.get())
        txt_file = open("prefrences.txt", "w")
        txt_file.write(self.token_entry.get())
        txt_file.write("\n"+self.mod_entry.get())
        txt_file.close()
        print("GUI | SETTINGS WRITTEN")

    # Function for sending the run command.
    def onclick_run_bot(self):
        print("GUI | ONCLICK RUNBOT RECIEVED")
        try:
            bot_process.start()
        except RuntimeError:
            messagebox(title="GUI ERROR", message="ERROR CANNOT START TWICE PLEASE RESTART AND CHECK YOUR PREFRENCES")

# Run the backend functions
def backend_run_func():
    root = Tk()
    root.title("Tourni BACKEND")
    gui_instance=Gui(root)
    root.mainloop()

# Sets up the multiprocessing processes
backend_process = multiprocessing.Process(target=backend_run_func)
bot_process = multiprocessing.Process(target=bot.run_bot)

# Main routine, starts backend window
if __name__ == "__main__":
    backend_process.start()
