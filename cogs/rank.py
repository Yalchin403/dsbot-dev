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
            embed = discord.Embed(title="Level Check", description=f"{member.mention}, your level is {level}", color=discord.Color.purple())
            await ctx.message.channel.send(embed=embed)
        else:
            level = 1
            embed = discord.Embed(title="Levelled Check", description=f"{member.mention}, your levelled is {level}", color=discord.Color.purple())
            await ctx.message.channel.send(embed=embed)
    
def setup(client):
    client.add_cog(RemoveCog(client))