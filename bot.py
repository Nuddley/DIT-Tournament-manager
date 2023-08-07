"""Tourni bot Version 1.4 (NOT FUNCTIONAL)"""

import discord
from discord.ext import commands 
from discord.ext.commands import has_permissions
import tracemalloc


# Import constants for user
TOKEN = "token"
MODERATOR_ROLE = "moderator role"
PREFIX = "prefix"


client = commands.Bot(command_prefix=PREFIX, intents = discord.Intents.all())
entrys = []

@client.event
async def on_ready():
    print("Bot is online")
    # Check memory allocation and print it
    print("Traced memory: ", tracemalloc.get_traced_memory())
    tracemalloc.stop()

# Initial add command, only available for competitors
@client.command()
async def me(ctx):
    message_content = ctx.message.content
    ingame_name = ""
    ingame_rank = ""
    name_rank = []
    
    message = message_content[4:]
    user = ctx.author

    # Remove unneccasary characters in the format
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

        # DEV Print info to console
        print(f"Both: {name_rank}")
        print(f"Name: {ingame_name}")
        print(f"Rank: {ingame_rank}")
        print(f"Discord Name: {user}")

        # Send confirmation message to DMs
        await ctx.author.send(f"Hello {user} you have entered the tournament with the following information: \nUsername:{ingame_name} \nRank: {ingame_rank}")
    except:
        # Or tell the user the correct format if any issues
        await ctx.send(f"{ctx.message.author.mention} That format is incorrect, please try again with the following format. \n!me (UserName)(Rank)")

    # Append validated entry to the list and print it to console
    entrys.append([ctx.author, ingame_name, ingame_rank])
    print(f"NEW ENTRY: \n    Discord: {user} | \n    IGN: {ingame_name} | \n    Rank: {ingame_rank} |")


"""↓↓↓ Moderator Only Commands ↓↓↓"""

# Saves and prints the teams to a .txt file
@client.command()
async def get_teams(ctx):
    message = ctx.message.content
    user = ctx.author
    TAB = "	"
    # Checks if user is a server moderator and runs command if true.
    if MODERATOR_ROLE in [i.name.lower() for i in user.roles]:
        with open("Teams.txt", "w")as f:
            f.write(f"Team{TAB}DISC user{TAB}IGN{TAB}Rank")
            for player in entrys:
                team = 1
                disc_user = player[0]
                ign = player[1]
                rank = player[2]
                f.write(f"\n{team}{TAB}{disc_user}{TAB}{ign}{TAB}{rank}")
        await ctx.send(f"{user} | A text file has been created on your desktop with the current teams.")
    else:
        await ctx.send(f"{user} does not have permission to use this command.")

    
# Funtion to run the bot
def run_bot():
    client.run(TOKEN)

# Memory trace start
tracemalloc.start()
