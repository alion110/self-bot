from pyrogram import Client,filters

print('bot 2 started')
app2 = Client('bot2', api_id=4109627,api_hash='5874fe255bec03272faaa41ac22e55dc')

@app2.on_message(filters.user(1223702732) & filters.command(['star'], ['/','!','+','-','']))
async def starme(client,message):
  tedad = int(message.text.split(' ')[1])
  for i in range(tedad):
    await message.reply_text('+')
  await client.send_message(message.chat.id, '**done !**')
  
app2.run()
print('bot 2 stopped')