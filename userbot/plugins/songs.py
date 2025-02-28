# by  @sandy1709 ( https://t.me/mrconfused  )

# songs finder for catuserbot
# reverse search by  @Lal_bakthan

import asyncio
import base64
import os
from pathlib import Path

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from . import name_dl, song_dl, video_dl, yt_search

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "__wi8..! I am finding your song....__"
SONG_NOT_FOUND = "__Sorry !I am unable to find any song like that__"
SONG_SENDING_STRING = "__yeah..! i found something wi8..🥰...__"
SONGBOT_BLOCKED_STRING = "__Please unblock @songdl_bot and try again__"
# =========================================================== #
#                                                             #
# =========================================================== #


@bot.on(admin_cmd(pattern="(song|song320)($| (.*))"))
@bot.on(sudo_cmd(pattern="(song|song320)($| (.*))", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply:
        if reply.message:
            query = reply.message
    else:
        await edit_or_reply(event, "__What I am Supposed to find __")
        return
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catevent = await edit_or_reply(event, "__wi8..! I am finding your song....__")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(
            f"Sorry!. I can't find any related video/audio for __{query}__"
        )
    cmd = event.pattern_match.group(1)
    if cmd == "song":
        q = "128k"
    elif cmd == "song320":
        q = "320k"
    song_cmd = song_dl.format(QUALITY=q, video_link=video_link)
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    stderr = (await _catutils.runcmd(song_cmd))[1]
    if stderr:
        return await catevent.edit(f"**Error :** __{stderr}__")
    catname, stderr = (await _catutils.runcmd(name_cmd))[:2]
    if stderr:
        return await catevent.edit(f"**Error :** __{stderr}__")
    # stderr = (await runcmd(thumb_cmd))[1]
    catname = os.path.splitext(catname)[0]
    # if stderr:
    #    return await catevent.edit(f"**Error :** __{stderr}__")
    song_file = Path(f"{catname}.mp3")
    if not os.path.exists(song_file):
        return await catevent.edit(
            f"Sorry!. I can't find any related video/audio for __{query}__"
        )
    await catevent.edit("__yeah..! i found something wi8..🥰__")
    catthumb = Path(f"{catname}.jpg")
    if not os.path.exists(catthumb):
        catthumb = Path(f"{catname}.webp")
    elif not os.path.exists(catthumb):
        catthumb = None

    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=query,
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (catthumb, song_file):
        if files and os.path.exists(files):
            os.remove(files)


async def delete_messages(event, chat, from_message):
    itermsg = event.client.iter_messages(chat, min_id=from_message.id)
    msgs = [from_message.id]
    async for i in itermsg:
        msgs.append(i.id)
    await event.client.delete_messages(chat, msgs)
    await event.client.send_read_acknowledge(chat)


@bot.on(admin_cmd(pattern="vsong( (.*)|$)"))
@bot.on(sudo_cmd(pattern="vsong( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        if reply.message:
            query = reply.messag
    else:
        event = await edit_or_reply(event, "What I am Supposed to find")
        return
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catevent = await edit_or_reply(event, "__wi8..! I am finding your song....__")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(
            f"Sorry!. I can't find any related video/audio for __{query}__"
        )
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    video_cmd = video_dl.format(video_link=video_link)
    stderr = (await _catutils.runcmd(video_cmd))[1]
    if stderr:
        return await catevent.edit(f"**Error :** __{stderr}__")
    catname, stderr = (await _catutils.runcmd(name_cmd))[:2]
    if stderr:
        return await catevent.edit(f"**Error :** __{stderr}__")
    # stderr = (await runcmd(thumb_cmd))[1]
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    # if stderr:
    #    return await catevent.edit(f"**Error :** __{stderr}__")
    catname = os.path.splitext(catname)[0]
    vsong_file = Path(f"{catname}.mp4")
    if not os.path.exists(vsong_file):
        vsong_file = Path(f"{catname}.mkv")
    elif not os.path.exists(vsong_file):
        return await catevent.edit(
            f"Sorry!. I can't find any related video/audio for __{query}__"
        )
    await catevent.edit("__yeah..! i found something wi8..🥰__")
    catthumb = Path(f"{catname}.jpg")
    if not os.path.exists(catthumb):
        catthumb = Path(f"{catname}.webp")
    elif not os.path.exists(catthumb):
        catthumb = None
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        force_document=False,
        caption=query,
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (catthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(pattern="song2 (.*)"))
@bot.on(sudo_cmd(pattern="song2 (.*)", allow_sudo=True))
async def cat_song_fetcer(event):
    if event.fwd_from:
        return
    song = event.pattern_match.group(1)
    chat = "@songdl_bot"
    reply_id_ = await reply_id(event)
    catevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(song)
            hmm = await conv.get_response()
            while hmm.edit_hide != True:
                await asyncio.sleep(0.1)
                hmm = await event.client.get_messages(chat, ids=hmm.id)
            baka = await event.client.get_messages(chat)
            if baka[0].message.startswith(
                ("I don't like to say this but I failed to find any such song.")
            ):
                await delete_messages(event, chat, purgeflag)
                return await edit_delete(
                    catevent, SONG_NOT_FOUND, parse_mode="html", time=5
                )
            await catevent.edit(SONG_SENDING_STRING, parse_mode="html")
            await baka[0].click(0)
            await conv.get_response()
            await conv.get_response()
            music = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(SONGBOT_BLOCKED_STRING, parse_mode="html")
            return
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b>➥ Song :- __{song}__</b>",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await catevent.delete()
        await delete_messages(event, chat, purgeflag)


@bot.on(admin_cmd(pattern="szm$", outgoing=True))
@bot.on(sudo_cmd(pattern="szm$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "______Reply to an audio message.______")
        return
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    catevent = await edit_or_reply(event, "______Identifying the song______")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(reply_message)
            check = await conv.get_response()
            if not check.text.startswith("Audio received"):
                return await catevent.edit(
                    "An error while identifying the song. Try to use a 5-10s long audio message."
                )
            await catevent.edit("Wait just a sec...")
            result = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("______Please unblock (@auddbot) and try again______")
            return
    namem = f"**Song Name : **__{result.text.splitlines()[0]}__\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
    await catevent.edit(namem)


CMD_HELP.update(
    {
        "songs": "**Plugin : **__songs__\
        \n\n•  **Syntax : **__.song <query/reply>__\
        \n•  **Function : **__searches the song you entered in query from youtube and sends it, quality of it is 128k__\
        \n\n•  **Syntax : **__.song320 <query/reply>__\
        \n•  **Function : **__searches the song you entered in query from youtube and sends it quality of it is 320k__\
        \n\n•  **Syntax : **__.vsong <query/reply>__\
        \n•  **Function : **__Searches the video song you entered in query and sends it__\
        \n\n•  **Syntax : **__.song2 query__\
        \n•  **Function : **__searches the song you entered in query and sends it quality of it is 320k__\
        \n\n**•  Syntax : **__.szm__ reply to an audio file\
        \n**•  Function :**Reverse searchs of song/music\
        "
    }
)
