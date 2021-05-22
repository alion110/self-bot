from pyrogram import Client as app,filters
import asyncio
import time
last = time.time()
@app.on_message(filters.me & filters.command(['fid'],['']))
async def fid(client, message):
    rp = message.reply_to_message
    print(rp)
    await client.send_animation(message.chat.id, animation='AgADLgYAAoaouVM')
    if rp.animation:
        await client.send_message(message.chat.id, f'file id = ```{rp.animation.file_id}```')
    if rp.sticker:
        await client.send_message(message.chat.id, f'file id = ```{rp.sticker.file_id}```')

@app.on_message(filters.me & filters.command(['msg'],['/','!','+','-','','*','~','#','$','']))
async def fid(client, message):
    rp = message.reply_to_message
    print(rp)
    await client.send_message(message.chat.id, rp, reply_to_message_id=rp.message_id)





