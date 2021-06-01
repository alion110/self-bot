from pyrogram import Client as app
from pyrogram import filters
import asyncio


@app.on_message(filters.me & filters.command(['kir'], ['/', '!', '+', '-', '']))
async def kirekhar(client, message):
    await client.delete_messages(message.chat.id, message.message_id)
    text = message.text.split('kir')[1].split('=')[0]
    tedad = int(message.text.split('=')[1])
    if message.reply_to_message:
        rp = message.reply_to_message.message
        #await asyncio.gether(*[client.send_message(message.chat.id, text for i in range(tedad), reply_to_message_id=rp)])
    elif not message.reply_to_message:
        await asyncio.gether(*[client.send_message(message.chat.id, text for i in range(tedad))])


