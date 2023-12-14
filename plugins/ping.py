import time
import random
from pyrogram import Client, filters
from info import ADMINS

CMD = "."

@Client.on_message(filters.user(ADMINS) & filters.command("ping" ,CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"<b>🏓 Pong!\n<code>{time_taken_s:.3f} ms</code>\n</b>")
    
