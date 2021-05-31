from pyrogram import Client as app , filters
import json, time,asyncio
from prettytable import PrettyTable
last = time.time()
def bla(sec):
    asyncio.sleep(sec)
@app.on_message(filters.me & filters.command(['set_auto','auto', 'delkhar', 'khar', 'remove', 'addvoice', 'answers'],['/','!','+','-','','*','~','#','$','']))
async def databasing(client, message):
    try:
        with open('users.json', 'r', encoding='utf8') as jsonfile:
            data = json.load(jsonfile)
        if 'answers' in message.text:
            table = PrettyTable()
            idlist = []
            table.field_names =['فرد', 'جواب']
            text = 'لیست جواب خودکار : \n'
            for id in data['autoanswer']:
                idlist.append(id)
                T = data["autoanswer"][id]
                table.add_row([f'[{id}](tg://user?id={id})', T])
                #text += f'[{id}](tg://user?id={id}) : {T} \n'
                if len(idlist) == 5:
                    await client.send_message(message.chat.id, table, reply_to_message_id=message.message_id)
                    idlist = []
                    table.clear_rows()

        if 'auto' in message.text and 'set' not in message.text:
            answer = message.text.split('auto')[1]
            for i in data["autoanswer"]:
                if i == str(message.reply_to_message.from_user.id):
                    data["autoanswer"][str(message.reply_to_message.from_user.id)] = answer

            data['autoanswer'][str(message.reply_to_message.from_user.id)] = answer
            with open('users.json', 'w', encoding='utf8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            await client.edit_message_text(message.chat.id, message.message_id, f'''
            **Auto Answer Changed to : ** __{answer}__''')


        if 'khar' in message.text and 'delkhar' not in message.text:
            for i in data["blocklist"]:
                if i == str(message.reply_to_message.from_user.id):
                    await app.delete_messages(message.chat.id, message.message_id)
                    return
            data['blocklist'].append(str(message.reply_to_message.from_user.id))
            with open('users.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            await client.edit_message_text(message.chat.id, message.message_id, '**دیگه حساب نیستی فانداک !**')


        if 'delkhar' in message.text:
            uid = message.reply_to_message.from_user.id
            for i in data["blocklist"]:
                if i == str(uid):
                    data["blocklist"].remove(str(i))
            with open('users.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            await client.edit_message_text(message.chat.id, message.message_id, "**حساب شدی بی آبرو**")

        if 'remove' in message.text:
            uid = message.reply_to_message.from_user.id
            if str(uid) in data["autoanswer"]:
                data["autoanswer"].pop(str(uid))
            with open('users.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            await app.delete_messages(message.chat.id, message.message_id)
        if 'addvoice' in message.text:
            fid = message.reply_to_message.message_id
            texts = message.text.split('addvoice ')[1]
            for i in texts.split(' '):
                data["voice"][i] = fid
            with open('users.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            await client.edit_message_text(message.chat.id, message.message_id, "**ست شد !**")

    except Exception as r:
        print(r)


@app.on_message(filters.mentioned)
async def mentionedme(client, message):
    global last
    try:
        rp = message.reply_to_message
        if rp:
            if rp.from_user.id == 1223702732 and not '@' in message.text:
                return
        if time.time() - last < 10:
            return
        default = "حق با توعه"
        print('hey')
        with open('users.json', 'r', encoding='utf-8') as jsonfile:
            data = json.loads(jsonfile.read())
        last = time.time()
        if str(message.from_user.id) in data['blocklist']:
            print('blocked user !')
            return
        for userid in data['autoanswer']:
            print('auto answering ...')
            if int(userid) == message.from_user.id:
                print('it exists...')
                print('getting from db')
                await client.send_message(message.chat.id, data['autoanswer'][str(userid)], reply_to_message_id=message.message_id)
                await bla(20)
                return
        await client.send_message(message.chat.id, default, reply_to_message_id=message.message_id)
        await bla(20)
        last = time.time()
    except Exception as t:
        print(t)
