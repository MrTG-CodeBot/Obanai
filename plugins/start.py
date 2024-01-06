import os
from pyrogram.errors import ChatAdminRequired, FloodWait
import random
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import enums, filters, Client
from info import API_ID, API_HASH, BOT_TOKEN, PORT, ADMINS, LOG_CHANNEL, DATABASE_NAME, DATABASE_URI, S_GROUP, S_CHANNEL
from Script import script
from utils import temp
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from database.users_db import db
import re
import json
import base64
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

@Client.on_message(filters.command("support"))
async def support_command(client, message):
    buttons = [
        [
            InlineKeyboardButton("📢 Support Group", url=S_GROUP),
            InlineKeyboardButton("📢 Support Channel", url=S_CHANNEL)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=script.SUPPORT_TXT, reply_markup=reply_markup)

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        buttons = [[
            InlineKeyboardButton("ʜᴇʟᴘ", url=f"https://t.me/{temp.U_NAME}?start=help"),
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(text=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
        await asyncio.sleep(2)
        if not await db.get_chat(message.chat.id):
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return await message.reply(script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton("🍂 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ ", url=f"http://t.me/{temp.U_NAME}?startgroup=true")
            ],[
            InlineKeyboardButton("️🍃 Hᴇʟᴩ", callback_data="help"),
            InlineKeyboardButton("🍁 Aʙᴏᴜᴛ", callback_data="about")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(text=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
    
@Client.on_message(filters.command("help"))
async def help_command(client, message):
    buttons = [[
         InlineKeyboardButton('ᴀᴅᴍɪɴ', callback_data='admin')
         ],[
         InlineKeyboardButton('ᴛᴇʟᴇɢʀᴘʜ', callback_data='telegraph'),
         InlineKeyboardButton('ᴏᴘᴇɴᴀɪ', callback_data='openai'),
         InlineKeyboardButton('ʀᴇᴘᴏ sᴇᴀʀᴄʜ', callback_data='repos')
         ],[
         InlineKeyboardButton('sᴏɴɢ', callback_data='song'),
         InlineKeyboardButton('ʀɪɢᴛᴜɴᴇ', callback_data='ringtune'),
         InlineKeyboardButton('sᴘᴏᴛɪғʏ', callback_data='spotify')
         ],[
         InlineKeyboardButton('sᴛɪᴄᴋᴇʀ', callback_data='sticker'),
         InlineKeyboardButton('ɪɴsᴛᴀ', callback_data='insta'),
         InlineKeyboardButton('stats', callback_data='stats')
         ],[
         InlineKeyboardButton('ʀᴇᴘoʀᴛ', callback_data='rport'),
         InlineKeyboardButton('ғᴇᴇᴅʙᴀᴄᴋ', callback_data='feedback'),
         InlineKeyboardButton('ғᴏɴᴛ', callback_data='font')
         ],[
         InlineKeyboardButton('ᴅᴏɴᴀᴛᴇ', callback_data='donate'),
         InlineKeyboardButton('ᴀᴜᴛᴏ ʀᴇǫᴜᴇsᴛ ᴀᴄᴄᴇᴘᴛ', callback_data='auto_accept')
         ],[
         InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
         InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=script.HELP_TXT, reply_markup=reply_markup)

@Client.on_callback_query()
async def callback_handle(client, query):
    if query.data == 'start':
        buttons = [[
            InlineKeyboardButton("🍂 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ ", url=f"http://t.me/{temp.U_NAME}?startgroup=true")
            ],[
            InlineKeyboardButton("️🍃 Hᴇʟᴩ", callback_data="help"),
            InlineKeyboardButton("🍁 Aʙᴏᴜᴛ", callback_data="about"),
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'help':
        buttons = [[
         InlineKeyboardButton('ᴀᴅᴍɪɴ', callback_data='admin')
         ],[
         InlineKeyboardButton('ᴛᴇʟᴇɢʀᴀᴘʜ', callback_data='telegraph'),
         InlineKeyboardButton('ᴏᴘᴇɴᴀɪ', callback_data='openai'),
         InlineKeyboardButton('ʀᴇᴘᴏ sᴇᴀʀᴄʜ', callback_data='repos')
         ],[
         InlineKeyboardButton('sᴏɴɢ', callback_data='song'),
         InlineKeyboardButton('ʀɪɴɢᴛᴜɴᴇ', callback_data='ringtune'),
         InlineKeyboardButton('sᴘᴏᴛɪғʏ', callback_data='spotify')
         ],[
         InlineKeyboardButton('sᴛɪᴄᴋᴇʀ', callback_data='sticker'),
         InlineKeyboardButton('ɪɴsᴛᴀ', callback_data='insta'),
         InlineKeyboardButton('stats', callback_data='stats')
         ],[
         InlineKeyboardButton('ʀᴇᴘoʀᴛ', callback_data='rport'),
         InlineKeyboardButton('ғᴇᴇᴅʙᴀᴄᴋ', callback_data='feedback'),
         InlineKeyboardButton('ғᴏɴᴛ', callback_data='font')
         ],[
         InlineKeyboardButton('ᴅᴏɴᴀᴛᴇ', callback_data='donate'),
         InlineKeyboardButton('ᴀᴜᴛᴏ ʀᴇǫᴜᴇsᴛ ᴀᴄᴄᴇᴘᴛ', callback_data='auto_accept')
         ],[
         InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
         InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.HELP_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'admin':
        buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.ADMIN_CMD_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'telegraph':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.TELEGRAGH_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'openai':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.OPENAI_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'song':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.SONG_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'ringtune':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.RINGTUNE_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'spotify':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.SPOTIFY_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)    

    elif query.data == 'sticker':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.STICKER_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'insta':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.INSTA_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'repos':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.REPO_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'stats':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        await query.message.edit_text(text=script.STATUS_TXT.format(users, chats),reply_markup=reply_markup,parse_mode=enums.ParseMode.HTML)

    elif query.data == 'rport':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.REPORT_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'feedback':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.FEEDBACK_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'font':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.FONT_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'donate':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.DONATE_TXT.format(query.from_user.mention), reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'auto_accept':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.REQUEST_ACCEPT_TXT.format(query.from_user.mention), reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
    
    elif query.data == 'about':
        buttons = buttons = [[
            InlineKeyboardButton("🌿 Repo & ʀᴇᴘᴏʀᴛ ʙᴜɢs", callback_data="rrb")
            ],[
            InlineKeyboardButton('Home', callback_data='start'),
            InlineKeyboardButton('close', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.ABOUT_TXT.format(temp.B_NAME), reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
        
    elif query.data == 'rrb':
        buttons = [[
            InlineKeyboardButton("🌿 Repo", url="https://github.com/MrTG-CodeBot/Obanai"),
            InlineKeyboardButton("🐞 ʀᴇᴘᴏʀᴛ ʙᴜɢs", url=S_GROUP)
            ],[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(text=script.RRB_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
        
    elif query.data == 'close':
        await query.message.delete()
        edited_keyboard = InlineKeyboardMarkup([])
        await query.answer()
        await query.message.edit_reply_markup(edited_keyboard)
