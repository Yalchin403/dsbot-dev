import discord
from discord.ext import commands


class RemoveCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()

    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, number):
        mgs = []
        number = int(number) + 1
        await ctx.channel.purge(limit=number)
        title = "Cleared"
        description = f"I've deleted {number-1} messages."
        embed = discord.Embed(title=title, description= description, color= discord.Color.purple())
        message = await ctx.send(embed=embed)
        await asyncio.sleep(4)
        await message.delete()

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.message.author.mention}, you don't have permission to use this command")
    
def setup(client):
    client.add_cog(RemoveCog(client))










