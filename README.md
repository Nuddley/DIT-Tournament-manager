# DIT-Tournament-manager

TOURNI VER 1.4 (NON-FUNCTIONAL)
___________________________________

Welcome to Tourni bot. This is a discord bot designed for valorant tournament managing. It has features for competitor entry, team creation, and score tracking. The program is written in Python but doesn't require any python knowledge.

To use this bot you will need: A discord bot, (These can be made at the discord developer portal https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications),

A discord server in which you have admin controls to add bots,

And a moderator role for moderator only commands.
_________________________________________________

Steps:
1. At the top of bot.py are three constants TOKEN, MODERATOR_ROLE, and PREFIX. Fill these in with TOKEN being the bot token from your discord portal, MODERATOR_ROLE being the text name of your servers mod role, and PREFIX being the prefix for commands the bot sends in the server.

2. Add the bot to your server

3. Run main.py, wait for the "Bot is ready" message in the console and then the bot is online!
_________________________________________________

List of Commands:
(The prefix used in these examples is "!" but your prefix may be whatever you choose)

Public commands:

!me (IGN) (RANK)
: Appends the values inside the brackets to a list, IGN and RANK and the discord user who used the command. This list is only players, it is used when the teams are made.

!help 
: Prints a similair list of public commands and what they do in the channel used.

↓↓↓ Moderator Only Commands ↓↓↓

!get_teams
: Makes a .txt file with a list of the discord usernames, In-game names, and game ranks, formatted with a tab inbetween each value so you can easily copy/paste it into a excel file or google sheet.