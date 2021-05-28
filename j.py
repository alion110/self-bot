#Alion Self-Bot
from pyrogram import Client,filters,idle
import os
print('>>> BOT STARTED')

app = Client("bot",api_id=4109627,api_hash='5874fe255bec03272faaa41ac22e55dc',config_file='config.ini')
app2 = Client('bot2', api_id=4109627,api_hash='5874fe255bec03272faaa41ac22e55dc')

#app2.run()
app.start()
app2.start()
@app2.on_message(filters.user(1223702732) & filters.command(['star'], ['/','!','+','-','']))
async def starme(client,message):
  tedad = int(message.text.split(' ')[1])
  for i in range(tedad):
    await message.reply_text('+')
  await client.send_message(message.chat.id, '**done !**')

@app.on_message(filters.me & filters.command(['run2'], ['/','!','+','-','']))
async def run2bot(client, message):
  await client.send_message(message.chat.id, 'ران شد')
  app2.run()
  
idle()
app.stop()
app2.stop()
print('\n>>> BOT STOPPED')
