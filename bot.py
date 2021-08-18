from pyrogram import Client,filters
import configparser,asyncio
configs = configparser.ConfigParser()
configs.read("config.ini")
api_id = int(configs.get("pyrogram","api_id"))
api_hash = str(configs.get("pyrogram","api_hash"))
print('>>> BOT STARTED')

app = Client('BABiRSUSsIK4A0cQbR1PTq1HN0Ik5dsDY8Y8FVSp7-wZo_sYARkov7uk7oLUP7dFxnCEzcgTF2J6tb4T00cO-qACv1AdbE_TuMeUIxdmXLl_MaZi_IBf0Sn0c7JHoXUfV9SxpVd-qvb8dgKN0qCHruEH-dhu07DoCRRsnLtPPVaaTxDfXvscfw6ObQ_Zgr8e4dI716b_Zjtc0jwDUDUeftoprMpA5LcS1qfbSTYiqVCnOq8UvmzGm8LZtkQ-ZMX1ZUdlPXM2BfeVg6_5phs4GeaOXkGjMjg1jWp9NZxz_SogtXTaVrNHNpBBmE8fTHsPcP1pLLp3Aoe2GxM03WBUicU4bXsq1gA',config_file='config.ini')

app.run()
print('\n>>> BOT STOPPED')

