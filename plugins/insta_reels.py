#The mastermind 

import pyrogram 
from pyrogram import Client, filters

@Client.on_message(filters.command("insta"))
async def insta(client, message):
    if len(message.command) < 2:
        await message.reply("Please provide the Instagram reel ID.")
    else:
        query = " ".join(message.command[1:])

        reels = f"<a href='https://www.ddinstagram.com/reel/{query}'>https://www.instagram.com/reel/{query}</a>"

        await message.reply(reels)
