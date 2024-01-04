class script(object):  
    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

◉ ɢʀᴏᴜᴩ: {}(<code>{}</code>)
◉ ᴍᴇᴍʙᴇʀꜱ: {}
◉ ᴀᴅᴅᴇᴅ ʙʏ: {}"""
    
    LOG_TEXT_P = """#ɴᴇᴡ_ᴜꜱᴇʀ
    
◉ ᴜꜱᴇʀ-ɪᴅ: <code>{}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {}"""

    LOG_TEXT_FP = """#ɴᴇᴡ_ғᴇᴇᴅʙᴀᴄᴋ_ᴘᴜʙʟɪᴄ
ғᴇᴇᴅʙᴀᴄᴋ ғʀᴏᴍ {}
ᴛʜᴇ ᴛᴇxᴛ ɪs : <code>{}</code>"""

    LOG_TEXT_FA = """#ɴᴇᴡ_ғᴇᴇᴅʙᴀᴄᴋ_ᴀɴᴏɴʏᴍᴏᴜsʟʏ 
ғᴇᴇᴅʙᴀᴄᴋ ғʀᴏᴍ {}
ᴛʜᴇ ᴛᴇxᴛ ɪs : <code>{}</code>"""

    START_TXT = """Hᴇʟʟᴏ {}.
Mʏ Nᴀᴍᴇ Is <a href=https://t.me/{}>{}</a>. ɪ ᴀᴍ ᴀ sᴘᴇᴄɪᴀʟ ʙᴏᴛ"""

    HELP_TXT = """Hᴇʀᴇ ɪs Mʏ Hᴇʟᴩ.
ᴄʟɪᴄᴋ ᴛʜɪs /support"""

    ABOUT_TXT = """<b>✯ Mʏ ɴᴀᴍᴇ ɪs {} </>
✯ Dᴇᴠᴇʟᴏᴩᴇʀ: <a href='https://t.me/MrTG_Coder'>ᴍʀ.ʙᴏᴛ ᴛɢ</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ Mʏ Sᴇʀᴠᴇʀ: <a href='https://www.render.com'>ʀᴇɴᴅᴇʀ </a>
✯ Pʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ: ᴠ2.0.30
✯ Mʏ ᴠᴇʀsɪᴏɴ: ᴠ1.8"""

    WELCME_TXT ="""ʜᴇʏ {} ✨,\n🗓️ᴊᴏɪɴ ᴅᴀᴛᴇ :- {}\n🕛ᴊᴏɪɴ ᴛɪᴍᴇ :- {}\n\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}🍃\n"""

    RRB_TXT = """ɪғ ᴀɴʏ ʙᴜɢs ɪɴ ᴛʜɪs ʙᴏᴛ ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛᴏ sᴜᴘᴘᴏʀᴛ ᴀᴅᴍɪɴ. ᴛʜɪs ʙᴏᴛ ɪs ᴀ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ
ᴄʀᴇᴅɪᴛs @MrTG_Coder"""

    SUPPORT_TXT = """ᴛʜᴇsᴇ ᴀʀᴇ ᴍʏ sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢʀᴏᴜᴘ. ɪғ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ʀᴇᴘᴏʀᴛ ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴ
ᴄʀᴇᴅɪᴛs @MrTG_Coder"""

    STATUS_TXT =  """<b>◉ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code></b>
◉ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>"""

    ADMIN_CMD_TXT = """/broadcast ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs\n/group_broadcast ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssɢᴇ ᴛᴏ ᴀʟʟ ʙᴏᴛ ᴀᴅᴍɪɴ ɢʀᴏᴜᴘs/leave ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀ ɢʀᴏᴜᴘ\n/ban ᴛᴏ ʙᴀɴ ᴀ ᴜsᴇʀ\n/unban ᴛᴏ ᴜɴʙᴀɴ ᴛʜᴇ ʙᴀɴɴᴇᴅ ᴜsᴇʀ\n/users ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟɪsᴛ ᴏғ ᴜsᴇʀs\n.ping ғᴏʀ ᴛʜᴇ ᴘᴏɴɢ\n"""

    TELEGRAGH_TXT = """/telegraph Rᴇᴘʟʏ Tᴏ A Pʜᴏᴛᴏ Oʀ Vɪᴅᴇᴏ"""

    OPENAI_TXT = """/openai {ᴜʀ ǫᴜᴇsᴛɪᴏɴ}\n sᴏᴍᴇᴛɪᴍᴇs ɪᴛ ᴡɪʟʟ ɴᴏᴛ ᴡᴏʀᴋ ᴘʀᴏᴘᴇʀʟʏ"""

    SONG_TXT = """/song {song_name} .ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ
ᴄʀᴇᴅɪᴛs @MrTG_Coder"""

    RINGTUNE_TXT = """ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ʀɪɴɢᴛᴜɴᴇ ɪɴ ᴛʜᴇ ғʀᴏᴍ ᴏғ /ringtune {sᴏɴɢ_ɴᴀᴍᴇ + ᴀʀᴛɪsᴛ_ɴᴀᴍᴇ} ᴏʀ {sᴏɴɢ_ɴᴀᴍᴇ}\n <a href='https://t.me/amal_nath_05/197'>ʀᴇᴀsᴏɴ</a>
ᴄʀᴇᴅɪᴛs @MrTG_Coder"""

    STICKER_TXT = """reply to the sticker as /sticker_id"""

    INSTA_TXT = """sᴇɴᴅ ɪɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟ,sᴛᴏʀɪᴇs ᴀɴᴅ ᴘᴏsᴛ ʟɪɴᴋ ᴛᴏ ᴛʜɪs ʙᴏᴛ, ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ, ᴘᴜʙʟɪᴄ ᴏɴʟʏ"""

    REPO_TXT = """/repo ᴛᴏ sᴇᴀʀᴄʜ ᴛʜᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ 
ᴄʀᴇᴅɪᴛs @MrTG_Coder"""

    SPOTIFY_TXT = """/spotify {song_name}\nɴᴏᴡ ᴡᴇ ᴏɴʟʏ ᴀᴅᴅ ғɪɴᴅ ᴛʜᴇ sᴏɴɢ ᴅᴇᴛᴀɪʟs ʙʏ ᴜʀ ʀᴇǫᴜᴇsᴛ.
ᴄʀᴇᴅɪᴛs @MrTG_Coder"""

    REPORT_MSG = """ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs"""

    REPORT_TXT = """@admins, @admins, /report. ғᴏʀ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs(ᴡᴏʀᴋ ᴏɴʟʏ ɪɴ  ɢʀᴏᴜᴘ)"""

    GET_REPO_TXT = """ʜᴇʏ {}, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ ʀᴇᴘᴏ ᴀɴᴅ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʀᴇᴘᴏ"""

    FEEDBACK_TXT = """/fp - ᴛᴏ sᴇɴᴅ ʏᴏᴜʀ ғᴇᴇᴅʙᴀᴄᴋ ʙʏ ᴘᴜʙʟɪᴠᴀʟʟʏ
/fa - ᴛᴏ sᴇɴᴅ ʏᴏᴜʀ ғᴇᴇᴅʙᴀᴄᴋ ʙʏ ᴀɴᴏɴʏᴍᴏᴜsʟʏ
ᴄʀᴇᴅɪᴛs @MrTG_Coder"""

    FONT_TXT = """ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴜɴᴄᴛɪᴏɴ

/font {your_text}

ᴇɢ:- <code>/font sd bots </code>
ᴄʀᴇᴅɪᴛs @MrTG_Coder"""
