from pyrogram import Client as app
from pyrogram import filters
import asyncio
@app.on_message(filters.me & filters.command(['kir'], ['/','!','+','-','']))
async def kirekhar(client, message):
    if message.reply_to_message:
        rp = message.reply_to_message.message
    elif not message.reply_to_message:
        rp = None
    await client.delete_messages(message.chat.id, message.message_id)
    await asyncio.gather(*[client.send_message(message.chat.id, message.text.split('kir')[1].split('=')[0] for i in range(int(message.text.split('=')[1])), reply_to_message_id=rp])



