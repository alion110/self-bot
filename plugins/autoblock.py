from pyrogram import Client as app, filters
import json
with open('users.json', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)
if data['autoblock'] == 1:
    autoblock = True
else: autoblock = False

@app.on_message(filters.me & filters.command(['ablock'], ['']))
async def autoblock_en(client, message):
    global autoblock
    if autoblock:
        data['autoblock'] = 2
        with open('users.json', 'w', encoding='utf8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
    elif autoblock != True:
        data['autoblock'] = 1
        with open('users.json', 'w', encoding='utf8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
    await client.edit_message_text(message.chat.id, message.message_id, 'done')

@app.on_message(filters.private)
async def privater323(client, message):
    if message.from_user.id == 1223702732:
        return
    if autoblock:
        await client.send_message(message.chat.id,'در راستای جلوگیری از اسپم توسط افراد خاص اکانت شما به صورت موقت بلاک شد')
        await client.block_user(message.from_user.id)
