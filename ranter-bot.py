import discord
from discord.ext import commands
import requests
import json
import datetime
import os

from helpers import generate_embed
from helpers import error_embed

# Get tooken and prefix from environment variables 
prefix = os.getenv('PREFIX', '&')
tooken = os.getenv('TOOKEN')

# Init bot
bot = commands.Bot(command_prefix = prefix)
bot.remove_command('help')

# Called when the bot is ready
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(name = 'Type ' + prefix + 'help to get started'))

    print('Bot ready!')

# Help command displays an help embed with a list of all the commands
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.from_rgb(249, 154, 102)
    )

    embed.set_author(name = 'Ranter Bot Help')

    embed.add_field(name = prefix + 'top', value = 'Gets the top rant given by devRant algorithm.')
    embed.add_field(name = prefix + 'surprise', value = 'Gets a random rant from devRant', inline = False)

    await ctx.send(embed = embed)

# Rant command gets a rant using devRant algorithm
@bot.command()
async def top(ctx):
    response = requests.get('https://devrant.com/api/devrant/rants?app=3&sort=algo&limit=1')

    if response.json()['success'] != True:
        await ctx.send(embed = error_embed(response.json()['error']))
        return

    rant = response.json()['rants'][0]
    await ctx.send(embed = generate_embed(rant))

# Surprise command gets a random rant from devRant API and sends it to server's text channel
@bot.command()
async def surprise(ctx):
    response = requests.get('https://devrant.com/api/devrant/rants/surprise?app=3')

    if response.json()['success'] != True:
        await ctx.send(embed =  error_embed(response.json()['error']))
        return

    rant = response.json()['rant']
    await ctx.send(embed = generate_embed(rant))

# Run bot
bot.run(tooken)