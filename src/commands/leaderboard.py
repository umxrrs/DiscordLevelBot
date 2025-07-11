from discord.ext import commands
import discord
import aiosqlite

async def leaderboard_command(ctx):
    async with aiosqlite.connect('leveling.db') as db:
        async with db.execute('SELECT user_id, xp, level FROM users WHERE guild_id = ? ORDER BY xp DESC LIMIT 10',
                             (ctx.guild.id,)) as cursor:
            users = await cursor.fetchall()
    if not users:
        await ctx.send("No users on the leaderboard yet!")
        return
    embed = discord.Embed(title="Leaderboard", color=discord.Color.blue())
    for i, (user_id, xp, level) in enumerate(users, 1):
        user = await ctx.bot.get_user(int(user_id))
        embed.add_field(name=f"{i}. {user.name}", value=f"Level {level} | {xp} XP", inline=False)
    await ctx.send(embed=embed)
