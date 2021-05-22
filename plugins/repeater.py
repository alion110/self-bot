from pyrogram import Client as app, filters
import time,asyncio
import random
async def bla(sec):
    asyncio.sleep(sec)

last = time.time()
payam = {}
ajablistic=[]

@app.on_message(filters.text)
async def start_hooshmand(client, message):
    global payam,ajablistic,last
    try:
        if message.chat.id in payam:
            if payam.get(message.chat.id)['text'] != message.text:
                payam.pop(message.chat.id)
                return
            if message.text in ajablistic:
                return
            if message.from_user.id == payam.get(message.chat.id)['from_user']["id"]:
                return
            reply = message.reply_to_message.message_id if message.reply_to_message else None
            await client.send_message(message.chat.id, message.text, reply_to_message_id=reply)
            ajablistic.append(message.text)
            payam[message.chat.id] = message
            await asyncio.sleep(3600)
            ajablistic.remove(message.text)

        payam[message.chat.id] = message
    except:
        pass
