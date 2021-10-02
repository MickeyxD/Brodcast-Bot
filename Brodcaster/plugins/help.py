from brodcaster.bot import bot
from telethon import events
from brodcaster.Config import sudo


@bot.on(events.NewMessage(pattern="/help"))
async def help(event):
    if event.sender_id in sudo:
        txt = '''**1: /bcast --> ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ɪɴ ᴀʟʟ ɢʀᴏᴜᴘ, ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴜꜱᴇʀꜱ
/bcast loud <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ> ᴛᴏ ᴘɪɴ ᴍᴇꜱꜱᴀɢᴇ ᴀʟꜱᴏ.
/bcast <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ> ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴡɪᴛʜᴏᴜᴛ ᴘɪɴ
2: /ccast --> ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ɪɴ ᴀʟʟ ᴄʜᴀɴɴᴇʟ ᴏɴʟʏ
/cast loud <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ> ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴡɪᴛʜ ᴘɪɴ.
/ccast <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ> ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴡɪᴛʜᴏᴜᴛ ᴘɪɴ
3: /dcast --> ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ɪɴ ᴀʟʟ ᴜꜱᴇʀꜱ
/dcast <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ>
4: /gcast --> ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ɪɴ ᴀʟʟ ɢʀᴏᴜᴘꜱ
/gcast loud <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ> ᴛᴏ ᴘɪɴ ᴍᴇꜱꜱᴀɢᴇ ᴀʟꜱᴏ.
/gcast <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ> ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴡɪᴛʜᴏᴜᴛ ᴘɪɴ
5: /ping --> ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ɪꜱ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ**'''
    await event.reply(txt)
