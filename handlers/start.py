#KANGERS_GIVE_CREDITS
import os
from pyrogram import filters
from main import bot

START_TEXT = """
Hi <b>{}</b> 👋
I can play music & stream videos in Telegram group voice chats. 
Make your own bot using below source code.
"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📨 Support", url="https://t.me/TITANIUM_XYZ"),
            InlineKeyboardButton("📚 Source Code", url="https://github.com/TitaniumOp/MusicBot")
        ]
    ]
)
