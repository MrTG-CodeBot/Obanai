from pyrogram import Client, filters
import requests

@Client.on_message(filters.command("repo"))
async def repo(client, message):
    if len(message.command) > 1:
        query = ' '.join(message.command[1:])
        response = requests.get(f"https://api.github.com/search/repositories?q={query}")
        if response.status_code == 200:
            data = response.json()
            if data['total_count'] > 0:
                repo = data['items'][0]  # Get the first result
                reply = f"**{repo['name']}**\n\n" \
                        f"**🔖 ᴅᴇsᴄʀɪᴘᴛɪᴏɴ:** <code>{repo['description']}</code>\n" \
                        f"**🔗 ᴜʀʟ:** {repo['html_url']}\n" \
                        f"**✨ sᴛᴀʀs:** <code>{repo['stargazers_count']}</code>\n" \
                        f"**📡 ғᴏʀᴋs:** <code>{repo['forks_count']}</code>"

                # Await the coroutine here
                await message.reply_text(reply)
            else:
                await message.reply_text("ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ.")
        else:
            await message.reply_text("ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ.")
    else:
        await message.reply_text("ᴜsᴀɢᴇ: /repo {repo_name}")
