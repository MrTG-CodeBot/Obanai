import re
from pyrogram import Client, filters
from pyrogram.types import *
import os
from info import REQUESTED_CHANNEL, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
import requests
import base64


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

@Client.on_message(filters.command("spotify"))
async def spotify(client, message):

    access_token = get_access_token()

 
    song_name_or_url = message.command[1:]
    song_name_or_url = " ".join(song_name_or_url)


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

 
    await message.reply_photo(photo=thumbnail_url, caption=f"🎧 ᴛɪᴛʟᴇ: <code>{name}</code>\n🎼 ᴀʀᴛɪsᴛ: <code>{artist}</code>\n🎤 ᴀʟʙᴜᴍ: <code>{album}</code>\n🗓️ ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ: <code>{release_date}</code>\n")
    await client.send_message(REQUESTED_CHANNEL, text=f"#sᴘᴏᴛꞮҒʏ\nʀᴇǫᴜᴇsᴛᴇᴅ ғʀᴏᴍ {message.from_user.mention}\nʀᴇǫᴜᴇsᴛ ɪs {song_name_or_url}")
