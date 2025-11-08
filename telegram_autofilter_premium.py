from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

API_ID = int(os.getenv("API_ID", 21930652))
API_HASH = os.getenv("API_HASH", "6cf4623177849a4e534963d98446792e")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7852466875:AAHKWS6s0JVAReFLo6YoFSmKk-hXtds0u0Y")
OWNER_ID = int(os.getenv("OWNER_ID", 7310926033))
CHANNEL_ID = int(os.getenv("CHANNEL_ID", -1002676537585))

bot = Client("AutoFilterBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(_, message):
    buttons = [
        [InlineKeyboardButton("Channel", url="https://t.me/yourchannel")],
        [InlineKeyboardButton("Request Movie", callback_data="request")]
    ]
    await message.reply_text(
        f"Hi {message.from_user.first_name} 👋\n\nI’m your Auto Filter Bot!",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@bot.on_callback_query()
async def callback_handler(_, query):
    if query.data == "request":
        await query.message.reply_text("Send me the movie name you want!")

print("✅ Bot is running...")
bot.run()
