import requests
import time

#https://discord.com/api/v9/channels/490935325259202560/messages

payload = {
    'content': 'Hey, My name is Dev Periwal'
}

header = {
    'authorization': 'NzUzODM0NjY4NTkxMTUzMTYy.YYtfMA.Yx7rIi8kFbRqPkMUzFITz5bTvsg'
}


while True:
    time.sleep(60)
    r = requests.post('https://discord.com/api/v9/channels/490935325259202560/messages', data=payload, headers=header)