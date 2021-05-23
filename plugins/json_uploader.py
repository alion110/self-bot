from pyrogram import Client as app , filters

@app.on_message(filoters.me & filters.command(['ujson'],['/','!','+','-','','*','~','#','$','']))
async def json_uploader(client, message):
    await client.send_document(message.chat.id, 'users.json')

