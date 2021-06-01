from pyrogram import Client,filters,idle
import configparser
configs = configparser.ConfigParser()
configs.read("config.ini")
api_id = int(configs.get("pyrogram","api_id"))
api_hash = str(configs.get("pyrogram","api_hash"))
print('>>> BOT STARTED')

app = Client("bot",api_id,api_hash,config_file='config.ini')
bot = Client("bot",api_id,api_hash,bot_token='1899785392:AAFvsm7835MbYcvKl0BkHTYuuOvhGa8HGc0',config_file='config.ini')
app.start()
bot.start()

bot.stop()
app.stop()

print('\n>>> BOT STOPPED')

