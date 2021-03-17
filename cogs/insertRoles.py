import discord
from discord.ext import commands
from pathlib import Path
import json


class InsertRolesCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def insertRoles(self, ctx):
        path = '/media/mrrootlog/Desktop/webDev/discord/bot_dev/cogs/test.json'
        with open(path, 'r') as file:
            data = json.load(file)
        
        for msg_id in data:
            guild_id = data[msg_id]["guild_id"]
            for emoji in data[msg_id]["pairs"]:
                await self.client.pg_con.execute("INSERT INTO roles (msg_id, guild_id, emoji, role) VALUES ($1, $2, $3, $4)", msg_id, guild_id, emoji, data[msg_id]['pairs'][emoji])

def setup(client):
    client.add_cog(InsertRolesCog(client))