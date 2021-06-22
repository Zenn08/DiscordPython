# extern libraries
import discord
from discord.ext import commands

class Moderator(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands

        # mute and unmute
    @commands.command(name='mute')
    @commands.has_role('Staff')
    async def Mute(self, ctx, member: discord.Member=None, *, reason='Sin razón!'):
        r = discord.utils.get(ctx.guild.roles, name='Muted')

        # errors
            # none user
        if member == None:
            return await ctx.send('Tiene que insertar el usuario que quieres silenciar.')
            # already muted
        if r in member.roles:
            return await ctx.send(f'{member.mention} ya está **silenciado**!')
        await member.add_roles()
        await member.edit(roles=[r])        
        await ctx.send(f'{member.mention} ha sido muteado por **{ctx.author.display_name}**.')

    @commands.command(name='unmute')
    @commands.has_role('Staff')
    async def UnMute(self, ctx, member: discord.Member=None):
        r = discord.utils.get(ctx.guild.roles, name='Muted')
        r2 = discord.utils.get(ctx.guild.roles, name='Member')

        # errors
            # none user
        if member == None:
            return await ctx.send('Tienes que insertar el usuario .')
            # user not muted
        if not r in member.roles:
            return await ctx.send(f'{member.mention} no está silenciado!')

        await member.remove_roles(r)
        await member.add_roles(r2)
        await ctx.send(f'**{ctx.author.display_name}** le ha quitado el silencio ha {member.mention}.')

# setup
def setup(client):
    client.add_cog(Moderator(client))
    print('Comandos de moderador cargados.')