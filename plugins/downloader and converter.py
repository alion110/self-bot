from pyrogram import Client as app , filters
import os,asyncio

async def bla(sec):
    await asyncio.sleep(sec)

@app.on_message(filters.me & filters.command(['download', 'save'],['/','!','+','-','','*','~','#','$'])) #Download files from telegram and save in local directory
async def downloader(client, message):
    try:
        video = message.reply_to_message.video if message.reply_to_message.video else None
        photo = message.reply_to_message.photo if message.reply_to_message.photo else None
        music = message.reply_to_message.audio if message.reply_to_message.audio else None
        if video:
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await message.reply_to_message.download(f'{message.message_id}.mp4')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
            await bla(10)
            await client.delete_messages(message.chat.id, message.message_id)
        elif photo:
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await message.reply_to_message.download(f'{message.message_id}.png')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
            await bla(8)
            await client.delete_messages(message.chat.id, message.message_id)
        elif music:
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await message.reply_to_message.download(f'{message.message_id}.mp3')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
            await bla(8)
            await client.delete_messages(message.chat.id, message.message_id)
        else:
            whattosave = message.reply_to_message
            await whattosave.forward(me)
            await client.delete_messages(message.chat.id, message.message_id)
    except:
        pass

@app.on_message(filters.me & filters.command(['stick', 'photo', 'voice', 'audio'],['/','!','+','-','','*','~','#','$'])) #file converter :)
async def convertermessage(client, message):
    try:
        rp = message.reply_to_message
        if rp.sticker:
            print('got')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await rp.download('files1.png')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
            await client.send_photo(message.chat.id, 'downloads/files1.png', reply_to_message_id = rp.message_id)
            await client.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files1.png')
        if rp.photo or rp.document:
            print('got')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await rp.download('files2.webp')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
            print('downloaded')
            await client.send_sticker(message.chat.id, 'downloads/files2.webp', reply_to_message_id = rp.message_id)
            print('sent')
            await client.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files2.webp')
        if rp.voice:
            print('got')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await rp.download('files2.mp3')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
            print('downloaded')
            await client.send_audio(message.chat.id, 'downloads/files2.mp3', reply_to_message_id = rp.message_id)
            print('sent')
            await client.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files2.mp3')
        if rp.audio:
            print('got')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await rp.download('files2.ogg')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
            print('downloaded')
            await client.send_voice(message.chat.id, 'downloads/files2.ogg', reply_to_message_id = rp.message_id)
            print('sent')
            await client.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files2.ogg')
    except:
        pass