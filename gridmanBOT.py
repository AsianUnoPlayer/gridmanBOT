import discord
import bot_command
from datetime import datetime
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def sendtime(ctx):
    await ctx.send(datetime.now())

@client.command()    
async def sendwiki(ctx, test):
    underscore = arg.replace(" ", "_")
    print(underscore)
    await ctx.send("https://en.wikipedia.org/wiki/" + underscore)

client.run('OTM5NjE3NDcxNzc2ODM3NzAy.Yf7c9g.G5zj5xlzjpiKeRo1tCR3ooLpbaU')