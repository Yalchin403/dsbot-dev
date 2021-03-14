import discord
from discord.ext import commands
from discord.utils import get, find


class RemoveReactionCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):

        guild_id = str(payload.guild_id)
        message_id = str(payload.message_id)
        emoji = str(payload.emoji)
        user = payload.member

        role = await self.client.pg_con.fetch("SELECT * FROM roles WHERE msg_id = $1 AND guild_id = $2 AND emoji = $3", message_id, guild_id, emoji)
        if role:
            role = await self.client.pg_con.fetchrow("SELECT * FROM roles WHERE msg_id = $1 AND guild_id = $2 AND emoji = $3", message_id, guild_id, emoji)        
            role_name = role['role']
            guild = self.client.get_guild(id=int(guild_id))
            member = find(lambda m : m.id == payload.user_id, guild.members)
            role = get(guild.roles, name=role_name)
            if role == get(guild.roles, name="verified_members"):
                await member.add_roles(get(guild.roles, name="unverified_members"))
            await member.remove_roles(role)

def setup(client):
    client.add_cog(RemoveReactionCog(client))