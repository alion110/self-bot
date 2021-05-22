from pyrogram import Client as app, filters
@app.on_message(filters.me &filters.command(['tag'],['/','!','+','-','']))
def tag(client, message):
    try:
        list5 = []
        ted1 = 0
        text = 'Members List :\n'
        num = '⚜'
        if int(message.text.split('g')[1]) > 0:
            ted = int(message.text.split('g')[1])
        if ted1 == ted:
            return
        for member in client.iter_chat_members(message.chat.id):
            list5.append(member.user.id)
            s = member.user.username if member.user.username else member.user.first_name
            text += f'{num}:[{s}](tg://user?id={member.user.id}) \n'

            if len(list5) == 5:
                text += '---------------'
                client.send_message(message.chat.id, text)
                text = ''
                list5 = []
                ted1 += 1

    except Exception as r:
        print(r)


@app.on_message(filters.me & filters.command(['slow'],['/','!','+','-','']))
def slow(client, message):
    try:
        sec = int(message.text.split('slow')[1])
        client.set_slow_mode(message.chat.id, sec)
        client.send_message(message.chat.id, f'__Slow Mode ```{str(sec)}``` Seconds!__')
    except Exception as r:
        print(r)
        client.send_message(message.chat.id, '__Error__', reply_to_message_id=message.message_id)


