import discord
from discord.ext import commands


class KickCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member:discord.Member, *, reason="Not specified"):
        await member.kick(reason=reason)
        message = f"{member} kicked. Reason: {reason}"
        embed = discord.Embed(title="Kicked", description= message, color= discord.Color.purple())
        await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.message.author.mention}, you don't have permission to use this command")

    
def setup(client):
    client.add_cog(KickCog(client))


