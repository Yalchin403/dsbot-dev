import discord
from discord.ext import commands
from bad_words import polished_data


class EMessage(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()

    async def on_message_edit(self, before, after):
        if "discord.gg/" in after.content.lower() or "discordapp.com/invite/" in after.content.lower():
            await after.author.send("Sending server invites breaks the rules, if you think this is a mistake please contact the moderator.")
            await after.delete()

        message_list = after.content.lower().split(' ')
        for word in polished_data:

            if word in message_list:
                await after.author.send("Sending swear words breaks the rules, if you think this is a mistake please contact the moderator.")
                await after.delete()
                break

def setup(client):
    client.add_cog(EMessage(client))