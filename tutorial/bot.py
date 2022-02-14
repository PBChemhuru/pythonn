import os
import random
import discord
from dotenv import load_dotenv
from sweet_nothing import sweet_list, mad_thing, smexy_things

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


def get_sweet():
    sweet = random.choice(sweet_list)
    return sweet.lower()


def get_mad():
    mad = random.choice(mad_thing)
    return mad.lower()


def get_smexy():
    smexy = random.choice(smexy_things)
    return smexy.lower()


@client.event
async def on_ready():
    print(
        f'{client.user} is connected\n'
    )


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'right-here':
        if user_message.lower() == 'hey':
            await message.channel.send(get_sweet())
            print(get_sweet())
            return
        elif user_message.lower() == 'i m mad':
            await message.channel.send(get_mad())
            print(get_sweet())
            return
        elif user_message.lower() == 'talk dirty to me':
            await message.channel.send(get_smexy())
            print(get_sweet())
            return


client.run(TOKEN)
