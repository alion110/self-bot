#Alion Self-Bot
from pyrogram import Client
print('>>> BOT STARTED')
try:
  Client("bot",api_id = 4109627,api_hash = '5874fe255bec03272faaa41ac22e55dc',config_file='config.ini').run()
except Exception as r:
  print(r)
print('\n>>> BOT STOPPED')

