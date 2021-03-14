import discord
from discord.ext import commands
class PruneCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["detect"])
    @commands.has_permissions(administrator=True)
    async def prune(self, ctx):
        count = 0
        guild = ctx.message.guild
        users = [user for user in guild.members]
        
        for user in users:
            for role in user.roles:
                if role.name == "unverified_members":
                    count += 1
                    await ctx.send(f"{user} kicked. Reason: {user} is not verified")
                    await user.kick(reason="User is not verified")
        await ctx.send(f"{count} unverified users have been deleted")

    @prune.error
    async def prune_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.message.author.mention}, you don't have permission to use this command")
        
def setup(client):
        client.add_cog(PruneCog(client))



