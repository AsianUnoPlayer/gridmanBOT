import discord
from discord.ext import commands

from datetime import datetime

client = commands.Bot(command_prefix = '$')

class cool_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @client.command()
    async def sendtime(self, ctx):
        await ctx.send(datetime.now())

    @client.command()    
    async def sendwiki(self, ctx, arg):
        underscore = arg.replace(" ", "_")
        print(underscore + " has been wiki'd")
        await ctx.send("https://en.wikipedia.org/wiki/" + underscore)

def setup(client):
    client.add_cog(cool_commands(client))