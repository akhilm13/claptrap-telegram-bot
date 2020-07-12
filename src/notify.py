#! /usr/bin/python3
import sys
import requests 
import conf

chat_id = str(conf.bot["admin_chat_id"]);
key = conf.bot["key"];

if (len(sys.argv) < 2): 
    message = "A process that was being monitored was stopped but the message was empty";
else: 
    message = sys.argv[1];

url = "https://api.telegram.org/bot" + key + "/sendMessage?chat_id=" + chat_id + "&text=" + message;
requests.get(url);
