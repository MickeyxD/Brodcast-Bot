from brodcaster.bot import bot
from telethon import events
from telethon import functions
from brodcaster.Config import log_id, sudo

chats = set()
msg_id = set()


@bot.on(events.NewMessage(pattern="/bcast"))
async def brodcaster(event):
    if event.sender_id in sudo:
        if event.is_reply:
            txt = str(event.raw_text[7:])
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
                async for chat in bot.iter_dialogs():
                    ids = chat.id
                    chats.add(ids)
                if txt.lower() == "loud":
                    try:
                        for x in chats:
                            try:
                                semx = await bot.send_message(x, repl)
                                try:
                                    await bot.pin_message(x, semx.id)
                                except Exception as e:
                                    pass
                                chat_num += 1
                            except Exception as e:
                                failed_chat += 1
                        await event.reply(f"**ꜱᴇɴᴅ ɪɴ {chat_num} ᴄʜᴀᴛꜱ,  ᴜꜱᴇʀꜱ\nꜰᴀɪʟᴇᴅ ɪɴ {failed_chat} ᴄʜᴀᴛꜱ, ᴜꜱᴇʀꜱ**")
                    except Exception as e:
                        await event.reply("🤖ꜱᴏᴍᴇᴛʜɪɴᴋ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʟᴏɢ ɢʀᴏᴜᴘ")
                        await event.client.send_message(log_id, e)
                else:
                    for i in chats:
                        try:
                            await event.client.send_message(i, repl)
                            chat_num += 1
                        except Exception as e:
                            failed_chat += 1
                    await event.reply(f"**ꜱᴇɴᴅ ɪɴ {chat_num} ᴄʜᴀᴛꜱ\nꜰᴀɪʟᴇᴅ ɪɴ {failed_chat} ᴄʜᴀᴛꜱ**")
            except Exception as e:
                await event.reply("🤖ꜱᴏᴍᴇᴛʜɪɴᴋ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʟᴏɢ ɢʀᴏᴜᴘ")
                await event.client.send_message(log_id, e)
                pass
        else:
            await event.reply("🤖ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ")
