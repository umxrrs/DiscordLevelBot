import aiosqlite

async def init_db():
    async with aiosqlite.connect('leveling.db') as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT,
                guild_id TEXT,
                xp INTEGER,
                level INTEGER,
                PRIMARY KEY (user_id, guild_id)
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS role_rewards (
                guild_id TEXT,
                level INTEGER,
                role_id TEXT,
                PRIMARY KEY (guild_id, level)
            )
        ''')
        await db.commit()

async def get_user(user_id, guild_id):
    async with aiosqlite.connect('leveling.db') as db:
        async with db.execute('SELECT * FROM users WHERE user_id = ? AND guild_id = ?', (user_id, guild_id)) as cursor:
            return await cursor.fetchone()

async def update_user(user_id, guild_id, xp, level):
    async with aiosqlite.connect('leveling.db') as db:
        await db.execute('INSERT OR REPLACE INTO users (user_id, guild_id, xp, level) VALUES (?, ?, ?, ?)',
                        (user_id, guild_id, xp, level))
        await db.commit()
