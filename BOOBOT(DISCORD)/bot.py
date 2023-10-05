import os
import random
import discord
from dotenv import load_dotenv
from sweet_nothing import sweet_list, mad_thing, smexy_things

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


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
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to ' f'{guild.name}(id: {guild.id})\n'

    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    print(f'{username}: {user_message} ({channel})')


    if user_message.lower() == 'hey':
        await message.channel.send(get_sweet())
        print(get_sweet())
        return
    elif user_message.lower() == 'i m mad':
        await message.channel.send(get_mad())
        print(get_mad())
        return
    elif user_message.lower() == 'turnon':
        await message.channel.send(get_smexy())
        print(get_smexy())
        return



client.run(TOKEN)
