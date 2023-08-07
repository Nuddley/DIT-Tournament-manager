"""Tourni bot Version 1.4 NOT FUNCTIONAL)"""

from tkinter import *
from tkinter import messagebox
import multiprocessing
import bot

class Gui:
    # Inital GUI setup
    def __init__(self, parent):
        self.botstatus = False
        self.state_lbl = Label(parent, text="Bot is offline")
        self.butt_run = Button(parent, text="Run Bot", command=self.onclick_run_bot)
        self.token_entry = Entry(parent)
        self.prefix_entry = Entry(parent)
        self.mod_entry = Entry(parent)
        self.token_lbl = Label(parent, text="Token")
        self.prefix_lbl = Label(parent, text="Prefix")
        self.mod_lbl = Label(parent, text="Moderator role")
        self.apply_butt = Button(parent, text="Apply bot values", command=self.onclick_apply_botval  )

        self.state_lbl.grid(row=4, column=0)
        self.butt_run.grid(row=5, column=0)
        self.token_entry.grid(row=0, column=0)
        self.token_lbl.grid(row=0, column=1)
        self.mod_entry.grid(row=1, column=0)
        self.mod_lbl.grid(row=1, column=1)
        self.prefix_entry.grid(row=2, column=0)
        self.prefix_lbl.grid(row=2, column=1)
        self.apply_butt.grid(row=3, column=1)

    # Function checks if bot is online or not and either starts it or ends it aswell as configuring the GUI
    def onclick_run_bot(self):
        if self.botstatus == False:
            bot_process.start()
            self.botstatus = True
            self.butt_run.configure(text="Stop Bot")
        elif self.botstatus == True:
            bot_process.terminate()
            self.botstatus = False
            self.butt_run.configure(text="Run Bot")

    # Function sets bot values and 
    def onclick_apply_botval(self):
        print(self.token_entry.get())
        bot.TOKEN == self.token_entry.get()
        bot.PREFIX == self.prefix_entry.get()
        bot.MODERATOR_ROLE == self.mod_entry.get()

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
