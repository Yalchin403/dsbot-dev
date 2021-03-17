import discord
from discord.ext import commands


class RemoveCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rank(self, ctx):
        member = ctx.message.author
        user_id = str(ctx.message.author.id)
        guild_id = str(ctx.guild.id)
        user = await self.client.pg_con.fetch("SELECT * FROM user_levels WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
        if user:
            user = await self.client.pg_con.fetchrow("SELECT * FROM user_levels WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            level = user['lvl']
            all_users = await self.client.pg_con.fetch('SELECT * FROM user_levels ORDER BY lvl DESC')
            rank = all_users.index(user)
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
            embed.set_author(name=f"Level - {member}",icon_url=member.avatar_url)
            embed.add_field(name="Level", value=level)
            embed.add_field(name="RANK", value=rank+1)
            embed.add_field(name="XP", value=user['exp'])
            await ctx.message.channel.send(embed=embed)
        else:
            level = 1
            embed = discord.Embed(title="Levelled Check", description=f"{member.mention}, your levelled is {level}", color=member.color)
            await ctx.message.channel.send(embed=embed)
    
def setup(client):
    client.add_cog(RemoveCog(client))