# collage plugin for catuserbot by @sandy1709

# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

import os

from . import make_gif


@bot.on(admin_cmd(pattern="collage(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="collage(?: |$)(.*)", allow_sudo=True))
async def collage(cat):
    if cat.fwd_from:
        return
    catinput = cat.pattern_match.group(1)
    reply = await cat.get_reply_message()
    catid = cat.reply_to_msg_id
    cat = await edit_or_reply(
        cat, "______collaging this may take several minutes too..... 😁______"
    )
    if not (reply and (reply.media)):
        await cat.edit("__Media not found...__")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(catsticker)
        await cat.edit("__Media format is not supported...__")
        return
    if catinput:
        if not catinput.isdigit():
            os.remove(catsticker)
            await cat.edit("__You input is invalid, check help__")
            return
        catinput = int(catinput)
        if not 0 < catinput < 10:
            os.remove(catsticker)
            await cat.edit(
                "__Why too big grid you cant see images, use size of grid between 1 to 9__"
            )
            return
    else:
        catinput = 3
    if catsticker.endswith(".tgs"):
        hmm = await make_gif(cat, catsticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(catsticker)
            return await cat.edit(hmm)
        collagefile = hmm
    else:
        collagefile = catsticker
    endfile = "./temp/collage.png"
    catcmd = f"vcsi -g {catinput}x{catinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await _catutils.runcmd(catcmd))[:2]
    if not os.path.exists(endfile):
        for files in (catsticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await edit_delete(
            cat, f"__media is not supported or try with smaller grid size__", 5
        )
    await cat.client.send_file(
        cat.chat_id,
        endfile,
        reply_to=catid,
    )
    await cat.delete()
    for files in (catsticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "collage": "**Plugin : **__collage__\
        \n\n  •  **Syntax : **__.collage <grid size>__\
        \n  •  **Function : **__Shows you the grid image of images extracted from video \n Grid size must be between 1 to 9 by default it is 3__"
    }
)
