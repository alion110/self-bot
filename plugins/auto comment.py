from pyrogram import Client as app, filters
import random
@app.on_message(filters.group & filters.forwarded)
async def post251saz(client, message):
    try:
        emojies = '๐คฃ๐๐๐ฅถ๐๐๐๐ค๐ฟ๐ฅณ๐ฅถโ๐พโ๐พ๐๐ธ๐ต๐ฑ๐ต๐๐๐ฝโโ๐๐พโโ๐๐๐ฆง๐ฆ๐ซ๐ฆ๐ฆ๐๐๐๐๐ฆ๐๐๐๐ฉ๐ฆ๐๐โ๐๐ฒ๐ฆ๐ฟ๐ฆจ๐ชโ๏ธโก๏ธโจโ๐๐๐๐๐๐ฅ๐ฃ๐ฅ๐ฅ๐น๐๐พโโ๐ค๐ฏ๐ฎ๐ฃ๐งจ๐ช๐ชโโ๐ ๐ซโ๐ฉธ๐๐๐'
        nuemo = len(emojies)
        rand = random.randint(0, int(nuemo))
        whi12 = emojies[rand]
        if message.forward_from_chat.username == 'ali_sarsakht':
            print(message)
            if message.forward_signature == 'Alion':
                print('yesssssssssss its alion')
            await client.send_message(message.chat.id,f'**ูพุณุช ุดูุง ุฎูุฑุฏู ุดุฏ **{whi12}', reply_to_message_id=message.message_id)
        elif message.forward_from_chat.username == 'pgming':
            if message.forward_signature == 'Alireza':
                print('yesssssssssss its alireza')
                print(message)
                await client.send_message(message.chat.id,f'**ูพุณุช ุดูุง ุฎูุฑุฏู ุดุฏ **{whi12}', reply_to_message_id=message.message_id)
        elif message.forward_from_chat.username == 'nigga57':
            if message.forward_signature == 'Amir':
                print('yesssssssssss its alion')
            print(message)
            await client.send_message(message.chat.id, 'hey i know that', reply_to_message_id=message.message_id)
        else:
            pass
    except:
        pass