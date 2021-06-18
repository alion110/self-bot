from pyrogram import Client as app,filters
import asyncio
list = []
text = '''سلام دوست عزیز👤
پیامتون دریافت شد و در اسرع وقت خوانده و پاسخ داده میشه🌺
ممنون از صبر و شکیبایی شما🙏'''
@app.on_message(filters.private)
async def auto_private_answer(client, message):
    info = await client.get_users(message.from_user.id)
    if not info.is_contact:
        if not message.from_user.id in list and not message.from_user.id == 1223702732:
            await client.send_message(message.from_user.id, text)
            await client.send_message(1223702732, f'You Have a new message from [{message.from_user.first_name}](tg://user?id={message.from_user.id})\ntext : {message.text}')
            list.append(message.from_user.id)
            asyncio.sleep(300)
            list.remove(message.from_user.id)

        
