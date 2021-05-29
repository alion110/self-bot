from pyrogram import Client as app,filters
from config2 import sudo
@app.on_message(filters.user(sudo) & filters.command(['star'], ['/','!','+','-','']))
async def starme(client,message):
    rp = message.reply_to_message.message_id if message.reply_to_message else None
    tedad = int(message.text.split(' ')[1])
    for i in range(tedad):
        await message.reply_text('+')
    await client.send_message(message.chat.id, '**Done !**', reply_to_message_id=rp)


  
