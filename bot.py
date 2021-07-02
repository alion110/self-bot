from pyrogram import Client,filters,idle
import configparser,asyncio
configs = configparser.ConfigParser()
configs.read("config.ini")
api_id = int(configs.get("pyrogram","api_id"))
api_hash = str(configs.get("pyrogram","api_hash"))
print('>>> BOT STARTED')

app = Client('1BJWap1sBu0let_yfAfQYseESxLaUncqOE89aWOpc3IrMXTCD7F83rKi4aYIAGEdTBiqL26GU6Wa1n-kOKEVUGQ8wq8_4R72GV--EuBVlCh0zu7uH1WnR8rtQIy4guH-6Q_dn_gC9OKI2DT78jTWVCArO4pRoYfNO4jk8w1-j3W5pjuQa3nQi3UMERC3vA9_bAQ1sTbs0nSWyCnPnCew3YpFwLeLzLQMhbPcVf_zQbEuUQyKKlgGbie8NE7r8aCJkKrPBqWGIkw0nozT_HIZOrvo75DCfq6sEwZ9Pc3BUrhd-m9vUu1326g3brw9p_aSCoYG1puu98hgReChK9mosgxApOeTluDU=',config_file='config.ini')
bot = Client("bot",api_id,api_hash,bot_token='1899785392:AAFvsm7835MbYcvKl0BkHTYuuOvhGa8HGc0',config_file='config.ini')
@bot.on_message(filters.user(1223702732) & filters.command(['star'], ['/', '!', '+', '-', '']))
async def starbot(client, message):
  text = message.text.split('star')[1].split('=')[0]
  tedad = int(message.text.split('=')[1])
  if message.reply_to_message:
      rp = message.reply_to_message.message
      await asyncio.gether(*[client.send_message(message.chat.id, text, reply_to_message_id=rp) for i in range(tedad)])
  elif not message.reply_to_message:
      await asyncio.gether(*[client.send_message(message.chat.id, text) for i in range(tedad)])

app.start()
bot.start()
idle()
bot.stop()
app.stop()

print('\n>>> BOT STOPPED')

