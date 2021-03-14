import discord
from discord.ext import commands


class RemoveCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["verified?"])
    async def amIVerified(self ,ctx):
	    count = 0
	    guild = ctx.message.guild
	    member = ctx.message.author
	    role_names = [role.name for role in member.roles]
	    role_names[0] = "everyone"

	    if "verified_members" in role_names:
	        await ctx.send(f"Yes, {member.mention}, you are indeed verified!")
	    else:
	        await ctx.send("Sorry, you are not verified...")

def setup(client):
    client.add_cog(RemoveCog(client))