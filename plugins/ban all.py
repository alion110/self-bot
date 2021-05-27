from pyrogram import Client as app , filters
from pyrogram.errors import FloodWait
import asyncio
@app.on_message(filters.me & filters.command(['clm'], ['/','!','+','-','']))
def clmembers(client, message):
    try:
        limit = message.text.split(' ')[1] if int(message.text.split(' ')[1]) else 500
        client.send_message(message.chat.id, 'loading members ...')
        for member in client.iter_chat_members(message.chat.id, limit=int(limit)):
            print(member)
            client.kick_chat_member(message.chat.id, member.user.id)
        client.send_message(message.chat.id, 'انجام شد')
    except FloodWait as r:
        asyncio.sleep(r.x)
