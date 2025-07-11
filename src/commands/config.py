from discord.ext import commands
import discord
import aiosqlite

@commands.has_permissions(administrator=True)
async def config_command(ctx, action: str, level: int, role: discord.Role):
    if action.lower() not in ['add', 'remove']:
        await ctx.send("Action must be 'add' or 'remove'!")
        return
    async with aiosqlite.connect('leveling.db') as db:
        if action.lower() == 'add':
            await db.execute('INSERT OR REPLACE INTO role_rewards (guild_id, level, role_id) VALUES (?, ?, ?)',
                            (ctx.guild.id, level, role.id))
            await ctx.send(f"Added {role.mention} as reward for level {level}.")
        else:
            await db.execute('DELETE FROM role_rewards WHERE guild_id = ? AND level = ?', (ctx.guild.id, level))
            await ctx.send(f"Removed role reward for level {level}.")
        await db.commit()
