from pyrogram import Client, filters
import requests

api_url = "https://superla-da3619feeafc.herokuapp.com/llama"


@Client.on_message(filters.command("llama"))
async def llama(client, message):
  try:
    mes = " ".join(message.command[1:])
    response = requests.get(f"{api_url}?query={mes}").json()
    await message.reply_text(response['answer'])
  except Exception as e:
    await message.reply_text(e)
