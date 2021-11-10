import requests
import time

#https://discord.com/api/v9/channels/490935325259202560/messages

payload = {
    'content': 'Hey, My name is Dev Periwal'
}

header = {
    'authorization': 'NzUzODM0NjY4NTkxMTUzMTYy.YYtZ7Q.v9j-EMNAYltwuUyo_CF0E5lcDiQ'
}

def send():
    r = requests.post('https://discord.com/api/v9/channels/490935325259202560/messages', data=payload, headers=header)


sending = True

while sending:
    time.sleep(60)
    send()