from pyrogram import Client as app,filters 


@app.on_message(filters.group & filters.me & filters.command(['clm'],['/','!','+','-','','*','~','#']))
def clmember(client, message):
    can_not_remove = ['administrator', 'creator']
    try:
        client.edit_message_text(message.chat.id,message.message_id ,'**Deleting ...**')
        for member in client.iter_chat_members(message.chat.id):
            if member.status in can_not_remove:
                pass
            else:
                message.chat.kick_member(member.user.id)
        client.delete_messages(message.chat.id, message.message_id)
        client.send_message(message.chat.id, 'Done :)')

    except Exception as r:
        print(r)
        client.send_message(message.chat.id, f'```~ERROR : ``` {r}')
