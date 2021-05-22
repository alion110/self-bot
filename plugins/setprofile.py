from pyrogram import Client as app
from pyrogram import filters
import asyncio

async def bla(sec):
    await asyncio.sleep(sec)


@app.on_message(filters.me & filters.command(['setprofile', 'setprof'],['/','!','+','-','','*','~','#','$'])) #set telegram profile
async def setprofilephoto(client, message):
    try:
        gif = message.reply_to_message.animation if message.reply_to_message.video else None
        photo = message.reply_to_message.photo if message.reply_to_message.photo else None
        if photo:
            await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس ...**')
            await message.reply_to_message.download('profile.png')
            await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس .**')
            await client.set_profile_photo(photo = 'downloads/profile.png')
            os.remove('downloads/profile.png')
            await client.edit_message_text(message.chat.id, message.message_id, '**پروفایل با موفقیت تنظیم شد 👁**')
            await bla(10)
            await app.delete_messages(message.chat.id, message.message_id)

        if gif: #it does not working right now :(
            await client.edit_message_text(message.chat.id, message.message_id, '**درحال دانلود گیف .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف ...**')
            await message.reply_to_message.download('profile.mp4')
            await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف .**')
            await client.set_profile_photo(video = 'downloads/profile.mp4')
            os.remove('downloads/profile.mp4')
            await client.edit_message_text(message.chat.id, message.message_id, '**پروفایل با موفقیت تنظیم شد 👁**')
    except:
        pass