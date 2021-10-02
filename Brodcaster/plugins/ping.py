from brodcaster.bot import bot
from telethon import events
from datetime import datetime
from brodcaster.Config import sudo


@bot.on(events.NewMessage(pattern="/ping"))
async def brodcaster(event):
    if event.sender_id in sudo:
        start = datetime.now()
        txt = "Pong!"
        event = await event.reply(txt)
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit(f"ᴘᴏɴɢ!🤖\n`{ms}` ᴍs")
