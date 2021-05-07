from asyncio import sleep


@bot.on(admin_cmd(pattern="sdm (\d*) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="sdm (\d*) (.*)", allow_sudo=True))
async def selfdestruct(destroy):
    cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    try:
        await destroy.delete()
    except Exception as e:
        LOGS.info(str(e))
    smsg = await destroy.client.send_message(destroy.chat_id, message)
    await sleep(ttl)
    await smsg.delete()


@bot.on(admin_cmd(pattern="selfdm (\d*) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="selfdm (\d*) (.*)", allow_sudo=True))
async def selfdestruct(destroy):
    cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    text = (
        message + f"\n\n__This message shall be self-destructed in {str(ttl)} seconds__"
    )
    try:
        await destroy.delete()
    except Exception as e:
        LOGS.info(str(e))
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(ttl)
    await smsg.delete()


CMD_HELP.update(
    {
        "selfdestruct": "**Plugin : **__selfdestruct__\
        \n\n**Syntax : **__.sdm [number] [text]__\
        \n**Function : **__self destruct this message in number seconds__\
        \n\n**Syntax : **__.selfdm [number] [text]__\
        \n**Function : **__self destruct this message in number seconds with showing that it will destruct. __\
"
    }
)
