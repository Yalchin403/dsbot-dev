import discord
from discord.ext import commands


class DeleteCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def delete_removed(self, ctx):
        users = ctx.message.guild.members
        guild_id = str(ctx.message.guild.id)
        db_users = await self.client.pg_con.fetch("SELECT * FROM user_levels WHERE guild_id = $1", guild_id)
        user_ids = [str(user.id) for user in users]
        db_user_ids = [db_user["user_id"] for db_user in db_users]
        for db_user_id in db_user_ids:
            if db_user_id not in user_ids:
                try:
                    # check if user is not bot
                    await self.client.pg_con.execute("DELETE FROM user_levels WHERE user_id = $1 AND guild_id = $2", db_user_id, guild_id)
                except:
                    print("Could not delete user from database")
        await ctx.send("deleted all removed users")


def setup(client):
    client.add_cog(DeleteCog(client))