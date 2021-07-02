from pyrogram import Client,filters
import configparser,asyncio
configs = configparser.ConfigParser()
configs.read("config.ini")
api_id = int(configs.get("pyrogram","api_id"))
api_hash = str(configs.get("pyrogram","api_hash"))
print('>>> BOT STARTED')

app = Client('1BJWap1sBu3gGrhvj2CQrEXoDHpww-H6XQb1X0XSQ8jX8ZEMz2aEn2ZGRGtVKKil7KdsmfmD1h-JVnR-68DEBLcCyXJsMN7TOIUVWyxpcCcCntKuVMhC91Crbi0UknPHfaqRyz7AwjKIqeTMjIIFPoh6SkL0-G9ppW43C7fhT5H6vWA9caZS87IstKxfy6JS7rpjSsvTH9LLFtbebR6TEvbUq98UFNwzr3YzVOzY6n24OeYrX4xXQoKdGxUVbVkg8EOLrw6eGJvRXx9Y9mBvExW0uKC4gb0I581YTjt_-3SB8oz-ixc2uC3AOBWr1fbY657zeTXM82lpmMp3unbe-1hoNgDRXwh0=',config_file='config.ini')

app.run()
print('\n>>> BOT STOPPED')

