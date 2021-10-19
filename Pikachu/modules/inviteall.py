from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest

from Pikachu import *
from Pikachu.utils import lightning_cmd


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("ᴜsᴇʀɴᴀᴍᴇ ɢᴀʟᴀᴛ ʜᴀɪ ɢʀᴜᴘ ᴋᴀ..🌝")
            return None
        except ChannelPrivateError:
            await event.reply(
                "ʏᴇ ɢʀᴜᴘ ʏᴀ ᴛᴏ ᴘʀɪᴠᴀᴛᴇ ʜᴀɪ🤔 ʏᴀ ᴍᴜᴊʜᴇ ʙᴀɴ ᴋɪʏᴀ ʜᴀɪ ʏᴀʜᴀ..😅"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("ᴜsᴇʀɴᴀᴍᴇ ɢᴀʟᴀᴛ ʜᴀɪ ɢʀᴜᴘ ᴋᴀ..🌝")
            return None
        except (TypeError, ValueError):
            await event.reply("ᴜsᴇʀɴᴀᴍᴇ ɢᴀʟᴀᴛ ʜᴀɪ ɢʀᴜᴘ ᴋᴀ..🌝")
            return None
    return chat_info


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


@borg.on(lightning_cmd(pattern=r"allinvite ?(.*)"))
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("ᴘʀᴏᴄᴇssɪɴɢ...")
    else:
        rkp = await event.edit("ᴘʀᴏᴄᴇssɪɴɢ...")
    rk1 = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await rkp.edit("sᴏʀʀʏ🥺 ɴɪ ʜᴏ sᴀᴋᴛᴇ ᴍᴇᴍʙᴇʀs ᴀᴅᴅ..")
    s = 0
    f = 0
    error = "None"

    await rkp.edit("ʀᴜᴋᴏ ᴄʜᴜʀᴀ ʀʜᴀ ʜᴜ ᴍᴇᴍʙᴇʀs..😆")
    async for user in event.client.iter_participants(rk1.full_chat.id):
        try:
            if error.startswith("Too"):
                return await rkp.edit(
                    f"ʟɪᴍɪᴛᴇᴅ ʜᴏɢᴀʏᴀ ᴀᴄᴄ..🤐\n\n• ɪɴᴠɪᴛᴇᴅ »»» `{s}`  \n• ғᴀɪʟᴇᴅ ᴛᴏ ɪɴᴠɪᴛᴇ »»» `{f}` "
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await rkp.edit(
                f"ʀᴜᴋᴏ ᴄʜᴜʀᴀ ʀʜᴀ ʜᴜ ᴍᴇᴍʙᴇʀs..😆\n\n• ɪɴᴠɪᴛᴇᴅ »»» `{s}`  \n• ғᴀɪʟᴇᴅ ᴛᴏ ɪɴᴠɪᴛᴇ »»» `{f}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await rkp.edit(
        f"ᴄʜᴜʀᴀ ʟɪʏᴇ ᴍᴇᴍʙᴇʀs..😎 ᴀʙʙ @Iᴛs_JᴀssMᴀɴᴀᴋ ᴋᴏ 150$ sᴇɴᴅ ᴋʀᴏ\n\n• ɪɴᴠɪᴛᴇᴅ »»» `{s}`  \n• ғᴀɪʟᴇᴅ ᴛᴏ ɪɴᴠɪᴛᴇ »»» `{f}` "
