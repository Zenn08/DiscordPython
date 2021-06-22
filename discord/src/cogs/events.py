# extern libraries
import discord
from discord.ext import commands

class Events(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    # events

    @commands.Cog.listener()
    async def on_ready(self):
        print('Versión del cliente: 0.0.1')
        print(f'Id del cliente: {self.client.user.id}')
        print(f'Nombre del cliente: {self.client.user.name}')
        await self.client.change_presence(status=discord.Status.dnd, activity=discord.Game(name='Helping moderators!'))

# setup
def setup(client):
    client.add_cog(Events(client))
    print('Eventos cargados!')