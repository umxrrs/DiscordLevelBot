from discord.ext import commands
import discord
from database.db import get_user, update_user
from utils.xp_math import calculate_level

@commands.has_permissions(administrator=True)
async def addxp_command(ctx, member: discord.Member, amount: int):
    if amount <= 0:
        await ctx.send("XP amount must be positive!")
        return
    user = await get_user(member.id, ctx.guild.id)
    xp = user[2] + amount if user else amount
    level = calculate_level(xp)
    await update_user(member.id, ctx.guild.id, xp, level)
    await ctx.send(f"Added {amount} XP to {member.mention}. New level: {level}")
