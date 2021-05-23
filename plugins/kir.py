from pyrogram import Client as app
from pyrogram import filters

@app.on_message(filters.me & filters.command(['kir'], ['/','!','+','-','']))
async def kirekhar(client, message):
    print('kire khar')
    for i in range(int(message.text.split('=')[1])):
        await client.send_message(message.chat.id, message.text.split('kir')[1].split('=')[0] , reply_to_message_id=message.reply_to_message.message_id)
    await client.delete_messages(message.chat.id, message.message_id)



