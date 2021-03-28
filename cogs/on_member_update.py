import discord
from discord.ext import commands


class UpdateCog(commands.Cog):
    def __init__(self, client):
            self.client = client

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        user_id = str(before.id)
        guild_id = str(before.guild.id)
        roles_list = [role.name for role in after.roles]
        db_user = await self.client.pg_con.fetch("SELECT * FROM user_levels WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
        if db_user:
            await self.client.pg_con.execute("UPDATE user_levels SET roles = $1 WHERE user_id = $2 AND guild_id = $3", roles_list, user_id, guild_id)
def setup(client):
        client.add_cog(UpdateCog(client))