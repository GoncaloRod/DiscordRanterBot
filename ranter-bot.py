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

    embed.add_field(
        name = '```' + prefix + 'top' + '```', 
        value = 'Check out the master of rants!',
        inline = False,
    )
    
    embed.add_field(
        name = '```' + prefix + 'trending' + '```',
        value = 'Just ask devRant\'s algorithm for a rant.',
        inline = False
    )
    
    embed.add_field(
        name = '```' + prefix + 'recent' + '```',
        value = 'Check out the latest and greatest from de devRant community!',
        inline = False
    )
    
    embed.add_field(
        name = '```' + prefix + 'surprise' + '```',
        value = 'Feeling lucky?',
        inline = False
    )
    
    embed.add_field(
        name = '```' + prefix + 'rant <link>' + '```',
        value = 'Have you seen a cool rant? Want to share it with your friends in a cooler way?! Well, this command has got your back!',
        inline = False
    )

    await ctx.send(embed = embed)

@bot.command()
async def top(ctx):
    response = requests.get('https://devrant.com/api/devrant/rants?app=3&sort=top&limit=1')

    if response.json()['success'] != True:
        await ctx.send(embed = error_embed(response.json()['error']))
        return

    rant = response.json()['rants'][0]
    await ctx.send(embed = generate_embed(rant))


@bot.command()
async def trending(ctx):
    response = requests.get('https://devrant.com/api/devrant/rants?app=3&sort=algo&limit=1')

    if response.json()['success'] != True:
        await ctx.send(embed = error_embed(response.json()['error']))
        return

    rant = response.json()['rants'][0]
    await ctx.send(embed = generate_embed(rant))

@bot.command()
async def recent(ctx):
    response = requests.get('https://devrant.com/api/devrant/rants?app=3&sort=recent&limit=1')

    if response.json()['success'] != True:
        await ctx.send(embed = error_embed(response.json()['error']))
        return

    rant = response.json()['rants'][0]
    await ctx.send(embed = generate_embed(rant))

@bot.command()
async def surprise(ctx):
    response = requests.get('https://devrant.com/api/devrant/rants/surprise?app=3')

    if response.json()['success'] != True:
        await ctx.send(embed =  error_embed(response.json()['error']))
        return

    rant = response.json()['rant']
    await ctx.send(embed = generate_embed(rant))

@bot.command()
async def rant(ctx, link):
    id = link.split('/')[4]

    response = requests.get('https://devrant.com/api/devrant/rants/' + id + '?app=3')

    if response.json()['success'] != True:
        await ctx.send(embed =  error_embed(response.json()['error']))
        return

    rant = response.json()['rant']
    await ctx.send(embed = generate_embed(rant))

# Run bot
bot.run(tooken)