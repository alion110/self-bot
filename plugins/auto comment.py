from pyrogram import Client as app, filters
import random
@app.on_message(filters.group & filters.forwarded)
async def post251saz(client, message):
    try:
        emojies = '🤣🍎💀🥶🍆😈😔🤘🏿🥳🥶✊🏾✌🏾👀🐸🌵🌱🌵👀💁🏽‍♂💆🏾‍♂🐊🐘🦧🦍🐫🦒🦘🐃🐂🐄🐐🦙🐑🐏🐖🐩🦃🐉🍀☘🎄🌲🦔🐿🦨🪐☄️⚡️✨☀🌟🌎🌙🌗🍎🥖🍣🥃🥎🛹🏌🏾‍♀🎤🎯🎮💣🧨🪓🔪⛓⚙🛠🔫⛏🩸💉🔑🎁'
        nuemo = len(emojies)
        rand = random.randint(0, int(nuemo))
        whi12 = emojies[rand]
        if message.forward_from_chat.username == 'ali_sarsakht':
            print(message)
            if message.forward_signature == 'Alion':
                print('yesssssssssss its alion')
            await client.send_message(message.chat.id,f'**پست شما خورده شد **{whi12}', reply_to_message_id=message.message_id)
        elif message.forward_from_chat.username == 'pgming':
            if message.forward_signature == 'Alireza':
                print('yesssssssssss its alireza')
                print(message)
                await client.send_message(message.chat.id,f'**پست شما خورده شد **{whi12}', reply_to_message_id=message.message_id)
        elif message.forward_from_chat.username == 'nigga57':
            if message.forward_signature == 'Amir':
                print('yesssssssssss its alion')
            print(message)
            await client.send_message(message.chat.id, 'hey i know that', reply_to_message_id=message.message_id)
        else:
            pass
    except:
        pass