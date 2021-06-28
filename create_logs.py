    # if the server doesn't have an database, you can make it manualy with this command
    @commands.command(alias=['cl', 'createl', 'clogs'])
    @commands.has_permissions(administrator=True)
    async def createlogs(self, ctx):
        try:
            open(f'guilds/{ctx.guild.id}')
            embed = discord.Embed(
                title = '<:blurplecross:857312303078440980> The logs file already exists!'
            )
            
            await ctx.send(embed=embed)
        except:
            file = open(f'guilds/{ctx.guild.id}', 'x')
            file.write(ctx.guild.name)
            embed = discord.Embed(
                title = "<:blurplecheck:857308308758069328> The logs file has been created! You can watch the logs with '?logs'."
            )
            
            await ctx.send(embed=embed)

    # watch the logs
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def logs(self, ctx):
       try:
           file = open(f'guilds/{ctx.guild.id}', 'r')
           await ctx.send(f'```{file.read()}```')
       except:
            embed = discord.Embed(
                title = "<:blurplecross:857312303078440980> You need to create an logs file with '?createlogs'!"
            )
            
            await ctx.send(embed=embed)
