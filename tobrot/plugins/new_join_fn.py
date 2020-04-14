#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


from tobrot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"?Kechirasiz men faqat @YTUPGROUP guruhida ishlayman siz ham ushbu guruhda mendan bemalol foydalaning.ungacha esa Xayir?")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you ?不?不?不?不", quote=True)
    channel_id = str(AUTH_CHANNEL)[4:]
    message_id = 3
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="botdan foydalanish",
            url="https://t.me/ytubgroup/3"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "Salom Botdan foydalanish uchun ushbu tugmani bosing yoki <a href='https://t.me/c/{channel_id}/{message_id}'>ushbu saxifaga kiring</a>",
        quote=True,
        reply_markup=reply_markup
    )



async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="read this?",
            url="https://t.me/YTUPGROUP"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "please use @YTUPBOT",
        quote=True,
        reply_markup=reply_markup
    )
