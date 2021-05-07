# credits to @mrconfused (@sandy1709)

#  Copyright (C) 2020  sandeep.n(π.$)
import asyncio
import base64
import os
import re

from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)


@bot.on(admin_cmd(outgoing=True, pattern="fakegs(?: |$)(.*)", command="fakegs"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="fakegs(?: |$)(.*)", command="fakegs"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    reply_to_id = await reply_id(cat)
    if not text:
        if cat.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await edit_delete(cat, "__What should i search in google.__", 5)
            return
    cate = await edit_or_reply(cat, "__Connecting to https://www.google.com/ ...__")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            cat,
            "__How should i create meme follow the syntax as show__ __.fakegs top text ; bottom text__",
            5,
        )
        return
    catfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@bot.on(admin_cmd(outgoing=True, pattern="trump(?: |$)(.*)", command="trump"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="trump(?: |$)(.*)", command="trump"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(cat, "**Trump : **__What should I tweet__", 5)
            return
    cate = await edit_or_reply(cat, "__Requesting trump to tweet...__")
    try:
        hmm = Get(hmm)
        await cat.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await trumptweet(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@bot.on(admin_cmd(outgoing=True, pattern="modi(?: |$)(.*)", command="modi"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="modi(?: |$)(.*)", command="modi"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(cat, "**Modi : **__What should I tweet__", 5)
            return
    cate = await edit_or_reply(cat, "Requesting modi to tweet...")
    try:
        hmm = Get(hmm)
        await cat.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await moditweet(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@bot.on(admin_cmd(outgoing=True, pattern="cmm(?: |$)(.*)", command="cmm"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="cmm(?: |$)(.*)", command="cmm"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(cat, "__Give text to write on banner, man__", 5)
            return
    cate = await edit_or_reply(cat, "__Your banner is under creation wait a sec...__")
    try:
        hmm = Get(hmm)
        await cat.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await changemymind(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@bot.on(admin_cmd(outgoing=True, pattern="kanna(?: |$)(.*)", command="kanna"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="kanna(?: |$)(.*)", command="kanna"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(cat, "**Kanna : **__What should i show you__", 5)
            return
    cate = await edit_or_reply(cat, "__Kanna is writing your text...__")
    try:
        hmm = Get(hmm)
        await e.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await kannagen(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@bot.on(admin_cmd(outgoing=True, pattern="tweet(?: |$)(.*)", command="tweet"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="tweet(?: |$)(.*)", command="tweet"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(
                cat,
                "what should I tweet? Give some text and format must be like __.tweet username ; your text__ ",
                5,
            )
            return
    try:
        hmm = Get(hmm)
        await cat.client(hmm)
    except BaseException:
        pass
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            cat,
            "__what should I tweet? Give some text and format must be like__ __.tweet username ; your text__",
            5,
        )
        return
    cate = await edit_or_reply(cat, f"__Requesting {username} to tweet...__")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await tweets(text, username)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


CMD_HELP.update(
    {
        "imgmemes": """**Plugin : **__imgmemes__

  •  **Syntax : **__.fakegs search query ; what you mean text__
  •  **Function : **__Shows you image meme for your google search query__  

  •  **Syntax : **__.trump reply/text__
  •  **Function : **__sends you the trump tweet sticker with given custom text__

  •  **Syntax : **__.modi reply/text__
  •  **Function : **__sends you the modi tweet sticker with given custom text__ 

  •  **Syntax : **__.cmm reply/text__
  •  **Function : **__sends you the  Change my mind banner with given custom text__ 

  •  **Syntax : **__.kanna reply/text__
  •  **Function : **__sends you the kanna chan sticker with given custom text__  

  •  **Syntax : **__.tweet reply/<username> ; <text>__
  •  **Function : **__sends you the desired person tweet sticker with given custom text__ 
  """
    }
)
