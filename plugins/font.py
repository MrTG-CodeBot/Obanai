from pyrogram import Client, filters
from plugins.sd_bots.font_list import Font
from info import REQUESTED_CHANNEL

@Client.on_message(filters.command("font"))
async def stylize_text(client, message):
    text_to_stylize = message.text.split(" ", 1)[1]  
    stylized_text = Font.SD(text_to_stylize)  

    await message.reply_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴛᴇxᴛ: <code>{stylized_text}</code>")
    await client.send_message(REQUESTED_CHANNEL, text=f"ʀᴇǫᴜᴇsᴛᴇᴅ ғʀᴏᴍ {message.from_user.mention}\n ᴛᴇxᴛ ɪs {text_to_stylize}")
