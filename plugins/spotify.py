import re
from pyrogram import Client, filters, enums
import os
from info import REQUESTED_CHANNEL, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
import requests
import base64
from yt_dlp import YoutubeDL
import os, wget
import random
import shutil

client_id = SPOTIFY_CLIENT_ID
client_secret = SPOTIFY_CLIENT_SECRET
credentials = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')).decode('utf-8')

def get_access_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()['access_token']

async def download_songs(name, download_directory="."):
  query = f"{name} Lyrics".replace(":", "").replace("\"", "")
  ydl_opts = {
      "format": "bestaudio/best",
      "default_search": "ytsearch",
      "noplaylist": True,
      "nocheckcertificate": True,
      "outtmpl": f"{name}.mp3",
      "quiet": True,
      "addmetadata": True,
      "prefer_ffmpeg": True,
      "geo_bypass": True,
      "nocheckcertificate": True,
  }

  with YoutubeDL(ydl_opts) as ydl:
      try:
          video = ydl.extract_info(f"ytsearch:{name}", download=False)["entries"][0]["id"]
          info = ydl.extract_info(video)
          filename = ydl.prepare_filename(info)
          if not filename:
              print(f"Track Not Found⚠️")
          else:
              path_link = filename
              return path_link, info 
      except Exception as e:
          raise Exception(f"Error downloading song: {e}") 

@Client.on_message(filters.regex(r'https://open\.spotify\.com/track/([a-zA-Z0-9]+)'))
async def spotify(client, message):
 try:

    access_token = get_access_token()

    song_name_or_url = message.text
    match = re.match(r'https://open\.spotify\.com/track/([a-zA-Z0-9]+)', song_name_or_url)
    if match:

        song_id = match.group(1)
    else:

        song_name = song_name_or_url
        url = f'https://api.spotify.com/v1/search?q={song_name}&type=album,track'
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        data = response.json()
        item = data["tracks"]["items"][0]
        song_id = item["id"]

    url = f'https://api.spotify.com/v1/tracks/{song_id}'
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    thumbnail_url = data["album"]["images"][0]["url"]

    artist = data["artists"][0]["name"]
    name = data["name"]
    album = data["album"]["name"]
    release_date = data["album"]["release_date"]

    randomdir = f"/tmp/{str(random.randint(1, 100000000))}"
    os.mkdir(randomdir)
    path, info = await download_songs(name, randomdir)
    thumbnail = wget.download(thumbnail_url)
 
    await message.reply_photo(photo=thumbnail_url, caption=f"🎧 ᴛɪᴛʟᴇ: <code>{name}</code>\n🎼 ᴀʀᴛɪsᴛ: <code>{artist}</code>\n🎤 ᴀʟʙᴜᴍ: <code>{album}</code>\n🗓️ ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ: <code>{release_date}</code>\n")
    await client.send_message(REQUESTED_CHANNEL, text=f"#sᴘᴏᴛꞮҒʏ\nʀᴇǫᴜᴇsᴛᴇᴅ ғʀᴏᴍ {message.from_user.mention}\nʀᴇǫᴜᴇsᴛ ɪs {song_name_or_url}")
    await message.reply_audio(
        path,
        thumb=thumbnail
    )    
    shutil.rmtree(randomdir)
    os.remove(thumbnail)
 except Exception as e:
    await message.reply_text(f"{e}")
