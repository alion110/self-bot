#Alion Self-Bot
from pyrogram import Client
print('>>> BOT STARTED')
app = Client("bot",api_id=4109627,api_hash='5874fe255bec03272faaa41ac22e55dc',config_file='config.ini')
#app2 = Client('bot2', api_id=4109627,api_hash='5874fe255bec03272faaa41ac22e55dc', config_file='config2.ini')

app.run()
#app2.run()

print('\n>>> BOT STOPPED')
