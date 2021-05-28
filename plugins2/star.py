from pyrogram import Client as app2, filters

@app2.on_message(filters.user(1223702732) & filters.command(['star'], ['/','!','+','-','']))
async def starme(client,message):
  tedad = int(message.text.split(' ')[1])
  for i in range(tedad):
    await message.reply_text('+')
  await client.send_message(message.chat.id, '**done !**')
