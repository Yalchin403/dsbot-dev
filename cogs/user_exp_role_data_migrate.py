import discord
from discord.ext import commands



class InsertCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def insert(self, ctx):
        #guild_id
            # user-id
                # user roles
                # user exp
        # will dump it as a string JSON format
        # then load or retrieve it as Python dict.

        users = ctx.guild.members
        guild_id = str(ctx.guild.id)
        flag = None
        for user in users:
            user_id = str(user.id)
            roles_list = [role.name for role in user.roles]
            db_user = await self.client.pg_con.fetch("SELECT * FROM user_levels WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            if db_user:
                await self.client.pg_con.execute("UPDATE user_levels SET roles = $1 WHERE user_id = $2 AND guild_id = $3", roles_list, user_id, guild_id)
                flag = 1
        if flag:
            await ctx.send("Successfully inserted data into database!")
            
    @insert.error
    async def insert_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.message.author.mention}, you don't have permission to use this command")
            

    
def setup(client):
    client.add_cog(InsertCog(client))