import asyncio

import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import youtube_dl

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="!")

youtube_dl.utils.bug_reports_message = lambda: ''

youtube_dl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilesnames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warning': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'

}


@client.event  # check if bot is ready
async def on_ready():
    print('Bot online')


ytdl = youtube_dl.YoutubeDL(youtube_dl_format_options)


@client.command(name='play_songs', help='To play song')
async def play_songs(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command(name='join', help='Tells the bot leave the voice channel')
async def join(ctx):
    if not ctx.nessage.author.voice:
        await ctx.send("{} is not in the voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@client.command(name='leave', help='Tells the bot to leave the channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to any channel.")


@client.command(name='pause', help='To pause song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything right now")


@client.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")


@client.command(name='Stop', help='Stops the songs')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


client.run(TOKEN)
