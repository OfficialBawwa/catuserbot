"""command: .hack & .thack """
# thx to @r4v4n4
import asyncio

from telethon.tl.functions.users import GetFullUserRequest

from . import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"


@bot.on(admin_cmd(pattern=r"hack$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"hack$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await event.client(GetFullUserRequest(reply_message.sender_id))
        idd = reply_message.sender_id
        if idd == 1035034432:
            await edit_or_reply(
                event, "This is My Master\nI can't hack my master's Account"
            )
        else:
            event = await edit_or_reply(event, "Hacking..")
            animation_chars = [
                "__Connecting To Hacked Private Server...__",
                "__Target Selected.__",
                "__Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ __",
                "__Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ __",
                "__Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ __",
                "__Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ __",
                "__Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ __",
                "__Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ __",
                "__Hacking... 84%\n█████████████████████▒▒▒▒ __",
                "__Hacking... 100%\n█████████HACKED███████████ __",
                f"__Targeted Account Hacked...\n\nPay 69$ To__ {DEFAULTUSER} . __To Remove this hack..__",
            ]
            animation_interval = 3
            animation_ttl = range(11)
            for i in animation_ttl:
                await asyncio.sleep(animation_interval)
                await event.edit(animation_chars[i % 11])
    else:
        await edit_or_reply(event, "No User is Defined\n Can't hack account")


@bot.on(admin_cmd(pattern=f"thack$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"thack$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(12)
    event = await edit_or_reply(event, "thack")
    animation_chars = [
        "**Connecting To Telegram Data Centre**",
        f"Target Selected By Hacker: {DEFAULTUSER}",
        "__Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ __\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
        "__Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ __\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package",
        "__Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ __\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)",
        "__Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ __\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'",
        "__Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ __\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e",
        "__Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ __\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b",
        "__Hacking... 84%\n█████████████████████▒▒▒▒ __\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**",
        "__Hacking... 100%\n█████████HACKED███████████ __\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**\n\n\n🔹Output: Generating.....",
        f"__Targeted Account Hacked...\n\nPay 699$ To__ {DEFAULTUSER} .__To Remove This Hack__\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**\n\n\n🔹**Output:** Successful",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@bot.on(admin_cmd(pattern=f"wahack$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"wahack$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(15)
    event = await edit_or_reply(event, "wahack..")
    animation_chars = [
        "Looking for WhatsApp databases in targeted person...",
        " User online: True\nTelegram access: True\nRead Storage: True ",
        "Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n__Looking for WhatsApp...__\nETA: 0m, 20s",
        "Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n__Looking for WhatsApp...__\nETA: 0m, 18s",
        "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n__Found folder C:/WhatsApp__\nETA: 0m, 16s",
        "Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n__Found folder C:/WhatsApp__\nETA: 0m, 14s",
        "Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n__Searching for databases__\nETA: 0m, 12s",
        "Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n__Found msgstore.db.crypt12__\nETA: 0m, 10s",
        "Hacking... 64.86%\n[███████████░░░░░░░░░]\n__Found msgstore.db.crypt12__\nETA: 0m, 08s",
        "Hacking... 74.02%\n[█████████████░░░░░░░]\n__Trying to Decrypt...__\nETA: 0m, 06s",
        "Hacking... 86.21%\n[███████████████░░░░░]\n__Trying to Decrypt...__\nETA: 0m, 04s",
        "Hacking... 93.50%\n[█████████████████░░░]\n__Decryption successful!__\nETA: 0m, 02s",
        "Hacking... 100%\n[████████████████████]\n__Scanning file...__\nETA: 0m, 00s",
        "Hacking complete!\nUploading file...",
        "Targeted Account Hacked...!\n\n ✅ File has been successfully uploaded to my server.\nWhatsApp Database:\n__./DOWNLOADS/msgstore.db.crypt12__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 15])


CMD_HELP.update(
    {
        "hack": "**Plugin : **__hack__\
        \n\n**Syntax : **__.hack reply to a person__\
        \n**Function : **__shows an animation of hacking progess bar__\
        \n\n**Syntax : **__.thack reply to a person__\
        \n**Function : **__shows an animation of Telegram account hacking to a replied person__\
        \n\n**Syntax : **__.wahack reply to a person__\
        \n**Function : **__shows an animation of whatsapp account hacking to a replied person__\
    "
    }
)
