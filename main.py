import discord
from discord.ext import commands
from tkinter import *
from tkinter import messagebox

class client_bot:
    def __init__(self):
        self.TOKEN = "Enter Token"
        entrys = []

        @self.client.event
        async def on_ready():
            print("Bot is online")

        @self.client.command()
        async def me(ctx):
            message_content = ctx.message.content
            ingame_name = ""
            ingame_rank = ""
            name_rank = []
            
            message = message_content[4:]
            user = ctx.author

            try:
                temp_list = []
                for letter in message:
                    temp_list.append(letter)
                    name_rank.append(letter)
                temp_list.remove("(")
                temp_list.remove("(")
                name_rank.remove("(")
                name_rank.remove("(")

                for x in temp_list:
                    if x == ")":
                        name_rank.remove(x)
                        break
                    else:
                        ingame_name += x
                        name_rank.remove(x)

                for x in name_rank:
                    if x == ")":
                        break
                    else:
                        ingame_rank += x

                print(f"Both: {name_rank}")
                print(f"Name: {ingame_name}")
                print(f"Rank: {ingame_rank}")
                print(f"Discord Name: {user}")

                await ctx.author.send(f"Hello {user} you have entered the tournament with the following information: \nUsername:{ingame_name} \nRank: {ingame_rank}")
            except:
                await ctx.send(f"{ctx.message.author.mention} That format is incorrect, please try again with the following format. \n!me (UserName)(Rank)")

            entrys.append([ctx.author, ingame_name, ingame_rank])


    def send_message(self):
        channel = self.client.get_channel(1120486918166155327)
        print(channel)
        channel.send("tester")
        

class Gui:
    def __init__(self, parent):
         label = Label(parent, text="Hello")
         label.pack()
         send_message = Button(parent, text="send", command=self.ask_bot)
         send_message.pack()

    def ask_bot():
        client_bot.send_message()


if __name__ == "__main__":
    root = Tk()
    instance=Gui(root)
    root.mainloop()
    client = commands.Bot(command_prefix="!", intents = discord.Intents.all())
    client.run("ENTER TOKEN")

