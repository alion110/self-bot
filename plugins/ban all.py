from pyrogram import Client as app , filters
from pyrogram.errors import FloodWait
import asyncio
@app.on_message(filters.me & filters.command(['clm'], ['/','!','+','-','']))
def clmembers(client, message):
    try:
        limit = message.text.split(' ')[1] if int(message.text.split(' ')[1]) else None
        list = []
        client.send_message(message.chat.id, 'loading members ...')
        for member in client.get_chat_members(message.chat.id):            
            print(member)
            list.append(member.user.id)
            print(list)
        for id in list:
            app.kick_chat_member(message.chat.id, id)
        client.send_message(message.chat.id, 'انجام شد')
    except FloodWait as r:
        asyncio.sleep(r.x)
