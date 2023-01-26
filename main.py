import asyncio
from pytgcalls import idle
#from config import api_id, api_hash, bot_token, session_name
import os
import sys
import random
import telethon.utils
from telethon import TelegramClient, events
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls


bot = Client(
    "music",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "handlers"},
)

BOT = TelegramClient('BOT', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)
Op = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'handlers'})
call_py = PyTgCalls(op)

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STARTING PYTGCALLS'S CLIENT")
    await call_py.start()
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
BOT.run_until_disconnected()
