"""
By:- @Mrconfused & @sandy1709
idea from userage
"""
import asyncio
import io
import os
import shutil
import time
from pathlib import Path

from . import humanbytes


@bot.on(admin_cmd(pattern="ls ?(.*)", command="ls"))
@bot.on(sudo_cmd(pattern="ls ?(.*)", allow_sudo=True, command="ls"))
async def lst(event):
    cat = "".join(event.text.split(maxsplit=1)[1:])
    path = cat or os.getcwd()
    if not os.path.exists(path):
        await edit_or_reply(
            event,
            f"there is no such directory or file with the name __{cat}__ check again",
        )
        return
    path = Path(cat) if cat else os.getcwd()
    if os.path.isdir(path):
        if cat:
            msg = "Folders and Files in __{}__ :\n".format(path)
        else:
            msg = "Folders and Files in Current Directory :\n"
        lists = os.listdir(path)
        files = ""
        folders = ""
        for contents in sorted(lists):
            catpath = os.path.join(path, contents)
            if not os.path.isdir(catpath):
                size = os.stat(catpath).st_size
                if str(contents).endswith((".mp3", ".flac", ".wav", ".m4a")):
                    files += "🎵" + f"__{contents}__\n"
                if str(contents).endswith((".opus")):
                    files += "🎙" + f"__{contents}__\n"
                elif str(contents).endswith(
                    (".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")
                ):
                    files += "🎞" + f"__{contents}__\n"
                elif str(contents).endswith((".zip", ".tar", ".tar.gz", ".rar")):
                    files += "🗜" + f"__{contents}__\n"
                elif str(contents).endswith(
                    (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")
                ):
                    files += "🖼" + f"__{contents}__\n"
                else:
                    files += "📄" + f"__{contents}__\n"
            else:
                folders += f"📁__{contents}__\n"
        msg = msg + folders + files if files or folders else msg + "__empty path__"
    else:
        size = os.stat(path).st_size
        msg = f"The details of given file :\n"
        if str(path).endswith((".mp3", ".flac", ".wav", ".m4a")):
            mode = "🎵"
        if str(path).endswith((".opus")):
            mode = "🎙"
        elif str(path).endswith((".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")):
            mode = "🎞"
        elif str(path).endswith((".zip", ".tar", ".tar.gz", ".rar")):
            mode = "🗜"
        elif str(path).endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")):
            mode = "🖼"
        else:
            mode = "📄"
        time.ctime(os.path.getctime(path))
        time2 = time.ctime(os.path.getmtime(path))
        time3 = time.ctime(os.path.getatime(path))
        msg += f"**Location :** __{str(path)}__\n"
        msg += f"**icon :** __{mode}__\n"
        msg += f"**Size :** __{humanbytes(size)}__\n"
        msg += f"**Last Modified Time:** __{time2}__\n"
        msg += f"**Last Accessed Time:** __{time3}__"
    if len(msg) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(msg)) as out_file:
            out_file.name = "ls.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=path,
            )
            await event.delete()
    else:
        await edit_or_reply(event, msg)


@bot.on(admin_cmd(pattern="rem (.*)", command="rem"))
@bot.on(sudo_cmd(pattern="rem (.*)", command="rem", allow_sudo=True))
async def lst(event):
    cat = event.pattern_match.group(1)
    if cat:
        path = Path(cat)
    else:
        await edit_or_reply(event, "what should i delete")
        return
    if not os.path.exists(path):
        await edit_or_reply(
            event,
            f"there is no such directory or file with the name __{cat}__ check again",
        )
        return
    catcmd = f"rm -rf {path}"
    if os.path.isdir(path):
        await _catutils.runcmd(catcmd)
        await edit_or_reply(event, f"Succesfully removed __{path}__ directory")
    else:
        await _catutils.runcmd(catcmd)
        await edit_or_reply(event, f"Succesfully removed __{path}__ file")


@bot.on(admin_cmd(pattern="mkdir(?: |$)(.*)", outgoing=True, command="mkdir"))
@bot.on(sudo_cmd(pattern="mkdir(?: |$)(.*)", allow_sudo=True, command="mkdir"))
async def _(event):
    if event.fwd_from:
        return
    pwd = os.getcwd()
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await edit_delete(
            event,
            "What should i create ?",
            parse_mode=parse_pre,
        )
    original = os.path.join(pwd, input_str.strip())
    if os.path.exists(original):
        await edit_delete(
            event,
            f"Already a directory named {original} exists",
        )
        return
    mone = await edit_or_reply(
        event, "creating the directory ...", parse_mode=parse_pre
    )
    await asyncio.sleep(2)
    try:
        await _catutils.runcmd(f"mkdir {original}")
        await mone.edit(f"Successfully created the directory __{original}__")
    except Exception as e:
        await edit_delete(mone, str(e), parse_mode=parse_pre)


@bot.on(admin_cmd(pattern="cpto(?: |$)(.*)", outgoing=True, command="cpto"))
@bot.on(sudo_cmd(pattern="cpto(?: |$)(.*)", allow_sudo=True, command="cpto"))
async def _(event):
    if event.fwd_from:
        return
    pwd = os.getcwd()
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await edit_delete(
            event,
            "What and where should i move the file/folder.",
            parse_mode=parse_pre,
        )
    loc = input_str.split(";")
    if len(loc) != 2:
        return await edit_delete(
            event, "use proper syntax .cpto from ; to destination", parse_mode=parse_pre
        )
    original = os.path.join(pwd, loc[0].strip())
    location = os.path.join(pwd, loc[1].strip())

    if not os.path.exists(original):
        await edit_delete(
            event,
            f"there is no such directory or file with the name __{cat}__ check again",
        )
        return
    mone = await edit_or_reply(event, "copying the file ...", parse_mode=parse_pre)
    await asyncio.sleep(2)
    try:
        await _catutils.runcmd(f"cp -r {original} {location}")
        await mone.edit(f"Successfully copied the __{original}__ to __{location}__")
    except Exception as e:
        await edit_delete(mone, str(e), parse_mode=parse_pre)


@bot.on(admin_cmd(pattern="mvto(?: |$)(.*)", outgoing=True, command="mvto"))
@bot.on(sudo_cmd(pattern="mvto(?: |$)(.*)", allow_sudo=True, command="mvto"))
async def _(event):
    if event.fwd_from:
        return
    pwd = os.getcwd()
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await edit_delete(
            event,
            "What and where should i move the file/folder.",
            parse_mode=parse_pre,
        )
    loc = input_str.split(";")
    if len(loc) != 2:
        return await edit_delete(
            event, "use proper syntax .mvto from ; to destination", parse_mode=parse_pre
        )
    original = os.path.join(pwd, loc[0].strip())
    location = os.path.join(pwd, loc[1].strip())

    if not os.path.exists(original):
        await edit_delete(
            event,
            f"there is no such directory or file with the name __{cat}__ check again",
        )
        return
    mone = await edit_or_reply(event, "Moving the file ...", parse_mode=parse_pre)
    await asyncio.sleep(2)
    try:
        shutil.move(original, location)
        await mone.edit(f"Successfully moved the __{original}__ to __{location}__")
    except Exception as e:
        await edit_delete(mone, str(e), parse_mode=parse_pre)


CMD_HELP.update(
    {
        "filemanager": "**Plugin :**__filemanager__\
     \n\nList Files plugin for userbot \
     \n  •  **Syntax :** __.ls__\
     \n  •  **Function :** will return files from current working directory\
     \n\n  •  **Syntax :** .ls path\
     \n  •  **Function :** will return output according to path  \
     \n\n  •  **Syntax :** .ls file path\
     \n  •  **Function :** will return file details\
     \n\nSimple Module for people who dont wanna use shell executor for listing files.\
     \n\n  •  **Syntax :** __.rem path__\
     \n  •  **Function :** To delete the required item from the bot server\
     \n\n  •  **Syntax :** __.mkdir foldername__\
     \n  •  **Function :** Creates a new empty folder in the server\
     \n\n  •  **Syntax :** __.mvto frompath ; topath__\
     \n  •  **Function :** Move a file from one location to other location in bot server\
     \n\n  •  **Syntax :** __.cpto frompath ; topath__\
     \n  •  **Function :** Copy a file from one location to other location in bot server\
"
    }
)
