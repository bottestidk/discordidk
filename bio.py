import time 
import requests 

url = "https://discord.com/api/v9/users/@me/settings"

file = open("textapa.txt", "r")
lines = file.readlines()

def ChangeStatus(message):

    header = {
        "authorization": "MTAwNzY3ODIwODcxMzQzMzE1OA.Gddt_f.JH6pCBDDWs6u6NWQT_pDrIIvqCjJ2mOF2uoc5w"
    }
    
    jsonData = {
        "status": "online",
        "custom_status": {
            "text": message
        }
    }
    request = requests.patch(url, headers=header, json=jsonData)
    
while True:
        
            for line in lines:
                
                ChangeStatus(line.split("\n")[0])
                time.sleep(5)
                
                
                