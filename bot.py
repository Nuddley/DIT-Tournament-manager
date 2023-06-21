import discord
from discord.ext import commands

TOKEN = "Enter your token"


client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is online")

@client.command()
async def ping(ctx):
    await ctx.author.send("Pong!")

client.run(TOKEN)
