import asyncio
from pyrogram import Client, filters
import requests
import wget 
from info import REQUESTED_CHANNEL


@Client.on_message(filters.command("image"))
async def google_text(client, message):
    try:
        user_query = ' '.join(message.command[1:])
        if not user_query:
            await message.reply_text("")
        encoded_query = user_query.replace(" ", "%20")

        response = requests.get(f"https://api.safone.dev/image?query={encoded_query}&limit=1")
        if response.status_code == 200:
            data = response.json()
            image_data = data['results'][0]
            image_url = image_data['imageUrl']
            downloaded_image = wget.download(image_url)
            await client.send_photo(message.chat.id, downloaded_image)
            await client.send_message(REQUESTED_CHANNEL, text=f"#ɪᴍᴀɢᴇ_sᴇᴀʀᴄʜ\nʜᴇʏ {message.from_user.mention}\nʀᴇǫᴜᴇsᴛ ɪs {user_query}")

    except Exception as e:
       await message.reply_text(f"An error occurred: {e}")
