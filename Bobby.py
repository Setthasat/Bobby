from ast import Return
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from datetime import datetime, timedelta
from email import message
from http import client
from multiprocessing.connection import Client
from async_timeout import timeout
from youtube_dl import YoutubeDL
import youtube_dl
import discord
import asyncio


bot = commands.Bot(command_prefix='!Bobby ',help_command=None)
#client = discord.Client()
message_cout = datetime.now()


@bot.command()
async def help(ctx):
    emBed = discord.Embed(title='Bobby help', description='All availabele bot commands', color=0x42f5a7)
    emBed.add_field(name='!Bobby help', value='Get help command', inline=False)
    emBed.add_field(name='!Bobby kick', value='Kick Bobby from channel', inline=False)
    emBed.add_field(name='!Bobby play <url>', value='Just play a music', inline=False)
    emBed.add_field(name='!Bobby stop', value='Stop the playing music', inline=True)
    emBed.add_field(name='!Bobby pause', value='Pause the playing music', inline=True)
    emBed.add_field(name='!Bobby resume', value='Resume the playing music', inline=True)
    emBed.set_thumbnail(url='https://i.kym-cdn.com/photos/images/newsfeed/001/230/774/9b2.gif')
    emBed.set_footer(text="Don't forget that Queen elizabeth is the best girl in the world❤️", icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRs_uI8-JYjISppu14g9xsH009DGNjYDjSW2xrJTFsrgDd30uhLLMJ9g0CBWcKPc2G2&usqp=CAU')
    await ctx.channel.send(embed=emBed)

@bot.command()
async def test(ctx):
    await ctx.channel.send('hey boi')

@bot.event
async def on_ready():
    print(f'logged is as {bot.user}')

@bot.event
async def on_message(message):
    global message_cout
    if message.content == '!Bobby say hi' and datetime.now() >= message_cout:
        message_cout = datetime.now() + timedelta(seconds=7)
        await message.channel.send(f"Hey {str(message.author.name)} i'm Bobby")
    elif message.content == '!Bobby who created you Bobby what do you want?' and datetime.now() >= message_cout :
        message_cout = datetime.now() + timedelta(seconds=7)
        await message.channel.send('Safe created me')
    elif message.content == '!Bobby who is the best girl the this world' and datetime.now() >= message_cout :
        message_cout = datetime.now() + timedelta(seconds=7)
        await message.channel.send('Sure she is Queen elizabeth she so fucking cute❤️❤️')
    elif message.content == '!Bobby well' and datetime.now() >= message_cout :
        message_cout = datetime.now() + timedelta(seconds=7)
        await message.channel.send('ty i love you too ❤️')
    
    if message.content == '!Bobby get out':
        await message.channel.send("Goodbye mate i'll come if you want GLHF")
        await bot.logout()
    if message.content == '!Bobby come here':
        await message.channel.send("Now i'm online what do you want bro?")
        await bot.login()
    await bot.process_commands(message)

@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_client == None:
        await ctx.channel.send('Joined')
        await channel.connect()
        voice_client = get(bot.voice_clients, guild=ctx.guild)
    YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist' : 'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not voice_client.is_playing():
        with YoutubeDL(YDL_OPTIONS)as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
                voice_client.play(discord.FFmpegPCMAudio(URL))
                voice_client.playing()
    else :
        await ctx.channel.send('Already playinng song')
        return


@bot.command()
async def kick(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice == None:
        await ctx.channel.send('Bot is not connect the channel')
        return
    if voice.channel != ctx.author.voice.channel: #ให้stopทำงานโดยคนที่อยู่ในchannelเท่านั้น
        await ctx.channel.send(f'The bot is currently connect to {voice.channel}')
        return
    await ctx.channel.send("Why you kick me from channel i'm gonna cry T^T")
    await ctx.voice_client.disconnect()
    
@bot.command()
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice == None:
        await ctx.channel.send('Bot is not connect the channel')
        return
    if voice.channel != ctx.author.voice.channel: #ให้stopทำงานโดยคนที่อยู่ในchannelเท่านั้น
        await ctx.channel.send(f'The bot is currently connect to {voice.channel}')
        return
    await ctx.channel.send('Bobby stop the playing music')
    voice.stop()

@bot.command()
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice == None:
        await ctx.channel.send('Bot is not connect the channel')
        return
    if voice.channel != ctx.author.voice.channel: #ให้stopทำงานโดยคนที่อยู่ในchannelเท่านั้น
        await ctx.channel.send(f'The bot is currently connect to {voice.channel}')
        return
    await ctx.channel.send('Bobby pause the playing music')
    voice.pause()

@bot.command()
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice == None:
        await ctx.channel.send('Bot is not connect the channel')
        return
    if voice.channel != ctx.author.voice.channel: #ให้stopทำงานโดยคนที่อยู่ในchannelเท่านั้น
        await ctx.channel.send(f'The bot is currently connect to {voice.channel}')
        return
    await ctx.channel.send('Bobby resume the playing music')
    voice.resume()    


bot.run('<Bot Token>')
