import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import *
from telegraph import upload_file


@Client.on_message(filters.command("telegraph") & filters.private)
async def telegraph_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        return await update.reply_text("Ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ or ᴠɪᴅᴇᴏ.")
    if not ( replied.photo or replied.video ):
        return await update.reply_text("ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀ ᴠᴀʟɪᴅ ᴍᴇᴅɪᴀ")
    text = await update.reply_text("<code>Downloading...</code>", disable_web_page_preview=True)   
    media = await replied.download()   
    await text.edit_text("<code>ᴜᴘʟᴏᴀᴅɪɴɢ...</code>", disable_web_page_preview=True)                                            
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        return await text.edit_text(text=f"ᴇƦƦᴏƦ :- {error}\nғᴏʀᴡʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ(/support) ᴏʀ ᴀᴅᴍɪɴ(/about", disable_web_page_preview=True)          
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return    
    await text.edit_text(
        text=f"https://telegra.ph{response[0]}",
        disable_web_page_preview=True,
    )

