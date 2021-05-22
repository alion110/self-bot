from PIL import Image
from pyrogram import Client as app, filters
from PIL import ImageFilter
import os
@app.on_message(filters.me & filters.command(['blur'],['/','!','+','-','']))
async def image(client, message):
    try:
        m1 = await client.get_me()
        print(m1)
        rp = message.reply_to_message
        if rp.photo or rp.sticker:
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await message.reply_to_message.download('file.png')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing ...**')
            img = Image.open('downloads/file.png')
            print('oppnd')
            blur = img.filter(ImageFilter.BLUR)
            print('blured')
            blur.save('file1.png')
            await client.send_photo(message.chat.id ,'file1.png', reply_to_message_id = rp.message_id)
            os.remove('file1.png')
            os.remove('downloads/file.png')
    except Exception as r:
        print(r)

@app.on_message(filters.me & filters.command(['gray'],['/','!','+','-','']))
async def imagegray(client, message):
    try:
        rp = message.reply_to_message
        if rp.photo or rp.sticker:
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await message.reply_to_message.download('file.png')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing ...**')
            img = Image.open('downloads/file.png')
            print('oppnd')
            blur = img.convert('L')
            print('grayed')
            blur.save('file1.png')
            await client.send_photo(message.chat.id ,'file1.png', reply_to_message_id=rp.message_id)
            os.remove('file1.png')
            os.remove('downloads/file.png')
    except Exception as r:
        print(r)

@app.on_message(filters.me & filters.command(['resize'],['/','!','+','-','']))
async def image_resize(client, message):
    try:
        rp = message.reply_to_message
        if rp.photo or rp.sticker or rp.document:
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await message.reply_to_message.download('file.png')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing ...**')
            img = Image.open('downloads/file.png')
            print('oppnd')
            img = img.resize((512,512))
            print('resized')
            img.save('file1.png')
            await client.send_document(message.chat.id,'file1.png',file_name=str(message.message_id),caption='@LilPG' ,reply_to_message_id=rp.message_id)
            await client.delete_messages(message.chat.id, )
            os.remove('file1.png')
            os.remove('downloads/file.png')

    except Exception as r:
        print(r)

@app.on_message(filters.me & filters.command(['rotate'],['/','!','+','-','']))
async def rotate(client, message):
    try:
        rp = message.reply_to_message
        if rp.photo:
            rot = int(message.text.split(' ')[1])
            await client.edit_message_text(message.chat.id, message.message_id,'**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await message.reply_to_message.download('file.png')
            img = Image.open('downloads/file.png')
            print('oppnd')
            out = img.rotate(int(rot))
            print('rotatad')
            out.save(f'{message.message_id}.png')
            await client.send_photo(message.chat.id, f'{message.message_id}.png', reply_to_message_id=message.message_id)
            os.remove(f'{message.message_id}.png')
            os.remove('downloads/file.png')
    except Exception as r:
        print(r)