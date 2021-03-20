import discord
from discord.ext import commands


class ReloadCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, cog):
    	try:
    		self.client.reload_extension(f'cogs.{cog}')

    	except:
    		await ctx.send(f"It was not possible to reload {cog}.py")
    		return
    	await ctx.send(f'Reloaded {cog}.py!')
    	
def setup(client):
    client.add_cog(ReloadCog(client))