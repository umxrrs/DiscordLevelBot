# DiscordLevelBot
---

A customizable Discord leveling system bot built with Python and `discord.py`. Users earn XP by sending messages, level up, and receive role rewards. Features include rank cards, leaderboards, and admin controls.

(Idea by mee6 bot)

---

## Features
- **XP and Levels**: Users gain 15 XP per message, with levels calculated as `level = sqrt(xp / 100)`.
- **Rank Cards**: Visual rank cards generated with `Pillow` (`!rank`).
- **Leaderboard**: Display top 10 users by XP (`!leaderboard`).
- **Role Rewards**: Assign roles at specific levels (`!config add <level> <role>`).
- **Admin Commands**: Add XP (`!addxp <user> <amount>`), configure roles.
- **Database**: Uses SQLite (`aiosqlite`) for lightweight storage.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/umxrrs/DiscordLevelBot.git
   cd DiscordLevelBot
   ```
---

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
---

3. Create a Discord bot in the [Discord Developer Portal](https://discord.com/developers/applications) and get the token.
---
5. Add the token to `config/config.json`:
   ```json
   {
    "token": "YOUR_BOT_TOKEN_HERE"
   }
   ```
---

5. Place a 500x200 `background.png` in the `assets/` folder for rank cards.
---

7. Run the bot:
   ```bash
   python src/bot.py
   ```

# Commands
`!rank`: Display your rank card with XP and level.
`!leaderboard`: Show the top 10 users by XP.
`!addxp <user> <amount>`: (Admin) Add XP to a user.
`!config <add/remove> <level> <role>`: (Admin) Set or remove role rewards for a level.

---

# Requirements
See `requirements.txt` for dependencies, including:

- `discord.py`
- `aiosqlite`
- `Pillow`
- `aiohttp`
---

### Hosting
**Local**: Run `python src/bot.py.`
**Cloud**: Deploy on Heroku, Replit, or a VPS. Ensure `leveling.db` is persistent.
**Note**: Provide your own `background.png` for rank cards.

---

### Contributing
Contributions are welcome! Not really need of it, ill keep updating this, just let me know whatever the issue is.

License
MIT License (see LICENSE).

### Credits:
- Built by: Umar/umxrrs
