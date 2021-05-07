# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @deleteduser420]
# ported to cat by @mrconfused (@sandy1709)

import os

import requests


@bot.on(admin_cmd(pattern="detect$", outgoing=True))
@bot.on(sudo_cmd(pattern="detect$", allow_sudo=True))
async def detect(event):
    if Config.DEEP_AI is None:
        return await edit_delete(
            event, "Add VAR __DEEP_AI__ get Api Key from https://deepai.org/", 5
        )
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "__Reply to any image or non animated sticker !__", 5
        )
    catevent = await edit_or_reply(event, "__Downloading the file to check...__")
    media = await event.client.download_media(reply)
    if not media.endswith(("png", "jpg", "webp")):
        return await edit_delete(
            event, "__Reply to any image or non animated sticker !__", 5
        )
    catevent = await edit_or_reply(event, "__Detecting NSFW limit...__")
    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={
            "image": open(media, "rb"),
        },
        headers={"api-key": Config.DEEP_AI},
    )
    os.remove(media)
    if "status" in r.json():
        return await edit_delete(catevent, r.json()["status"])
    r_json = r.json()["output"]
    pic_id = r.json()["id"]
    percentage = r_json["nsfw_score"] * 100
    detections = r_json["detections"]
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"<b>Detected Nudity :</b>\n<a href='{link}'>>>></a> __{percentage:.3f}%__\n\n"
    if detections:
        for parts in detections:
            name = parts["name"]
            confidence = int(float(parts["confidence"]) * 100)
            result += f"<b>• {name}:</b>\n   __{confidence} %__\n"
    await edit_or_reply(
        catevent,
        result,
        link_preview=False,
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "nsfwdetect": "**Plugin : **__nsfwdetect__\
    \n\n  •  **Syntax : **__.detect__\
    \n  •  **Function : **__Reply .detect command to any image or non animated sticker to detect the nudity in that__"
    }
)
