#KANGERS_GIVE_CREDITS
import os
import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from main import bot

START_TEXT = """
Hi <b>{}</b> 👋
I can play music & stream videos in Telegram group voice chats. 
Make your own bot using below source code.
"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📨 Support 🚩", url="https://t.me/TeamUltronX"),
            InlineKeyboardButton("🔥 Owner 🔥", url="https://t.me/officiallycute")
        ]
    ]
)


@bot.on_message(filters.command("start") & filters.private)
async def start_private(_, message):
    msg = START_TEXT.format(message.from_user.mention)
    await message.reply_text(text = msg,
                             reply_markup = START_BUTTONS)
    

@bot.on_message(filters.command("start") & filters.group)
async def start_group(_, message):
    await message.reply_text("🎧 <i>Music player is running.</i>")
    
