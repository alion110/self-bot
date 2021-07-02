from pyrogram import Client,filters
import configparser,asyncio
configs = configparser.ConfigParser()
configs.read("config.ini")
api_id = int(configs.get("pyrogram","api_id"))
api_hash = str(configs.get("pyrogram","api_hash"))
print('>>> BOT STARTED')

app = Client('afsgbfdgbdfg',api_id,api_hash,config_file='config.ini')

app.run()
print('\n>>> BOT STOPPED')

