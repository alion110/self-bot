from pyrogram import Client as app
from pyrogram import filters

@app.on_message(filters.reply & filters.me &filters.regex("^([Ii]d)$")) #get id by replying on messages
async def id(client, message):
    ids = message.reply_to_message.from_user.id
    await client.edit_message_text(message.chat.id, message.message_id, f'`{ids}`')

@app.on_message(filters.me & filters.regex("^\/ping$"))
async def ping(client, message):
    await client.edit_message_text(message.chat.id, message.message_id, "┈┅┅━━━━✦━━━━┅┅┈\n             Im Online\n┈┅┅━━━━✦━━━━┅┅┈")

@app.on_message(filters.me & filters.command(['load'], ['/','!','+','-','','*','~','#','$']))
async def loader(client, message):
    try:
        freete = '|'
        text111 = '███████████████████|'
        for i in text111:
            freete += i
            await client.edit_message_text(message.chat.id, message.message_id, freete)
        await client.edit_message_text(message.chat.id, message.message_id, 'Completely Loaded !')
    except:
        pass
