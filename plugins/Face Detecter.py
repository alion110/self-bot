import requests
from pyrogram import Client as app , filters

@app.on_message(filters.reply & filters.me & filters.command(['detect'],['/','!','+','-','']))
async def detect(client, message):
    if message.reply_to_message.photo:
        link_tel_file = None
        url = "https://deep-face-detect.p.rapidapi.com/prod"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': "d8d489e037msh938227ae35d9cd0p1e685ajsna381ea28caef",
            'x-rapidapi-host': "deep-face-detect.p.rapidapi.com"
        }
        payload = link_tel_file