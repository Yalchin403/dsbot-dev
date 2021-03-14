#!/usr/bin/env python3
import discord, os
import asyncpg
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
command_prefix = os.getenv('command_prefix')
client = commands.Bot(command_prefix = command_prefix, intents = intents, help_command=None)
database = os.getenv('database')
user = os.getenv('user')
password = os.getenv('password')

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