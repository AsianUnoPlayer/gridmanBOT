import sys
sys.path.append('commands')

import cool_commands
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

cog_files = ['commands.cool_commands']

for cog_file in cog_files:
    client.load_extension(cog_file)
    print("%s has loaded! " % cog_files)

client.run('god i love cute anime girls')