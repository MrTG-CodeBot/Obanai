from pyrogram import Client, filters
from PIL import Image
import qrcode


@Client.on_message(filters.command("qr"))
async def generate_qr_code(client, message):
    text = message.text.split(maxsplit=1)[1]
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
  
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
  
    img_path = "qr_code.png"
    img.save(img_path)
  
    await message.reply_photo(img_path)
