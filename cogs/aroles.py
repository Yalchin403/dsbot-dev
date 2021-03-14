import discord
from discord.ext import commands


class ARolesCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def aroles(self, ctx, raw_channel_id=None, *args):
        """
        example: ./aroles #roles 🌳=@verified_members
        There should be no space between emoji, equal sign, and
        role.
        """
        guild_id = str(ctx.guild.id)
        channel_id = raw_channel_id.strip('<#>')
        channel = self.client.get_channel(int(channel_id))
        pairs = dict()

        for item in args:
            polished = item.split('=')
            emoji = polished[0]
            role_raw = polished[1]
            role_id = int(role_raw.strip('<@&>'))
            for role in ctx.guild.roles:
                if role_id == role.id:
                    role_name = role.name
                    pairs[emoji] = role_name
        
        message = ""
        for item in pairs:
            message += f"{item} - {pairs[item]}\n\n"

        message = await channel.send(message)
        message_id = str(message.id)

        for item in pairs:
            await message.add_reaction(item)
        

        for emoji in pairs:
            await self.client.pg_con.execute("INSERT INTO roles (role, msg_id, guild_id, emoji) VALUES ($1, $2, $3, $4)", pairs[emoji], message_id, guild_id, emoji)

    @aroles.error
    async def aroles_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.message.author.mention}, you don't have permission to use this command")

    
def setup(client):
    client.add_cog(ARolesCog(client))