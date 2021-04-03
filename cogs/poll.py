import discord
from discord.ext import commands
import random_choice_4_poll 

class RemoveCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()



    @commands.has_permissions(administrator=True)
    async def poll(self, ctx, question, *options):
        n = len(options)
        choices = random_choice_4_poll.random_choice(n)
        title = question
        description = ''
        for i in range(n):
            description += f"{choices[i]} - {options[i]}\n\n"
        embed = discord.Embed(title=title, description=description, color=discord.Color.purple())
        message = await ctx.send(embed=embed)
        for i in range(n):
            await message.add_reaction(choices[i])
        

    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.message.author.mention}, you don't have permission to use this command")
    
def setup(client):
    client.add_cog(RemoveCog(client))






