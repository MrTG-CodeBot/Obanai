from pyrogram import Client, filters
import requests
from info import REQUESTED_CHANNEL, API_KEY
import google.generativeai as genai
# how to get the api key == 

genai.configure(api_key=API_KEY)

@Client.on_message(filters.command("ask"))
async def ai_generate(client, message):
   user_input = message.text.split()[1:]

   if not user_input:
       await message.reply_text("Please provide your question after /ask")
       return

   user_input = " ".join(user_input)

   generation_config = {
       "temperature": 0.9,
       "top_p": 1,
       "top_k": 1,
       "max_output_tokens": 2048,
   }

   safety_settings = [
       {
           "category": "HARM_CATEGORY_HARASSMENT",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
       {
           "category": "HARM_CATEGORY_HATE_SPEECH",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
       {
           "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
       {
           "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
   ]

   model = genai.GenerativeModel(
       model_name="gemini-pro",
       generation_config=generation_config,
       safety_settings=safety_settings
   )

   prompt_parts = [user_input]
   response = model.generate_content(prompt_parts)
   await message.reply_text(response.text)
   await client.send_message(REQUESTED_CHANNEL, text=f"#google_ai ʀᴇǫᴜᴇsᴛ ғʀᴏᴍ {message.from_user.mention}\nǫᴜᴇʀʏ ɪs:- {user_input}")
