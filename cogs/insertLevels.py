import discord
from discord.ext import commands
import json


class InsertLevelsCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def insertLevels(self, ctx):
        path = '/media/mrrootlog/Desktop/webDev/discord/bot_dev/cogs/level.json'
        with open(path, 'r') as file:
            data = json.load(file)
        guild_id = str(ctx.guild.id)
        for user_id in data:
            exp = data[user_id]['exp']
            lvl = data[user_id]['lvl']
            user = await self.client.pg_con.fetch("SELECT * FROM user_levels WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            if user:
                await self.client.pg_con.execute("UPDATE user_levels SET exp = $1 WHERE user_id = $2 AND guild_id = $3", exp, user_id, guild_id)
                await self.client.pg_con.execute("UPDATE user_levels SET lvl = $1 WHERE user_id = $2 AND guild_id = $3", lvl, user_id, guild_id)
            else:
                await self.client.pg_con.execute("INSERT INTO user_levels (user_id, guild_id, exp, lvl) VALUES ($1, $2, $3, $4)", user_id, guild_id, exp, lvl)
def setup(client):
    client.add_cog(InsertLevelsCog(client))