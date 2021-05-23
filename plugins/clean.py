from pyrogram import Client as app, filters

@app.on_message(filters.me & filters.command(['clean'],['/','!','+','-','','*','~','#','$']))
async def clean_messages(client, message):
    try:
        limit = int(message.text.split(' ')[1]) if message.text.split(' ')[1] else 500
        f = await client.get_history(message.chat.id, limit=limit)
        await client.edit_message_text(message.chat.id, message.message_id, '**در حال پاکسازی ...**')
        for message in f:
            await client.delete_messages(message.chat.id, message.message_id)
        await client.edit_message_text(message.chat.id, message.message_id, '**پاکسازی انجام شد!**')
        await client.delete_messages(message.chat.id, message.message_id)
    except:
        pass