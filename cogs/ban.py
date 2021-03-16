import discord
from discord.ext import commands


class BanCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member:discord.Member, *, reason="Not specified"):
        await member.ban(reason=reason)
        message = f"{member} banned. Reason: {reason}"
        embed = discord.Embed(title="Banned", description= message, color= discord.Color.purple())
        await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.message.author.mention}, you don't have permission to use this command")

    
def setup(client):
    client.add_cog(BanCog(client))