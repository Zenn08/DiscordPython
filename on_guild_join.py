    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            file = open(f'guilds/{guild.id}') # this makes a new file with the id of the guild if a guild invites the bot
            print(f'{guild.name} invited the bot another time!')
        except:
            file = open(f'guilds/{guild.id}', 'x')
            file.write(guild.name)

        await guild.owner.send(f"""
        
        Hi, {guild.owner.mention}! Thanks for invite me in **{guild.name}**.

        If you need support, enter in my discord server:
        https://discord.gg/yJuG6nnRJA

Have a nice day! 

        """)

        # creates a 'muted' role if the role doesn't exists
        role = discord.utils.get(guild.roles, name='Muted')

        if not role:
            role = await guild.create_role(name='Muted', colour=0x546e7a)

            for channel in guild.channels:
                await channel.set_permissions(role, speak=False, send_messages=False, read_message_history=True, read_messages=True)
