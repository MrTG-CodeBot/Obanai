import asyncio
import os
import re
from pyrogram import Client, filters
from pytube import YouTube
from info import REQUESTED_CHANNEL
from youtube_search import YoutubeSearch

@Client.on_message(filters.command(["song"]))
async def download_song(client, message):
  # Check if the user has provided a song name
  if len(message.text.split()) < 2:
    await message.reply("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ sᴏɴɢ ʏᴏᴜ ᴡᴀɴᴛ ᴇɢ:- /song lover")
    return

  song_name = " ".join(message.text.split()[1:]) # Extract and combine song name parts

  # Send "Searching..." message before searching
  await message.reply("⏳")

  # Search for the song on YouTube
  search_results = YoutubeSearch(song_name, max_results=1).to_dict()
  if not search_results:
    await message.reply("ɴᴏ sᴏɴɢ ғᴏᴜɴᴅ ᴡɪᴛʜ ᴛʜᴀᴛ ɴᴀᴍᴇ ᴡɪᴛʜ ᴛʜᴀᴛ")

  song_url = search_results[0]["url_suffix"]
  song_title = search_results[0]["title"]
  duration = search_results[0]["duration"]

  # Download the song using pytube
  yt = YouTube(f"https://www.youtube.com{song_url}")
  thumbnail_url = yt.thumbnail_url # Extract thumbnail URL

  audio_streams = yt.streams.filter(only_audio=True)
  if not audio_streams:
    await message.reply("ɴᴏ ᴀᴜᴅɪᴏ sᴛᴇᴇᴀᴍ ғᴏᴜɴᴅ ғᴏʀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ᴠɪᴅᴇᴏs")
    return

  video = audio_streams.first()
  audio_filename = f"{song_title}.mp3"

  try:
    video.download(filename=audio_filename)

    # Prepare the thumbnail for use as both caption and photo
    thumbnail_caption = f"**🍃 {song_title}**\n" + \
              f"🕛 ᴅᴜʀᴛɪᴏɴ: {duration}\n" + \
              f"🍂 ʏᴏᴜ ᴛᴜʙᴇ: <a href='https://www.youtube.com{song_url}'>ʏᴏᴜ ᴛᴜʙᴇ</a>"

    # Send the thumbnail as a photo with the caption
    await message.reply_photo(
      thumbnail_url,
      caption=thumbnail_caption
    )

    song_caption = f"**🎧 {song_title}**\n"

    # Send the downloaded song without an explicit caption (it's already in the photo)
    await message.reply_audio(
      audio_filename,
      caption=song_caption
    )
    await client.send_message(REQUESTED_CHANNEL, text=f"#sᴏɴɢ\nʀᴇǫᴜᴇsᴛᴇᴅ ғʀᴏᴍ {message.from_user.mention}\nʀᴇǫᴜᴇsᴛ ɪs {song_name}")

    # Delete the downloaded song after sending it
    os.remove(audio_filename)

  except Exception as e:
    await message.reply(f"ᴇʀʀᴏʀ sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ: {e}")
