import discord
from discord.ext import commands
from discord.utils import get, find


class ListUsers(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    # command structure ./show Python no need to take @ sign before role name
    # will display top ten user with Python role (only if user has also verified_member role)
    async def showMe(self, ctx, role):
        # get 20 users from roles_exp database
        # by sorting their roles and exp
        user_id = str(ctx.message.author.id)
        guild_id = str(ctx.message.guild.id)
        guild = ctx.message.guild
        users = await self.client.pg_con.fetch("SELECT * FROM user_levels WHERE guild_id = $1 AND $2 = ANY (roles) ORDER BY exp DESC LIMIT 20", guild_id, role)
        user_list = ''
        count = 1
        for user in users:
            db_user_id = int(user['user_id'])
            db_user = guild.get_member(db_user_id)
            user_list += f'{count}. {db_user.mention}\n'
            count += 1
            title = f"Top (up to) 20 members with {role} role"
            description = user_list + "\nPlease make sure you don't use excessive tags, and not using './list' command excessively\nUsers not obeying this rules will be banned!"
            embed = discord.Embed(title=title, description=description, color=db_user.color)


        await ctx.message.channel.send(embed=embed)

def setup(client):
    client.add_cog(ListUsers(client))