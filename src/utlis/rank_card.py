from PIL import Image, ImageDraw, ImageFont
import aiohttp
import io

async def create_rank_card(user, xp, level, next_level_xp):
    img = Image.open('assets/background.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    async with aiohttp.ClientSession() as session:
        async with session.get(str(user.avatar.url)) as resp:
            avatar = Image.open(io.BytesIO(await resp.read())).resize((100, 100))
    img.paste(avatar, (50, 50))
    draw.text((160, 50), f"{user.name}", fill="white", font=font)
    draw.text((160, 80), f"Level: {level}", fill="white", font=font)
    draw.text((160, 110), f"XP: {xp}/{next_level_xp}", fill="white", font=font)
    progress = (xp / next_level_xp) * 200
    draw.rectangle((160, 140, 160 + progress, 160), fill="blue")
    output = io.BytesIO()
    img.save(output, format='PNG')
    output.seek(0)
    return output
