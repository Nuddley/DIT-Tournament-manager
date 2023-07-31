"""Tourni bot Version 1.3 NOT FUNCTIONAL)"""

import discord
from discord.ext import commands
from tkinter import *
from tkinter import messagebox
import multiprocessing
import bot

class Gui:
    def __init__(self, parent):
        test = Label(parent, text="Hello")
        test.pack()
        butt = Button(parent, text="send message", command=self.bot_message)
        butt.pack()
        self.e1 = Entry(parent)
        self.e1.pack()

    async def bot_message(self):
        await bot.send_message(self.e1.get())


def bot_run_func():
    bot.run_bot()

def backend_run_func():
    root = Tk()
    root.title("Tourni BACKEND")
    gui_instance=Gui(root)
    root.mainloop()

backend_process = multiprocessing.Process(target=backend_run_func)
bot_process = multiprocessing.Process(target=bot_run_func)

if __name__ == "__main__":
    backend_process.start()
    bot_process.start()