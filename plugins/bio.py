from pyrogram import Client as app
from pyrogram import filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import random,asyncio
async def bla(sec):
    await asyncio.sleep(sec)

biochi = True
async def biochanger():
    global biochi
    emojies = ['🌵','🌱','🌾','🪐','☄️','✨','🔥','💥','🌪','🌟','🌎','🌙','🧘🏽‍♂️','🎧','🎤','🎸','🎮','🎯','♟','🎙','💣','⚔️','🗡','🔮','📿','💊','🧬','🖤']
    emo = random.choice(emojies)
    await app.update_profile(bio=f"تاریخ یه فی البداهه اس{emo}")
    await app.send_message(chat_id = -1001382846418, text=f'بیو به {emo}تغییر کرد')


scheduler = AsyncIOScheduler()
scheduler.add_job(biochanger, "interval", seconds=60)
scheduler.start()
