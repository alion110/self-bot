from pyrogram import Client as app
from pyrogram import filters
import random,asyncio
async def bla(sec):
    await asyncio.sleep(sec)

biochi = True


@app.on_message(filters.me & filters.command(['startbio', 'bio'],['/','!','+','-','','*','~','#','$'])) #Change Biography every 60 seconds !
async def strtbio(client, message):
    global biochi
    try:
        emojies = ['🌵','🌱','🌾','🪐','☄️','✨','🔥','💥','🌪','🌟','🌎','🌙','🧘🏽‍♂️','🎧','🎤','🎸','🎮','🎯','♟','🎙','💣','⚔️','🗡','🔮','📿','💊','🧬','🖤']
        await client.edit_message_text(message.chat.id, message.message_id, '**تغییر خودکار بیو روشن شد✅**')
        while 1 == 1:
            rand = int(random.randint(0, 28))
            emo = emojies[rand]
            if biochi == False:
                break
            await client.update_profile(first_name='Alion',bio=f"تاریخ یه فی البداهه اس{emo}")
            await client.send_message(-1001382846418, f'بیو به {emo}تغییر کرد')
            await bla(60)
    except Exception as e:
        print(e)



@app.on_message(filters.me & filters.command(['stopbio', 'biooff'],['/','!','+','-','','*','~','#','$'])) #make off biography changer
async def stpbio(client, message):
    try:
        global biochi
        biochi = False
        await client.edit_message_text(message.chat.id, message.message_id, '**تغییر خودکار بیو خاموش شد❗️**')
    except Exception as r:
        print(r)
        
  
