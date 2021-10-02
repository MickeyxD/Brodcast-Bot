
from telethon import TelegramClient
from brodcaster.Config import api_hash, api_id, string
from telethon.sessions import StringSession

if string:
    bot = TelegramClient(StringSession(string), api_id=api_id, api_hash=api_hash).start()
    print("client connected")
else:
    print("STRING SESSION NOT FOUND") 
