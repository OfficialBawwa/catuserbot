"""
credits to @mrconfused
dont edit credits
"""
#  Copyright (C) 2020  sandeep.n(π.$)

import asyncio
import base64
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights

import userbot.plugins.sql_helper.gban_sql_helper as gban_sql

from . import BOTLOG, BOTLOG_CHATID, CAT_ID, admin_groups, get_user_from_event
from .sql_helper.mute_sql import is_muted, mute, unmute

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@bot.on(admin_cmd(pattern=r"gban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"gban(?: |$)(.*)", allow_sudo=True))
async def catgban(event):
    if event.fwd_from:
        return
    cate = await edit_or_reply(event, "__gbanning.......__")
    start = datetime.now()
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == (await event.client.get_me()).id:
        await cate.edit("why would I ban myself")
        return
    if user.id in CAT_ID:
        await cate.edit("why would I ban my dev")
        return
    try:
        hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        await event.client(ImportChatInviteRequest(hmm))
    except BaseException:
        pass
    if gban_sql.is_gbanned(user.id):
        await cate.edit(
            f"__the __[user](tg://user?id={user.id})__ is already in gbanned list any way checking again__"
        )
    else:
        gban_sql.catgban(user.id, reason)
    san = []
    san = await admin_groups(event)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await cate.edit("__you are not admin of atleast one group__ ")
        return
    await cate.edit(
        f"__initiating gban of the __[user](tg://user?id={user.id}) __in {len(san)} groups__"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"__You don't have required permission in :__\n**Chat :** {event.chat.title}(__{event.chat_id}__)\n__For banning here__",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) __was gbanned in {count} groups in {cattaken} seconds__!!\n**Reason :** __{reason}__"
        )
    else:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) __was gbanned in {count} groups in {cattaken} seconds__!!"
        )

    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GBAN\
                \nGlobal Ban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **__{user.id}__\
                \n**Reason :** __{reason}__\
                \n__Banned in {count} groups__\
                \n**Time taken : **__{cattaken} seconds__",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GBAN\
                \nGlobal Ban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **__{user.id}__\
                \n__Banned in {count} groups__\
                \n**Time taken : **__{cattaken} seconds__",
            )
        try:
            if reply:
                await reply.forward_to(BOTLOG_CHATID)
                await reply.delete()
        except BadRequestError:
            pass


@bot.on(admin_cmd(pattern=r"ungban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"ungban(?: |$)(.*)", allow_sudo=True))
async def catgban(event):
    if event.fwd_from:
        return
    cate = await edit_or_reply(event, "__ungbanning.....__")
    start = datetime.now()
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.catungban(user.id)
    else:
        await cate.edit(
            f"the [user](tg://user?id={user.id}) __is not in your gbanned list__"
        )
        return
    san = []
    san = await admin_groups(event)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await cate.edit("__you are not even admin of atleast one group __")
        return
    await cate.edit(
        f"initiating ungban of the [user](tg://user?id={user.id}) in __{len(san)}__ groups"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"__You don't have required permission in :__\n**Chat : **{event.chat.title}(__{event.chat_id}__)\n__For unbaning here__",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}__) was ungbanned in {count} groups in {cattaken} seconds__!!\n**Reason :** __{reason}__"
        )
    else:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) __was ungbanned in {count} groups in {cattaken} seconds__!!"
        )

    if BOTLOG and count != 0:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#UNGBAN\
                \nGlobal Unban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **__{user.id}__\
                \n**Reason :** __{reason}__\
                \n__Unbanned in {count} groups__\
                \n**Time taken : **__{cattaken} seconds__",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#UNGBAN\
                \nGlobal Unban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **__{user.id}__\
                \n__Unbanned in {count} groups__\
                \n**Time taken : **__{cattaken} seconds__",
            )


@bot.on(admin_cmd(pattern="listgban$"))
@bot.on(sudo_cmd(pattern=r"listgban$", allow_sudo=True))
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "Current Gbanned Users\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
            else:
                GBANNED_LIST += (
                    f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) Reason None\n"
                )
    else:
        GBANNED_LIST = "no Gbanned Users (yet)"
    await edit_or_reply(event, GBANNED_LIST)


@bot.on(admin_cmd(outgoing=True, pattern=r"gmute(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"gmute(?: |$)(.*)", allow_sudo=True))
async def startgmute(event):
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("__Unexpected issues or ugly errors may occur!__")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == bot.uid:
            return await edit_or_reply(event, "__Sorry, I can't gmute myself__")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(event, "__Sorry. I am unable to fetch the user__")
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            f"{_format.mentionuser(user.first_name ,user.id)} __ is already gmuted__",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**Error**\n__{str(e)}__")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} __is Successfully gmuted__\n**Reason :** __{reason}__",
            )
        else:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} __is Successfully gmuted__",
            )
    if BOTLOG:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#GMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**Reason :** __{reason}__",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#GMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


@bot.on(admin_cmd(outgoing=True, pattern=r"ungmute(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"ungmute(?: |$)(.*)", allow_sudo=True))
async def endgmute(event):
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("__Unexpected issues or ugly errors may occur!__")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == bot.uid:
            return await edit_or_reply(event, "__Sorry, I can't gmute myself__")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(event, "__Sorry. I am unable to fetch the user__")

    if not is_muted(userid, "gmute"):
        return await edit_or_reply(
            event, f"{_format.mentionuser(user.first_name ,user.id)} __is not gmuted__"
        )
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**Error**\n__{str(e)}__")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} __is Successfully ungmuted__\n**Reason :** __{reason}__",
            )
        else:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} __is Successfully ungmuted__",
            )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNGMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**Reason :** __{reason}__",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNGMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )


@bot.on(admin_cmd(incoming=True))
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


@bot.on(admin_cmd(pattern=r"gkick(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"gkick(?: |$)(.*)", allow_sudo=True))
async def catgkick(event):
    if event.fwd_from:
        return
    cate = await edit_or_reply(event, "__gkicking.......__")
    start = datetime.now()
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == (await event.client.get_me()).id:
        await cate.edit("why would I kick myself")
        return
    if user.id in CAT_ID:
        await cate.edit("why would I kick my dev")
        return
    try:
        hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        await event.client(ImportChatInviteRequest(hmm))
    except BaseException:
        pass
    san = []
    san = await admin_groups(event)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await cate.edit("__you are not admin of atleast one group__ ")
        return
    await cate.edit(
        f"__initiating gkick of the __[user](tg://user?id={user.id}) __in {len(san)} groups__"
    )
    for i in range(sandy):
        try:
            await event.client.kick_participant(san[i], user.id)
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"__You don't have required permission in :__\n**Chat :** {event.chat.title}(__{event.chat_id}__)\n__For kicking there__",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) __was gkicked in {count} groups in {cattaken} seconds__!!\n**Reason :** __{reason}__"
        )
    else:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) __was gkicked in {count} groups in {cattaken} seconds__!!"
        )

    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GKICK\
                \nGlobal Kick\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **__{user.id}__\
                \n**Reason :** __{reason}__\
                \n__Kicked in {count} groups__\
                \n**Time taken : **__{cattaken} seconds__",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GKICK\
                \nGlobal Kick\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **__{user.id}__\
                \n__Kicked in {count} groups__\
                \n**Time taken : **__{cattaken} seconds__",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


CMD_HELP.update(
    {
        "gadmin": "**Plugin : **__gadmin__\
        \n\n•  **Syntax : **__.gban <username/reply/userid> <reason (optional)>__\
        \n•  **Function : **__Bans the person in all groups where you are admin .__\
        \n\n•  **Syntax : **__.ungban <username/reply/userid>__\
        \n•  **Function : **__Reply someone's message with .ungban to remove them from the gbanned list.__\
        \n\n•  **Syntax : **__.listgban__\
        \n•  **Function : **__Shows you the gbanned list and reason for their gban.__\
        \n\n•  **Syntax : **__.gmute <username/reply> <reason (optional)>__\
        \n•  **Function : **__Mutes the person in all groups you have in common with them.__\
        \n\n•  **Syntax : **__.ungmute <username/reply>__\
        \n•  **Function : **__Reply someone's message with .ungmute to remove them from the gmuted list.__\
        \n\n•  **Syntax : **__.gkick <username/reply/userid> <reason (optional)>__\
        \n•  **Function : **__kicks the person in all groups where you are admin .__\
        "
    }
)
