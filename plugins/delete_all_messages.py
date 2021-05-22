from pyrogram import Client as app
from pyrogram import filters
@app.on_message(filters.me & filters.command(['dell'], ['/','!','+','-','','*','~','#','$']))
async def delllll(client, message):
    if message.reply_to_message:
        await client.edit_message_text(message.chat.id, message.message_id, '**deleting ...**')
        await client.delete_user_history(message.chat.id, message.reply_to_message.from_user.id)
        await client.send_message(message.chat.id, '**done**')


@app.on_message(filters.me & filters.command(['del'],['/','!','+','-','','*','~','#','$']))
async def delll(client, message):
    try:
        limit = int(message.text.split(' ')[1]) if message.text.split(' ')[1] else 100
        f = await client.get_history(message.chat.id, limit=limit)
        await client.edit_message_text(message.chat.id,message.message_id, '**در حال پاکسازی ...**')
        for message in f:
            if message.from_user.id == 1223702732:
                await client.delete_messages(message.chat.id, message.message_id)
        await client.edit_message_text(message.chat.id, message.message_id, '**پاکسازی انجام شد!**')
        await client.delete_messages(message.chat.id, message.message_id)
    except Exception as r:
        print(r)
