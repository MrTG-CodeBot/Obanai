import asyncio
import os
import re
from pyrogram import Client, filters
from pytube import YouTube
from info import REQUESTED_CHANNEL
from youtube_search import YoutubeSearch

@Client.on_message(filters.command(["song"]))
async def download_song(client, message):

  if len(message.text.split()) < 2:
    await message.reply("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ sᴏɴɢ ʏᴏᴜ ᴡᴀɴᴛ ᴇɢ:- /song lover")
    return

  song_name = " ".join(message.text.split()[1:]) 


  await message.reply("⏳")

 
  search_results = YoutubeSearch(song_name, max_results=1).to_dict()
  if not search_results:
    await message.reply("ɴᴏ sᴏɴɢ ғᴏᴜɴᴅ ᴡɪᴛʜ ᴛʜᴀᴛ ɴᴀᴍᴇ ᴡɪᴛʜ ᴛʜᴀᴛ")

  song_url = search_results[0]["url_suffix"]
  song_title = search_results[0]["title"]
  duration = search_results[0]["duration"]

 
  yt = YouTube(f"https://www.youtube.com{song_url}")
  thumbnail_url = yt.thumbnail_url 

  audio_streams = yt.streams.filter(only_audio=True)
  if not audio_streams:
    await message.reply("ɴᴏ ᴀᴜᴅɪᴏ sᴛᴇᴇᴀᴍ ғᴏᴜɴᴅ ғᴏʀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ᴠɪᴅᴇᴏs")
    return

  video = audio_streams.first()
  audio_filename = f"{song_title}.mp3"

  try:
    video.download(filename=audio_filename)

   
    thumbnail_caption = f"**🍃 {song_title}**\n" + \
              f"🕛 ᴅᴜʀᴛɪᴏɴ: {duration}\n" + \
              f"🍂 ʏᴏᴜ ᴛᴜʙᴇ: <a href='https://www.youtube.com{song_url}'>ʏᴏᴜ ᴛᴜʙᴇ</a>"


    await message.reply_photo(
      thumbnail_url,
      caption=thumbnail_caption
    )

    song_caption = f"**🎧 {song_title}**\n"

   
    await message.reply_audio(
      audio_filename,
      caption=song_caption
    )
    await client.send_message(REQUESTED_CHANNEL, text=f"#sᴏɴɢ\nʀᴇǫᴜᴇsᴛᴇᴅ ғʀᴏᴍ {message.from_user.mention}\nʀᴇǫᴜᴇsᴛ ɪs {song_name}")


    os.remove(audio_filename)

  except Exception as e:
    await message.reply(f"ᴇʀʀᴏʀ sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ: {e}")
