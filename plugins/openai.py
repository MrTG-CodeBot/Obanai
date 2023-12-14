from pyrogram import Client, filters
from pyrogram.types import Message
import openai
from info import API_ID, API_HASH, BOT_TOKEN, OPENAI_API_KEY, PORT

openai.api_key = OPENAI_API_KEY

@Client.on_message(filters.command('openai'))
async def openai_command(client, message):
    if not message.text:
        await client.send_message(message.chat.id, "Please provide ur request")
        return

    try:
        user_input = message.text.split(' ', 1)[1]

        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=1024
        )

        await message.reply_text(response.choices[0].text)

    except Exception as e:
        error_message = f"Sorry, an error occurred: {str(e)}"
        await message.reply_text(error_message)
