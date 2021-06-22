# external libraries
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# client
client = commands.Bot(command_prefix='.', help_command=None)

# load extensions
client.load_extension('cogs.events')
client.load_extension('cogs.moderator')

# client run and dotenv
load_dotenv()
token = os.getenv("TOKEN")
client.run(token)

