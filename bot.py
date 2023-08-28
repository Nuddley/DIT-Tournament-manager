"""Tourni bot Version 1.5 (NOT FUNCTIONAL)"""

import discord
from discord.ext import commands 
from discord.ext.commands import has_permissions
from discord import app_commands
from tkinter import messagebox
import tracemalloc

client = commands.Bot(command_prefix="!", intents = discord.Intents.all())
entrys = []

global valorant_ranks
valorant_ranks = ["iron", "bronze", "silver", "gold", "platinum", "diamond", "ascendant", "immortal", "radiant"]

# Funtion to run the bot
def run_bot():
    print("BOT | START REQUEST RECIEVED")
    try:
        txt_open = open("prefrences.txt", "r")
        prefrences = txt_open.readlines()
        print("BOT | DEV ||", prefrences)
        global TOKEN
        global MODERATOR_ROLE
        TOKEN = prefrences[0]
        MODERATOR_ROLE = prefrences[1]
        txt_open.close()
        try:
            client.run(TOKEN)
            print("BOT | CLIENT STARTED PLEASE WAIT")
        except discord.errors.LoginFailure:
            messagebox(title="BOT ERROR", message="IMPROPER TOKEN PASSED PLEASE DELETE PREFRENCES.TXT AND RESTART")
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

# The entry command
@client.tree.command(name="compete")
@app_commands.describe(username = "Your in game name and tag E.G 'Username#4826'", rank = "Your current in game rank by full word and number E.G 'diamond 3'")
async def compete(interaction: discord.Interaction, username: str, rank: str):
    # Checks for a valorant tag and a valid rank before appending it to the list
    if any(check in rank for check in valorant_ranks):
        if "#" in username:
            entrys.append([interaction.user.mention, username, rank])
            await interaction.response.send_message(f"{interaction.user.name} you have applied with rank: {rank} and username: {username}", ephemeral=True)
            print(f"NEW ENTRY:\n    Discord: {interaction.user.mention}\n    IGN: {username}\n    Rank: {rank}")
        else:
            await interaction.response.send_message(f"The Username you have entered with ({username}) does not have a tag which is required, this entry has not been recorded. Please try again ", ephemeral=True)
    else:
        await interaction.response.send_message(f"The Rank you have entered with ({rank}) is not a valid VALORANT rank, this entry has not been recorded. Please try again with one of the following ranks: iron, bronze, silver, gold, platinum, diamond, ascendant, immortal, radiant.", ephemeral=True)

"""↓↓↓ Moderator Only Commands ↓↓↓"""

# Saves and prints the teams to a .txt file
@client.command()
async def get_teams(ctx):
    message = ctx.message.content
    user = ctx.author
    # Checks the prefrences file to get mod role variable
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
