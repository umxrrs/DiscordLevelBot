from discord.ext import commands
import discord
from utils.rank_card import create_rank_card
from database.db import get_user
from utils.xp_math import calculate_level, calculate_xp_for_level

async def rank_command(ctx):
    user = await get_user(ctx.author.id, ctx.guild.id)
    if not user:
        await ctx.send("You have no XP yet!")
        return
    xp, level = user[2], user[3]
    next_level_xp = calculate_xp_for_level(level + 1)
    rank_card = create_rank_card(ctx.author, xp, level, next_level_xp)
    await ctx.send(file=discord.File(rank_card, 'rank.png'))
