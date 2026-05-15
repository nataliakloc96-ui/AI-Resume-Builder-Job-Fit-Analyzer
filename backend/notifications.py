import requests
import os

TOKEN = "8958954903:AAHY5iUd1XF9-JCQbUPyvuTe4k-3_FxjPiA"
CHAT_ID = "8163340105"

def send_alert(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })
    