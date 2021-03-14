import discord
from discord.ext import commands
import asyncio
from pathlib import Path
import json


class RemoveCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member):

        user_id = str(member.id)
        guild_id = str(member.guild.id)
        user = await self.client.pg_con.fetch("SELECT * FROM user_levels WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
        if user:
            await self.client.pg_con.execute("UPDATE user_levels SET exp = $1 WHERE user_id = $2 AND guild_id = $3", 0, user_id, guild_id)
            await self.client.pg_con.execute("UPDATE user_levels SET lvl = $1 WHERE user_id = $2 AND guild_id = $3", 1, user_id, guild_id)

def setup(client):
    client.add_cog(RemoveCog(client))