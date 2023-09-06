"""Tourni bot Version 2.2"""

import discord
from discord.ext import commands 
from discord.ext.commands import has_permissions
from discord import app_commands
from tkinter import messagebox
import tracemalloc

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

global entrys
entrys = []
global valorant_ranks
valorant_ranks = ["iron", "bronze", "silver", "gold", "platinum", "diamond", "ascendant", "immortal", "radiant"]

# Funtion to run the bot
def run_bot():
    print("BOT | START REQUEST RECIEVED")
    try:
        txt_open = open("prefrences.txt", "r")
        prefrences = txt_open.readlines()
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

client.remove_command('help')

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
    """Slash command to compete in the tournament."""
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

# Help command
@client.command()
async def help(ctx, command_name: str = None):
    await ctx.send(f'Do "/compete" to enter into the tournament. This command will prompt you to add your IGN, and Rank. This is your In game name for VALORANT including your tag. your rank should be the full word followed by 1, 2, or 3 (Unless your radiant). (E.G: Diamond 3)\n Please be honest and enter your GENUINE RANK.')

"""↓↓↓ Moderator Only Commands ↓↓↓"""

# Saves and prints the teams to a .txt file
@client.command()
async def sort_elo_spec(ctx):
    """Moderator only command to get the sorted teams printed."""
    user = ctx.author
    # Checks if user is a server moderator and runs command if true.
    if MODERATOR_ROLE in [i.name.lower() for i in user.roles]:
        low_elo = [] # Iron Bronze
        mid_elo = [] # Silver Gold Plat
        high_elo = [] # Dia Asc
        top_elo = [] # Immortal Radiant
        unsorted = entrys
        # Sorts through the list of all players and assigns them to their specific "Elo"
        for player in unsorted:
            if "iron" in player[2] or "bronze" in player[2]:
                low_elo.append(player)
            if "silver" in player[2] or "gold" in player[2] or "platinum" in player[2]:
                mid_elo.append(player)
            if "diamond" in player[2] or "ascendant" in player[2]:
                high_elo.append(player)
            if "immortal" in player[2] or "radiant" in player[2]:
                top_elo.append(player)
            team_file("low_elo_teams", low_elo)
            team_file("mid_elo_teams", mid_elo)
            team_file("high_elo_teams", high_elo)
            team_file("top_elo_teams", top_elo)
        await ctx.send(f"{user} | A .txt file has been created in the TOURNI folder with the sorted teams")
    else:
        await ctx.send(f"{user} does not have permission to use this command.")


def team_file(file_name, list):
    # Gives the players team numbers
    f = open(("teams/"+file_name), "w")
    count = 1
    team = 1
    for player in list:
        player.append(team)
        if count == 5:
            count = 1
            team += 1
        else:
            count += 1
    # Writes the information to a txt file
    titles = ["Discord @", "IGN", "Rank", "Team #"]
    f.write(f"{titles[0]:<10}    {titles[1]:<10}    {titles[2]:<10}    {titles[3]:<10}\n")
    for player in list:
        f.write(f"{player[0]:<10}    {player[1]:<10}    {player[2]:<10}    {player[3]:<10}\n")
    f.close()

# Memory trace start
tracemalloc.start()
