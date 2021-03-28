import discord
from discord.ext import commands


class RemoveCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        title = "Commands that verified users can use:"
        description = """./help - will display the commands that verified members can use\n./rules - will list the rules\n./ping - will response you pong\n./8ball "Your question" - will randomly answer your question\n./verified? - will tell you if you are verified\n./rank - to check your rank\n./show nameOfRole - will show list of top 20 most active users with specified role \n\nMake sure you use ./verified? , ./ping and ./8ball, commands only in general channel and don't use it excessively."""
        embed = discord.Embed(title=title, description=description, color=discord.Color.purple())
        await ctx.send(embed=embed)

    
def setup(client):
    client.add_cog(RemoveCog(client))