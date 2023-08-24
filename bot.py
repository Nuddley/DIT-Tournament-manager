"""Tourni bot Version 1.5 (NOT FUNCTIONAL)"""

import discord
from discord.ext import commands 
from discord.ext.commands import has_permissions
from discord import app_commands
import tracemalloc

client = commands.Bot(command_prefix="!", intents = discord.Intents.all())
entrys = []

# Funtion to run the bot
def run_bot():
    print("BOT | START REQUEST RECIEVED")
    try:
        txt_open = open("prefrences.txt", "r")
        prefrences = txt_open.readlines()
        print("BOT | DEV ||", prefrences)
        TOKEN = prefrences[0]
        MODERATOR_ROLE = prefrences[1]
        txt_open.close()
        try:
            client.run(TOKEN)
            print("BOT | CLIENT STARTED PLEASE WAIT")
        except discord.errors.LoginFailure:
            print("BOT | IMPROPER TOKEN PASSED PLEASE DELETE PREFRENCES.TXT AND RESTART")
    except FileNotFoundError:
        print("BOT | PREFRENCES.TXT NOT LOCATED")

@client.event
async def on_ready():
    print("BOT | Bot is online")
    # Check memory allocation and print it
    print("BOT | Traced memory: ", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    # Sync slash commands
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command/s")
    except Exception as e:
        print(e)

# DEV Test command to get slash commands working
@client.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a test command",
    ephemeral = True)

# The entry command
@client.tree.command(name="compete")
@app_commands.describe(username = "Your InGame name and tag E.G Username#tag", rank = "Your current InGame rank")
async def compete(interaction: discord.Interaction, username: str, rank: str):
    await interaction.response.send_message(f"{interaction.user.name} Applied with rank {rank} and username {username}")
    # Append validated entry to the list and print it to console
    entrys.append([interaction.user.mention, username, rank])
    print(f"NEW ENTRY: \n    Discord: {interaction.user.mention} | \n    IGN: {username} | \n    Rank: {rank} |")


"""↓↓↓ Moderator Only Commands ↓↓↓"""

# Saves and prints the teams to a .txt file
@client.command()
async def get_teams(ctx):
    message = ctx.message.content
    user = ctx.author
    # Checks the prefrences file to get mod role variable
    txt_open = open("prefrences.txt", "r")
    prefrences = txt_open.readlines()
    print("BOT | DEV ||", prefrences)
    MODERATOR_ROLE = prefrences[1]
    txt_open.close()
    # Checks if user is a server moderator and runs command if true.
    if MODERATOR_ROLE in [i.name.lower() for i in user.roles]:
        f = open("Teams.txt", "w")
        f.write(f"Team	DISC user	IGN	Rank")
        for player in entrys:
            team = 1
            disc_user = player[0]
            ign = player[1]
            rank = player[2]
            f.write(f"\n{team}	{disc_user}	{ign}	{rank}")
        f.close()
        await ctx.send(f"{user} | A .txt file has been created in the TOURNI file with the current teams.")
    else:
        await ctx.send(f"{user} does not have permission to use this command.")

# Memory trace start
tracemalloc.start()
