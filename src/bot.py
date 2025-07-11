import discord
from discord.ext import commands
import json
import asyncio
from database.db import init_db, get_user, update_user
from utils.xp_math import calculate_level, calculate_xp_for_level
from commands.rank import rank_command
from commands.leaderboard import leaderboard_command
from commands.addxp import addxp_command
from commands.config import config_command

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await init_db()
    print(f'{bot.user} is online!')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    user = await get_user(message.author.id, message.guild.id)
    xp = user[2] if user else 0
    xp += 15  # Fixed XP for simplicity
    level = calculate_level(xp)
    if user:
        await update_user(message.author.id, message.guild.id, xp, level)
    else:
        await update_user(message.author.id, message.guild.id, xp, level)
    if user and user[3] < level:
        await message.channel.send(f'Congrats {message.author.mention}, you reached level {level}!')
    await bot.process_commands(message)

bot.command()(rank_command)
bot.command()(leaderboard_command)
bot.command()(addxp_command)
bot.command()(config_command)

with open('config/config.json') as f:
    config = json.load(f)
bot.run(config['token'])
