from telethon.utils import pack_bot_file_id


@bot.on(admin_cmd(pattern="(get_id|id)( (.*)|$)"))
@bot.on(sudo_cmd(pattern="(get_id|id)( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"__{str(e)}__", 5)
        try:
            if p.first_name:
                return await edit_or_reply(
                    event, f"The id of the user __{input_str}__ is __{p.id}__"
                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(
                        event, f"The id of the chat/channel __{p.title}__ is __{p.id}__"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "__Either give input as username or reply to user__")
    elif event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                f"**Current Chat ID : **__{str(event.chat_id)}__\n**From User ID: **__{str(r_msg.sender_id)}__\n**Media File ID: **__{bot_api_file_id}__",
            )
        else:
            await edit_or_reply(
                event,
                f"**Current Chat ID : **__{str(event.chat_id)}__\n**From User ID: **__{str(r_msg.sender_id)}__",
            )
    else:
        await edit_or_reply(event, f"**Current Chat ID : **__{str(event.chat_id)}__")


CMD_HELP.update(
    {
        "getid": "**Plugin : **__getid__\
    \n\n  •  **Syntax : **__.get_id__ or __.id__\
    \n  •  **Function : **__if given input then shows id of that given chat/channel/user else if you reply to user then shows id of the replied user \
    along with current chat id and if not replied to user or given input then just show id of the chat where you used the command__"
    }
)
