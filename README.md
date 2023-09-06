# DIT-Tournament-manager

TOURNI VER 2.2
___________________________________

Welcome to Tourni bot. This is a discord bot designed for valorant tournament managing. It has features for competitor entry and automatically sorting teams. The program is written in Python but doesn't require any python knowledge.

To use this bot you will need: A discord bot, (These can be made at the discord developer portal https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications),

A discord server in which you have admin controls to add bots,

And a moderator role for moderator only commands.
_________________________________________________

Steps:

1.  Create a bot at the Discord Developer Portal

2.  Write down the bot "Token" it will be a long string of letters and numbers (Write it down in a google doc or in your notes app)

3.  Add your bot to your discord server.

4.  Download the "main.py" and "bot.py" files and put them into a folder. 

5.  Add a sub folder calls "teams"

6.  To run the bot run "main.py". 
If it's your first time running the file this will open a window prompting you to add your bot token and the moderator role. Enter the values and click "apply values" and then click "run bot" If you've entered the values correctly the bot will run and you can close the window. (You will know the bot is online when the console says "Bot is ready") 
If there are any errors, close the program, delete "Prefrences.txt" and try again making sure you enter the token in correctly (I reccomend copy pasting it in.)

If it's not your first time the bot will simply startup without opening the window.


THINGS TO NOTE:
The bot will only be online while the file is running on your computer.
Most errors the bot will be able to just avoid so don't worry if your console has a red message in it. 
If the bot does crash the best solution is to just restart it.
_________________________________________________

List of Commands:

↓↓↓ Public commands ↓↓↓

/compete
A slash command which prompts you to enter a "Username" and "Rank". This is for competitors entering a tournament. When they enter with their valid username and valorant rank the entry is added to a list. When the entry period closes moderators can run the command to get a list of the teams.

!help 
Explains the entry process.

↓↓↓ Moderator Only Commands ↓↓↓

!sort_elo_spec
Will write txt files for: low, mid, high, and top elo. Sorting through all the entrys and assigning them to elo divisions based on their entered rank.
Each elo division will contain teams with their corrosponding ranks.

Low elo: Iron, Bronze
Mid elo: Silver, Gold, Platinum
High elo: Diamond, Ascendant
Top elo: Immortal, Radiant

Each division is split in a different file with a list containing the players discord @, IGN, Rank, and team number. You can copy paste this into a google sheet/excel spreadsheet for easier viewing.