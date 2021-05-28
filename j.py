#Alion Self-Bot
from pyrogram import Client,filters
import os
print('>>> BOT STARTED')

app = Client("bot",api_id=4109627,api_hash='5874fe255bec03272faaa41ac22e55dc',config_file='config.ini')
app2 = Client('bot2', api_id=4109627,api_hash='5874fe255bec03272faaa41ac22e55dc')

#app2.run()
@app.on_message(filters.me & filters.command(['run2'], ['/','!','+','-','']))
async def run2bot(client, message):
  await client.send_message(message.chat.id, 'ران شد')
  app2.run()
app.run()
print('\n>>> BOT STOPPED')
