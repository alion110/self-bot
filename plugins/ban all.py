from pyrogram import Client as app , filters
from pyrogram.errors import FloodWait
import asyncio
@app.on_message(filters.me & filters.command(['clm'], ['/','!','+','-','']))
def clmembers(client, message):
    try:
        limit = message.text.split(' ')[1] if int(message.text.split(' ')[1]) else 500
        await client.send_message(message.chat.id, 'loading members ...')
        for member in await client.iter_chat_members(message.chat.id, limit=int(limit)):
            await client.kick_chat_member(message.chat.id, member.user.id)
        await client.send_message(message.chat.id, 'انجام شد')
    except FloodWait as r:
        asyncio.sleep(r.x)
