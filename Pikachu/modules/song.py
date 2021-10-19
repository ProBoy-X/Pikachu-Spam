import asyncio
import os

import wget
from youtubesearchpython import SearchVideos

from Pikachu.Config import Var
from Pikachu.utils import lightning_cmd, edit_or_reply, sudo_cmd


@borg.on(lightning_cmd(pattern="ytmusic ?(.*)"))
@borg.on(sudo_cmd(pattern="ytmusic ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    myself_stark = await edit_or_reply(
        event, f"🌚ʀᴜᴋ ᴊᴀᴏ.. sᴀʙᴀʀ ᴋᴀʀᴏ.. ᴋʀʀᴀ ʜᴜ ᴅᴏᴡɴʟᴏᴀᴅ..🌝"
    )
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    if not os.path.isdir("./music/"):
        os.makedirs("./music/")
    path = Var.TEMP_DOWNLOAD_DIRECTORY
    sedlyf = wget.download(kekme, out=path)
    stark = (
        f'youtube-dl --force-ipv4 -q -o "./music/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality 128k '
        + mo
    )
    os.system(stark)
    await asyncio.sleep(4)
    km = f"./music/{thum}.mp3"
    if os.path.exists(km):
        await myself_stark.edit("🍁ʜᴏɢᴀʏᴀ ᴅᴏᴡɴʟᴏᴀᴅ ᴡᴀɪᴛ ᴋʀᴏ ᴜᴘʟᴏᴀᴅ ᴋʀᴛᴀ ʜᴜ..🍁")
    else:
        await myself_stark.edit("ᴇʀʀᴏʀ ᴀᴀɢᴀʏᴀ ʙʜᴀɪ.. sᴏʀʀʏ🥺")
    capy = f"**🎧sᴏɴɢ ɴᴀᴍᴇ🎧 ➠** `{thum}`\n**🦋ʏᴛ ʟɪɴᴋ🦋 ➠** `{mo}`"
    await borg.send_file(
        event.chat_id,
        km,
        force_document=False,
        allow_cache=False,
        caption=capy,
        thumb=sedlyf,
        performer=thums,
        supports_streaming=True,
    )
    await myself_stark.edit("🌸sᴏɴɢ ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ ᴘɪᴋᴀ ᴘɪᴋᴀ ᴘɪᴋᴀᴄʜᴜ..⚡️🌸")
    for files in (sedlyf, km):
        if files and os.path.exists(files):
            os.remove(files)
