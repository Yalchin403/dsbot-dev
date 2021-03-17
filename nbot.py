#!/usr/bin/env python3
import discord, os
import asyncpg
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
from bad_words import polished_data
from AntiSpam import AntiSpamHandler

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
command_prefix = os.getenv('command_prefix')
client = commands.Bot(command_prefix = command_prefix, intents = intents, help_command=None)
client.handler = AntiSpamHandler(client)
database = os.getenv('database')
user = os.getenv('user')
password = os.getenv('password')

@client.event
async def on_message(message):
    if message.content != "./rank" and message.channel.id == 817199997770137600:
        try:
            await message.author.send(f"You can only check your rank in {message.channel.mention}.")
            await message.delete()
        except:
            pass
    else:
        await client.process_commands(message)
        await client.handler.propagate(message)
        if "discord.gg/" in message.content.lower() or "discordapp.com/invite/" in message.content.lower():
            await message.author.send("sending server invites breaks the rules, if you think this is a mistake please contact the moderator.")
            await message.delete()
        
        message_list = message.content.lower().split(' ')
        for word in polished_data:
            if word in message_list:
                await message.author.send("sending swear words breaks the rules, if you think this is a mistake please contact the moderator.")
                await message.delete()
                break
        try:
            user = message.author
            user_id = str(message.author.id)
            guild_id = str(message.guild.id)
            channel_ids = [803586866619088946, 785614476241666048, 803591038349738014, 785910036953301033, 810641490014502972, 817199997770137600, 817769219898474536]
        except:
            pass
        if not user.bot and message.channel.id not in channel_ids:
            
            user = await client.pg_con.fetch("SELECT * FROM user_levels WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            if not user:
                await client.pg_con.execute("INSERT INTO user_levels (user_id, guild_id, exp, lvl) VALUES ($1, $2, 0, 1)", user_id, guild_id)
                embed = discord.Embed(title="You Leveled Up", description=f"{message.author.mention} your level is 1", color=discord.Color.purple())
                await message.channel.send(embed=embed)
            else:
                user = await client.pg_con.fetchrow("SELECT * FROM user_levels WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
                exp = user['exp'] + 5
                current_lvl = user['lvl']
                new_lvl = int(exp ** 0.25)
                if current_lvl < new_lvl:
                    await client.pg_con.execute("UPDATE user_levels SET exp = $1 WHERE user_id = $2 AND guild_id = $3", exp, user_id, guild_id)
                    await client.pg_con.execute("UPDATE user_levels SET lvl = $1 WHERE user_id = $2 AND guild_id = $3", new_lvl, user_id, guild_id)
                    embed = discord.Embed(title="You Leveled Up", description=f"{message.author.mention} your level is {new_lvl}", color=discord.Color.purple())
                    await message.channel.send(embed=embed)
                else:
                    await client.pg_con.execute("UPDATE user_levels SET exp = $1 WHERE user_id = $2 AND guild_id = $3", exp, user_id, guild_id)

async def create_db_pool():
    client.pg_con = await asyncpg.create_pool(database=database, user=user, password=password, host="127.0.0.1")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload.extension(f'cogs.{extension}')

for filename in  os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.loop.run_until_complete(create_db_pool())
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)