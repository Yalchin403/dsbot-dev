import discord, os
from discord.ext import commands
from bad_words import polished_data
from pathlib import Path



class MessageCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content != "./rank" and message.channel.id == 817409301479948338:
            await message.author.send(f"You can only check your rank in {message.channel.mention}.")
            await message.delete()
        else:
            if "discord.gg/" in message.content.lower() or "discordapp.com/invite/" in message.content.lower():
                await message.author.send("Sending server invites breaks the rules, if you think this is a mistake please contact the moderator.")
                await message.delete()
            
            message_list = message.content.lower().split(' ')
            for word in polished_data:
                if word in message_list:
                    await message.author.send("Sending swear words breaks the rules, if you think this is a mistake please contact the moderator.")
                    await message.delete()
                    break

            user = message.author
            user_id = str(message.author.id)
            guild_id = str(message.guild.id)
            channel_ids = [813164947848167464, 814936857300566066]
            if not user.bot and message.channel.id not in channel_ids:
                
                user = await self.client.pg_con.fetch("SELECT * FROM user_levels WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
                if not user:
                    await self.client.pg_con.execute("INSERT INTO user_levels (user_id, guild_id, exp, lvl) VALUES ($1, $2, 0, 1)", user_id, guild_id)
                    embed = discord.Embed(title="You Leveled Up", description=f"{message.author.mention} your level is 1", color=discord.Color.purple())
                    await message.channel.send(embed=embed)
                else:
                    user = await self.client.pg_con.fetchrow("SELECT * FROM user_levels WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
                    exp = user['exp'] + 5
                    current_lvl = user['lvl']
                    new_lvl = int(exp ** 0.25)
                    if current_lvl < new_lvl:
                        await self.client.pg_con.execute("UPDATE user_levels SET exp = $1 WHERE user_id = $2 AND guild_id = $3", exp, user_id, guild_id)
                        await self.client.pg_con.execute("UPDATE user_levels SET lvl = $1 WHERE user_id = $2 AND guild_id = $3", new_lvl, user_id, guild_id)
                        embed = discord.Embed(title="You Leveled Up", description=f"{message.author.mention} your level is {new_lvl}", color=discord.Color.purple())
                        await message.channel.send(embed=embed)
                    else:
                        await self.client.pg_con.execute("UPDATE user_levels SET exp = $1 WHERE user_id = $2 AND guild_id = $3", exp, user_id, guild_id)

def setup(client):
    client.add_cog(MessageCog(client))