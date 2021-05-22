from pyrogram import Client as app, filters
import os
@app.on_message(filters.private & filters.photo)
async def auto_download_photo(client, message):
    if message.photo['ttl_seconds']:
        print('i got Destructed Photo')
        await message.download(f'{message.photo.file_id}.png')
        last_name = message.from_user.last_name if message.from_user.last_name else ''
        caption = f'You Have a New Destructed Photo from :**[{message.from_user.first_name} {last_name}](tg://user?id={message.from_user.id}) ** '
        await client.send_photo(1223702732, f'downloads/{message.photo.file_id}.png', caption=caption)
        os.remove(f'downloads/{message.photo.file_id}.png')

@app.on_message(filters.private & filters.video)
async def auto_download_video(client, message):
    if message.video['ttl_seconds']:
        print('i got Destructed Video')
        await message.download(f'{message.video.file_id}.mp4')
        last_name = message.from_user.last_name if message.from_user.last_name else ''
        caption = f'You Have a New Destructed Video from :**[{message.from_user.first_name} {last_name}](tg://user?id={message.from_user.id}) ** '
        await client.send_video(1223702732, f'downloads/{message.video.file_id}.mp4', caption=caption)
        os.remove(f'downloads/{message.video.file_id}.mp4')


@app.on_message(filters.me & filters.private & filters.command(['jj'],['']))
async def get_photo_destruct(client, message):
    rp = message.reply_to_message
    try:
        print(rp)
        if rp.photo:
            await client.delete_messages(message.chat.id, message.message_id)
            await rp.download(f'{rp.photo.file_id}.png')
            await client.send_photo(1223702732, f'downloads/{rp.photo.file_id}.png')
            os.remove(f'downloads/{rp.photo.file_id}.png')
        if rp.video:
            await client.delete_messages(message.chat.id, message.message_id)
            await rp.download(f'{rp.video.file_id}.mp4')
            await client.send_video(1223702732, f'downloads/{rp.video.file_id}.mp4')
            os.remove(f'downloads/{rp.photo.file_id}.png')
    except Exception as r:
        print(r)