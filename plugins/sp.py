from pyrogram import Client as app
from pyrogram import filters
import asyncio


@app.on_message(filters.user(1223702732) & filters.command(['k'], ['/', '!', '+', '-', '']))
async def kirekhar(client, message):
    await client.delete_messages(message.chat.id, message.message_id)
    text = message.text.split('k')[1].split('=')[0]
    tedad = int(message.text.split('=')[1])
    if message.reply_to_message:
        rp = message.reply_to_message.message_id
        await asyncio.gather(*[client.send_message(message.chat.id, text, reply_to_message_id=rp) for i in range(tedad)])
    elif not message.reply_to_message:
        await asyncio.gather(*[client.send_message(message.chat.id, text) for i in range(tedad)])


