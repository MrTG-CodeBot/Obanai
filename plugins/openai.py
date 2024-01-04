from pyrogram import Client, filters
from pyrogram.types import Message
import openai
from info import OPENAI_API_KEY, REQUESTED_CHANNEL

openai.api_key = OPENAI_API_KEY

@Client.on_message(filters.command('openai'))
async def openai_command(client, message):
    if not message.text:
        await client.send_message(message.chat.id, "ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴜʀ ʀᴇǫᴜᴇsᴛ ")
        return

    try:
        user_input = message.text.split(' ', 1)[1]

        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = user_input,
            temperature = 0.5,
            max_tokens = 1000,
            top_p=1,
            frequency_penalty=0.1,
            presence_penalty = 0.0,
        )
        ai = response.choices[0].text
        await message.reply_text(ai)
        await client.send_message(REQUESTED_CHANNEL, text=f"ᴏᴘᴇɴᴀɪ ʀᴇǫᴜᴇsᴛ ғʀᴏᴍ {message.from_user.mention}\nǫᴜᴇʀʏ ɪs:- {user_input}")

    except Exception as e:
        error_message = f"sᴏʀʀʏ, ᴀɴ ᴇʀʀᴏʀ  ᴏᴄᴄᴜʀᴇᴅ: {str(e)}"
        await message.reply_text(error_message)
