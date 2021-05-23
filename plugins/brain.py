from pyrogram import Client as app, filters
import asyncio

@app.on_message(filters.me & filters.command(['brain'],['/','!','+','-','','*','~','#','$','']))
async def brain_func(client, message):
    animation_charts = [
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in range(14):
        await asyncio.sleep(0.2)
        await client.edit_message_text(message.chat.id, message.message_id, animation_charts[i % 14])

@app.on_message(filters.me & filters.command(['kill'],['/','!','+','-','','*','~','#','$','']))
async def killer(client, message):
    user = message.reply_to_message.from_user
    id = user.id
    name = user.first_name
    mentions = f'[{name}](tg://user?id={id})'
    animation_chars = [
        "killing...",
        "Ｆｉｉｉｉｉｒｅ",
        "(　･ิω･ิ)︻デ═一-->",
        "------>_____________",
        "--------->___⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠_______",
        "-------------->_____",
        "------------------->",
        "------>;(^。^)ノ",
        "(￣ー￣) DEAD",
        f"<b>{mentions} killed successfully (´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)</b>",
    ]
    for i in animation_chars:
        await asyncio.sleep(0.6)
        await client.edit_message_text(message.chat.id, message.message_id, animation_chars[i % 10])

@app.on_message(filters.me & filters.command(['kill'],['/','!','+','-','','*','~','#','$','']))
async def hack(client, message):
    animation_chars = [
        "```Connecting To Private Server \\```",
        "```Connecting To Private Server |```",
        "```Connecting To Private Server /```",
        "```Connecting To Private Server \\```",
        "```Connection Established ```",
        "```Target Selected```",
        "```Backdoor Found In Target```",
        "```Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒```",
        "```Hacking... 70%\n█████████████████▒▒▒▒▒```",
        "```Hacking... 88%\n█████████████████████▒```",
        "```Hacking... 100%\n███████████████████████```",
        "```Preparing Data... 1%\n▒██████████████████████```",
        "```Preparing Data... 14%\n████▒██████████████████```",
        "```Preparing Data... 30%\n████████▒██████████████```",
        "```Preparing Data... 55%\n████████████▒██████████```",
        "```Preparing Data... 72%\n████████████████▒██████```",
        "```Preparing Data... 88%\n████████████████████▒██```",
        "```Prepared Data... 100%\n███████████████████████```",
        "```Uploading Data to Server... 12%\n███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Uploading Data to Server... 44%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Uploading Data to Server... 68%\n███████████████▒▒▒▒▒▒▒▒```",
        "```Uploading Data to Server... 89%\n████████████████████▒▒▒```",
        "```Uploaded Data to Server... 100%\n███████████████████████```",
        "**User Data Upload Completed:** Target's User Data Stored "
        "at `downloads/victim/telegram-authuser.data.sql`",
    ]
    lenq = len(animation_chars)
    for i in range(lenq):
        await asyncio.sleep(2)
        await client.edit_message_text(message.chat.id, message.message_id, animation_chars[i % lenq])
    await client.edit_message_text(message.chat.id, message.message_id, '```Target Successfully Hacked```')
