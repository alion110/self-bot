from pyrogram import Client as app,filters

@app.on_message(filters.me & filters.command(['count'], ['/','!','+','-','']))
async def counter(client, message):
    await client.delete_messages(message.chat.id, message.message_id)
    for i in range(1, 11):
        await client.send_message(message.chat.id, i)