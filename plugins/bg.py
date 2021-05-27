from pyrogram import Client as app, filters
import requests, os

@app.on_message(filters.me & filters.reply & filters.command(['rbg'],['/','!','+','-','','*','~','#','$','']))
async def remove_bg(client, message):
    if 1 == 1:
        rp = message.reply_to_message
        if rp.photo or rp.sticker:
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await rp.download('bg.jpg')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Processing ...**')
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': open('downloads/bg.jpg', 'rb')},
                data={'size': 'auto'},
                headers={'X-Api-Key': 'nRG1x3QJwR3ghABkeJWiyiia'},
            )
            if response.status_code == requests.codes.ok:
                with open('no-bg.png', 'wb') as out:
                    out.write(response.content)
                await client.edit_message_text(message.chat.id, message.message_id, '**Uploading .**')
                await client.edit_message_text(message.chat.id, message.message_id, '**Uploading ..**')
                await client.edit_message_text(message.chat.id, message.message_id, '**Uploading ...**')
                await client.send_photo(message.chat.id, 'no-bg.png', caption='Background Successfully Removed :)', reply_to_message_id=rp.message_id)
                await client.send_document(message.chat.id, 'no-bg.png', caption='Background Successfully Removed :)', reply_to_message_id=rp.message_id)
                await client.delete_messages(message.chat.id, message.message_id)
                os.remove('downloads/bg.jpg')
                os.remove('no-pg.png')
            else:
                print("Error:", response.status_code, response.text)
