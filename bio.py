import os
import time
import requests

url = "https://discord.com/api/v9/users/@me/settings"

file = open("textapa.txt", "r")
lines = file.readlines()

def ChangeStatus(message):
    header = {
        "authorization": os.environ.get("DISCORD_TOKEN")
    }
    jsonData = {
        "status": "online",
        "custom_status": {"text": message}
    }
    requests.patch(url, headers=header, json=jsonData)

while True:
    for line in lines:
        ChangeStatus(line.strip())
        time.sleep(3)
