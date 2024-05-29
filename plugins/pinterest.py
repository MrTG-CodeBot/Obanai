import asyncio
import os
import wget
from pyrogram import Client, filters
from bs4 import BeautifulSoup
import requests
import re

def extract_image_url(pinterest_url):
    try:
        response = requests.get(pinterest_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        image_tags = soup.find_all('img', class_=['h-image-fit', 'h-unsplash-img'])
        if not image_tags:
            image_tags = soup.find_all('img', attrs={'src': lambda src: src and src.startswith('https://i.pinimg.com/')})
        if image_tags:
            return image_tags[0]['src']
    except requests.exceptions.RequestException as e:
        message.reply_text(f"Error fetching content from URL: {e}")
        print(f"Error fetching content from URL: {e}")
    except Exception as e:
        message.reply_text(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
    return None

pinterest_link_regex = r"https://pin\.it/(?P<code>\w+)"

@Client.on_message(filters.regex(pinterest_link_regex))
async def main(client, message):
  try:
    sd=await message.reply_text("<code>Downloading...</code>")
    pinterest_url = message.text
    image_url = extract_image_url(pinterest_url)

    if image_url:
        ls = image_url.split("x/")
        first_part = ls[0]
        f_s = first_part.split(".com/")
        second_part = ls[1]
        n = "https://i.pinimg.com/"
        index = "1200"
        m = n + index + "x/" + second_part
        print(f"m= {m}")
        b = wget.download(m)
        await client.send_document(message.chat.id , b)
        await sd.delete()
    else:
        await message.reply_text("Image URL not found. Consider respecting Pinterest's terms of service.")

  except Exception as e:
        await message.reply_text(f"Unexcepted error: {e}\n\nForward this error message to my admin or in support group")
