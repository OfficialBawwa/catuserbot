# inspired from uniborg Quotes plugin
import random

import requests


@bot.on(admin_cmd(pattern="quote ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="quote ?(.*)", allow_sudo=True))
async def quote_search(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "__Processing...__")
    input_str = event.pattern_match.group(1)
    if not input_str:
        api_url = "https://quotes.cwprojects.live/random"
        try:
            response = requests.get(api_url).json()
        except Exception:
            response = None
    else:
        api_url = f"https://quotes.cwprojects.live/search/query={input_str}"
        try:
            response = random.choice(requests.get(api_url).json())
        except Exception:
            response = None
    if response is not None:
        await catevent.edit(f"__{response['text']}__")
    else:
        await edit_delete(catevent, "__Sorry Zero results found__", 5)


CMD_HELP.update(
    {
        "quotes": "**Plugin : **__quotes__\
    \n\n**Syntax : **__.quote <category>__\
    \n**Function : **__An api that Fetchs random Quote from __goodreads.com____\
    "
    }
)
