import discord
from discord.ext import commands
import requests
import json
import datetime
import configparser

from helpers import generate_embed

# Open configuration file
config = configparser.ConfigParser()
config.read('bot.ini')

# Get data from configuration file
prefix = config['discord_bot_cfg']['prefix']
tooken = config['discord_bot_cfg']['tooken']

# Init bot
bot = commands.Bot(command_prefix = prefix)
bot.remove_command('help')

# Called when the bot is ready
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(name = 'Type ' + prefix + 'help to get started'))

    print('Bot ready!')

# &help command displays an help embed with a list of all the commands
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.from_rgb(249, 154, 102)
    )

    embed.set_author(name = 'Ranter Bot Help')

    embed.add_field(name = '&rant', value = 'Gets a random rant from devRant', inline = False)

    await ctx.send(embed = embed)

# &rant command gets a random rant from devRant API and sends it to server's text channel
@bot.command()
async def rant(ctx):
    response = requests.get('https://devrant.com/api/devrant/rants/surprise?app=3')

    if response.json()['success'] != True:
        embed = discord.Embed(
            title = ':exclamation: ' + response.json()['error'] + ' :exclamation:',
            colour = discord.Color.red()
        )

        await ctx.send(embed = embed)

        return

    rant = response.json()['rant']

    embed = generate_embed(rant)

    await ctx.send(embed = embed)

# Run bot
bot.run(tooken)