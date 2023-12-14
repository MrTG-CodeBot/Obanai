from info import API_ID, API_HASH, BOT_TOKEN, PORT
from pyrogram import Client
app = Client(
    'my_bot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "plugins"},
)

if __name__ == "__main__":
   app.run()
