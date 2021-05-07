# Urban Dictionary for catuserbot by @mrconfused
from PyDictionary import PyDictionary

from . import AioHttp


@bot.on(admin_cmd(pattern="ud (.*)"))
@bot.on(sudo_cmd(pattern="ud (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    word = event.pattern_match.group(1)
    try:
        response = await AioHttp().get_json(
            f"http://api.urbandictionary.com/v0/define?term={word}",
        )
        word = response["list"][0]["word"]
        definition = response["list"][0]["definition"]
        example = response["list"][0]["example"]
        result = "**Text: {}**\n**Meaning:**\n__{}__\n\n**Example:**\n__{}__".format(
            _format.replacetext(word),
            _format.replacetext(definition),
            _format.replacetext(example),
        )
        await edit_or_reply(event, result)
    except Exception as e:
        await edit_delete(
            event,
            text="__The Unban Dictionary API could not be reached__",
        )
        print(e)


@bot.on(admin_cmd(pattern="meaning (.*)"))
@bot.on(sudo_cmd(pattern="meaning (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    word = event.pattern_match.group(1)
    dictionary = PyDictionary()
    cat = dictionary.meaning(word)
    output = f"**Word :** __{word}__\n\n"
    try:
        for a, b in cat.items():
            output += f"**{a}**\n"
            for i in b:
                output += f"☞__{i}__\n"
        await edit_or_reply(event, output)
    except Exception:
        await edit_or_reply(event, f"Couldn't fetch meaning of {word}")


CMD_HELP.update(
    {
        "dictionary": "**Plugin :** __dictionary__\
    \n\n  •  **Syntax :** __.ud query__\
    \n  •  **Function : **fetches meaning from Urban dictionary\
    \n\n  •  **Syntax : **__.meaning query__\
    \n  •  **Function : **Fetches meaning of the given word\
    "
    }
)
