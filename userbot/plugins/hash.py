# catuserbot module containing hash and encode/decode commands.

import asyncio
import base64
import os
import time
from subprocess import PIPE
from subprocess import run as runapp

from ..utils import errors_handler
from . import media_type, progress


@bot.on(admin_cmd(outgoing=True, pattern="hash (.*)"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="hash (.*)"))
@errors_handler
async def gethash(hash_q):
    if hash_q.fwd_from:
        return
    hashtxt_ = "".join(hash_q.text.split(maxsplit=1)[1:])
    with open("hashdis.txt", "w+") as hashtxt:
        hashtxt.write(hashtxt_)
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = f"**Text : **\
            \n__{hashtxt_}__\
            \n**MD5 : **__\
            \n__{md5}__\
            \n**SHA1 : **__\
            \n__{sha1}__\
            \n**SHA256 : **__\
            \n__{sha256}__\
            \n**SHA512 : **__\
            \n__{sha512[:-1]}__\
         "
    await edit_or_reply(hash_q, ans)


@bot.on(admin_cmd(outgoing=True, pattern="hbase (en|de) ?(.*)"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="hbase (en|de) ?(.*)"))
@errors_handler
async def endecrypt(event):
    if event.fwd_from:
        return
    string = "".join(event.text.split(maxsplit=2)[2:])
    catevent = event
    if event.pattern_match.group(1) == "en":
        if string:
            result = base64.b64encode(bytes(string, "utf-8")).decode("utf-8")
            result = f"**Shhh! It's Encoded : **\n__{result}__"
        else:
            reply = await event.get_reply_message()
            if not reply:
                return await edit_delete(event, "__What should i encode__")
            mediatype = media_type(reply)
            if mediatype is None:
                result = base64.b64encode(bytes(reply.text, "utf-8")).decode("utf-8")
                result = f"**Shhh! It's Encoded : **\n__{result}__"
            else:
                catevent = await edit_or_reply(event, "__Encoding ...__")
                c_time = time.time()
                downloaded_file_name = await event.client.download_media(
                    reply,
                    Config.TMP_DOWNLOAD_DIRECTORY,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, catevent, c_time, "trying to download")
                    ),
                )
                catevent = await edit_or_reply(event, "__Encoding ...__")
                with open(downloaded_file_name, "rb") as image_file:
                    result = base64.b64encode(image_file.read()).decode("utf-8")
        await edit_or_reply(
            catevent, result, file_name="encodedfile.txt", caption="It's Encoded"
        )
        os.remove(downloaded_file_name)
    else:
        lething = str(
            base64.b64decode(
                bytes(event.pattern_match.group(2), "utf-8"), validate=True
            )
        )[2:]
        await edit_or_reply(event, "Decoded: __" + lething[:-1] + "__")


CMD_HELP.update(
    {
        "hash": "**Plugin : **__hash__\
        \n\n**Syntax : **__.hbase en toencode-text or .hbase de encoded-text__\
        \n**Function : **__Find the base64 encoding of the given string or decoding of string__\
        \n\n**Syntax : **__.hash text__\
        \n**Function : **__Find the md5, sha1, sha256, sha512 of the string when written into a txt file.__"
    }
)
