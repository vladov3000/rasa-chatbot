#!/usr/bin/env python3

import requests

sender = "sender" 

bot_message = ""
while bot_message != "Bye":
    message = input(">")

    r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender": sender, "message": message})

    print("")
    for i in r.json():
        bot_message = i['text']
        print({i['text']})
