import discord
from discord.ext import commands


class ReadyCog(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("Initiating Bot")

def setup(client):
	client.add_cog(ReadyCog(client))