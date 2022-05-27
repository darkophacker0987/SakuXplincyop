import os
from main import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

START_TEXT = """
Hi <b>{}</b> 👋
I can play music & stream videos in Telegram group voice chats. 
Make your own bot using below source code.
"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📨 Support", url="https://t.me/Titanium_Xyz"),
            InlineKeyboardButton("📚 Source Code", url="https://github.com/Titanium/MusicBot")
        ]
    ]
)


@bot.on_message(filters.command("start") & filters.private)
async def start_private(_, message):
    msg = START_TEXT.format(message.from_user.mention)
    await message.reply_text(text = msg,
                             reply_markup = START_BUTTONS)
