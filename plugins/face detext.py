import requests
from pyrogram import Client as app, filters
import os
USER_ID = '60b0cd03d11c8a6eaab02561'
@app.on_message(filters.me & filters.command(['detect'], ['/','!','+','-','']))
async def face_detector1(client, message):
    rp = message.reply_to_message
    if rp.photo or rp.sticker or rp.document:
        FILE_NAME = f'{rp.message_id}.png'
        await client.edit_message_text(message.chat.id, 'downloading ...')
        await rp.download(FILE_NAME)
        IMAGE_PATH = f'downloads/{FILE_NAME}'
        API_URL = 'http://facexapi.com/get_image_attr'
        files = {'image_attr' : open(IMAGE_PATH, 'rb')}
        headers = {'user_id': USER_ID}
        await client.edit_message_text(message.chat.id, 'posting ...')
        r = requests.post(API_URL, headers=headers, files=files)
        print(r.text)
        await client.send_message(message.chat.id, r.text , reply_to_message_id = message.message_id)
