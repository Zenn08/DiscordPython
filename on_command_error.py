    # error event
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title= '<:blurplecross:857312303078440980> Command not found!'
            )
            return await ctx.send(embed=embed)

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title= '<:3663syntax:858972511273877545> Missing required arguments!'
            )
            return await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title= '<:6985moderator:858973491189383198> Missing permissions!'
            )

            return await ctx.send(embed=embed)

        if isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                title= '<:3446blurplecertifiedmoderator:858974234767917076> Bot missing permissions!'
            )

            return await ctx.send(embed=embed)
