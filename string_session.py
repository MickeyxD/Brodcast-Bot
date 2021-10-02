from telethon import sessions
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print("")

API_ID = int(input("API_KEY: "))
API_HASH = input("API_HASH: ")

while True:
 try:
  with TelegramClient(StringSession(), API_ID, API_HASH) as client:
   print("String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!! ")
   print("")
   session = client.session.save()
   print(f"YOUR STRING SESSION IS\n{sessions}")
   client.send_message("me",f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)\n\n `{session}`")
 except:
  print("")
  print(
      "Wrong phone number \n make sure its with correct country code. Example : +918925534834! Kindly Retry"
  )
  print("")
  continue
 break
