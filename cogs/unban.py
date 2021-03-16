import discord
from discord.ext import commands


class UnbanCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, member, reason="Not specified"):
        banned_users = await ctx.message.guild.bans()
        member_name, member_discriminator = member.split("#")

        for banned_entry in banned_users:
            banned_user = banned_entry.user

            if (banned_user.name, banned_user.discriminator) == (member_name, member_discriminator):
                await ctx.message.guild.unban(banned_user)
                message = f"{member} unbanned. Reason: {reason}"
                embed = discord.Embed(title="Unbanned", description= message, color= discord.Color.purple())
                await ctx.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.message.author.mention}, you don't have permission to use this command")
    
def setup(client):
    client.add_cog(UnbanCog(client))