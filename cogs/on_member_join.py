import discord
from discord.ext import commands
from discord.utils import get, find
import asyncio


class JoinCog(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_member_join(self, member):
	    role = get(member.guild.roles, name="unverified_members")
	    await member.add_roles(role)
	    channel = discord.utils.get(member.guild.channels, name="welcome")
	    rules_channel = discord.utils.get(member.guild.channels, name="rules-and-verification📜")
	    intro_channel = discord.utils.get(member.guild.channels, name="self-introduction")
	    message = f"""Hey {member.mention}, welcome to Partner Up!
Dear {member.mention}, you won't be able to send a message unless and until you accept the rules and also consider that if you don't verify yourself you will be kicked from the server after some time.If you haven't verified yourself yet, please go to {rules_channel.mention} channel and verify yourself by clicking on :ballot_box_with_check: icon.
By the way don't forget to go to {intro_channel.mention} and introduce yourself thoroughly."""
	    await asyncio.sleep(10)
	    await channel.send(message)

def setup(client):
	client.add_cog(JoinCog(client))