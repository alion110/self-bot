from pyrogram import Client as app, filters
import asyncio, json
text = '''سلام دوست عزیز👤
پیامتون دریافت شد و در اسرع وقت خوانده و پاسخ داده میشه🌺
ممنون از صبر و شکیبایی شما🙏'''

with open('users.json', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

@app.on_message(filters.private)
async def auto_private_answer(client, message):
    info = await client.get_users(message.from_user.id)
    if not info.is_contact:
        if not str(message.from_user.id) in data['pv'] and not message.from_user.id == 1223702732:
            await client.send_message(message.from_user.id, text)
            await client.send_message(1223702732, f'You Have a new message from [{message.from_user.first_name}](tg://user?id={message.from_user.id})\ntext : {message.text}')
            data['pv'].append(str(message.from_user.id))
            with open('users.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile)
            asyncio.sleep(3000)
            data['pv'].remove(str(message.from_user.id))
            with open('users.json', 'w') as jsonfile:
                json.dump(data, jsonfile)           
