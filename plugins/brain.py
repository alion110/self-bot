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