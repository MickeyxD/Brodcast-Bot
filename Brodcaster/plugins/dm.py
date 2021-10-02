import asyncio
from brodcaster.bot import bot
from telethon import events
from telethon import functions
from brodcaster.Config import log_id, sudo

chats = set()


@bot.on(events.NewMessage(pattern="/dcast"))
async def brodcaster(event):
    if event.sender_id in sudo:
        if event.is_reply:
            await event.edit("`processing...`")
            repl = await event.get_reply_message()
            chat_num = 0
            failed_chat = 0
            try:
                await bot(functions.channels.JoinChannelRequest("@CYRAX_BOTS_SUPPORT"))
                await bot(functions.channels.JoinChannelRequest("@CYRAX_BOTS_CHAT_GROUP"))
            except Exception as e:
                print(e)
                pass
            try:
                async for user in bot.iter_dialogs():
                    if user.is_user and not user.entity.bot:
                        ids = user.id
                        chats.add(ids)
                for i in chats:
                    try:
                        await event.client.send_message(i, repl)
                        chat_num += 1
                    except Exception as e:
                        failed_chat += 1
                await event.reply(f"**ᴍᴇꜱꜱᴀɢᴇ ꜱᴇɴᴅ ᴛᴏ: `{chat_num}` ᴜꜱᴇʀꜱ**")
            except Exception as e:
                await event.reply("🤖ꜱᴏᴍᴇᴛʜɪɴᴋ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʟᴏɢ ɢʀᴏᴜᴘ")
                await event.client.send_message(log_id, e)
                pass
        else:
            await event.reply("🤖ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ")
