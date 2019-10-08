import discord

# Generates and returns an Embed object from a rant json object
def generate_embed(rant):
    embed = discord.Embed(
        description = rant['text'] + "\n[Read More](https://devrant.com/rants/" + str(rant['id']) + ")",
        colour = discord.Colour.from_rgb(249, 154, 102)
    )

    if rant.get('i'):
        embed.set_author(name = rant['user_username'], icon_url = 'https://avatars.devrant.com/' + rant['user_avatar']['i'])
    else:
        embed.set_author(name = rant['user_username'])

    embed.set_footer(text = str(rant['score']) + '++ | ' + str(rant['num_comments']) + ' Comments')



    if rant['attached_image'] != '':
        embed.set_image(url = rant['attached_image']['url'])

    return embed

def error_embed(error):
    discord.Embed(
        title = ':exclamation: ' + error + ' :exclamation:',
        colour = discord.Color.red()
    )