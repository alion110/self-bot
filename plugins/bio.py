from pyrogram import Client as app
from pyrogram import filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import random,asyncio
async def bla(sec):
    await asyncio.sleep(sec)

biochi = True
async def biochanger(client, message):
    global biochi
    emojies = ['🌵','🌱','🌾','🪐','☄️','✨','🔥','💥','🌪','🌟','🌎','🌙','🧘🏽‍♂️','🎧','🎤','🎸','🎮','🎯','♟','🎙','💣','⚔️','🗡','🔮','📿','💊','🧬','🖤']
    emo = random.choice(emojies)
    await client.update_profile(bio=f"تاریخ یه فی البداهه اس{emo}")
    await client.send_message(-1001382846418, f'بیو به {emo}تغییر کرد')


scheduler = AsyncIOScheduler()
scheduler.add_job(biochanger, "interval", seconds=60)
scheduler.start()
