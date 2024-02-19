from pyrogram import Client, filters
import re
import requests
import os, asyncio
import time
from pyrogram.types import *
from telegraph import upload_file

@Client.on_message(filters.regex(r"^https://telegra.ph/file/"))
async def download(client, message):
 try:
    url = message.text
    response = requests.get(url, stream=True)
    if message.text.endswith('.jpg'):

        if response.status_code == 200:
            with open('image.JPEG', 'wb') as f:
                f.write(response.content)

            await message.reply_photo(photo='image.JPEG')
            os.remove('image.JPEG')
    elif message.text.endswith('.mp4'):
        if response.status_code == 200:
            with open('video.mp4', 'wb') as f:
                f.write(response.content)
            await message.reply_video(video='video.mp4')
            os.remove('video.mp4')
        else:      
            await message.reply_text('Failed to decode the telegraph link.')
    else:
        return
 except Exception as e:
        await message.reply_text(f"{e}")
