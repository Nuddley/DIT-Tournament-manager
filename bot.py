import discord
from discord.ext import commands

TOKEN = "Enter Token"


client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

entrys = []

@client.event
async def on_ready():
    print("Bot is online")

@client.command()
async def me(ctx):
    message_content = ctx.message.content
    ingame_name = ""
    ingame_rank = ""
    name_rank = []
    
    message = message_content[4:]
    user = ctx.author

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

    await ctx.author.send(f"Your have entered the tournament with the following information: \nUsername:{ingame_name} \nRank: {ingame_rank}")

    entrys.append([ctx.author, ingame_name, ingame_rank])

client.run(TOKEN)
