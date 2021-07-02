from pyrogram import Client,filters
import configparser,asyncio
configs = configparser.ConfigParser()
configs.read("config.ini")
api_id = int(configs.get("pyrogram","api_id"))
api_hash = str(configs.get("pyrogram","api_hash"))
print('>>> BOT STARTED')

app = Client('1BJWap1sBu0let_yfAfQYseESxLaUncqOE89aWOpc3IrMXTCD7F83rKi4aYIAGEdTBiqL26GU6Wa1n-kOKEVUGQ8wq8_4R72GV--EuBVlCh0zu7uH1WnR8rtQIy4guH-6Q_dn_gC9OKI2DT78jTWVCArO4pRoYfNO4jk8w1-j3W5pjuQa3nQi3UMERC3vA9_bAQ1sTbs0nSWyCnPnCew3YpFwLeLzLQMhbPcVf_zQbEuUQyKKlgGbie8NE7r8aCJkKrPBqWGIkw0nozT_HIZOrvo75DCfq6sEwZ9Pc3BUrhd-m9vUu1326g3brw9p_aSCoYG1puu98hgReChK9mosgxApOeTluDU=',config_file='config.ini')

app.run
print('\n>>> BOT STOPPED')

