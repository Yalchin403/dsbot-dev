import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound


class NotFoundCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self ,ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send("Command, doesn't exists, make sure you don't have typo!")
        else:
            raise error

    
def setup(client):
    client.add_cog(NotFoundCog(client))