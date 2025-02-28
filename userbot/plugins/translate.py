from asyncio import sleep

from googletrans import LANGUAGES, Translator

from . import BOTLOG, BOTLOG_CHATID, deEmojify
from .sql_helper.globals import addgvar, gvarstatus


@bot.on(admin_cmd(pattern="tl (.*)"))
@bot.on(sudo_cmd(pattern="tl (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif ";" in input_str:
        lan, text = input_str.split(";")
    else:
        await edit_delete(event, "__.tl LanguageCode__ as reply to a message", time=5)
        return
    text = deEmojify(text.strip())
    lan = lan.strip()
    Translator()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        output_str = f"**TRANSLATED from {LANGUAGES[translated.src].title()} to {LANGUAGES[lan].title()}**\
                \n__{after_tr_text}__"
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_delete(event, str(exc), time=5)


@bot.on(admin_cmd(outgoing=True, pattern=r"trt(?: |$)([\s\S]*)"))
@bot.on(sudo_cmd(allow_sudo=True, pattern=r"trt(?: |$)([\s\S]*)"))
async def translateme(trans):
    if trans.fwd_from:
        return
    textx = await trans.get_reply_message()
    message = trans.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(trans, "__Give a text or reply to a message to translate!__")
        return
    TRT_LANG = gvarstatus("TRT_LANG") or "en"
    try:
        reply_text = await getTranslate(deEmojify(message), dest=TRT_LANG)
    except ValueError:
        await edit_delete(trans, "__Invalid destination language.__", time=5)
        return
    source_lan = LANGUAGES[f"{reply_text.src.lower()}"]
    transl_lan = LANGUAGES[f"{reply_text.dest.lower()}"]
    reply_text = f"**From {source_lan.title()}({reply_text.src.lower()}) to {transl_lan.title()}({reply_text.dest.lower()}) :**\n__{reply_text.text}__"

    await edit_or_reply(trans, reply_text)
    if BOTLOG:
        await trans.client.send_message(
            BOTLOG_CHATID,
            f"__Translated some {source_lan.title()} stuff to {transl_lan.title()} just now.__",
        )


@bot.on(admin_cmd(pattern="lang trt (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lang trt (.*)", allow_sudo=True))
async def lang(value):
    if value.fwd_from:
        return
    arg = value.pattern_match.group(1).lower()
    if arg in LANGUAGES:
        addgvar("TRT_LANG", arg)
        LANG = LANGUAGES[arg]
    else:
        await edit_or_reply(
            value,
            f"__Invalid Language code !!__\n__Available language codes for TRT__:\n\n__{LANGUAGES}__",
        )
        return
    await edit_or_reply(value, f"__Language for Translator changed to {LANG.title()}.__")
    if BOTLOG:
        await value.client.send_message(
            BOTLOG_CHATID, f"__Language for Translator changed to {LANG.title()}.__"
        )


# https://github.com/ssut/py-googletrans/issues/234#issuecomment-722379788
async def getTranslate(text, **kwargs):
    translator = Translator()
    result = None
    for _ in range(10):
        try:
            result = translator.translate(text, **kwargs)
        except Exception:
            translator = Translator()
            await sleep(0.1)
    return result


CMD_HELP.update(
    {
        "translate": "**Plugin :** __translate__\
         \n\n**•  Syntax : **__.tl LanguageCode <text/reply>__\
         \n**•  Function : **__Translates given language to destination language. For <text> use .tl LanguageCode ; <text>__\
         \n\n**•  Syntax : **__.trt <Reply/text>__\
         \n**•  Function : **__It will translate your messege__\
         \n\n**•  Syntax : **__.lang trt LanguageCode__\
         \n**•  Function : **__It will set default langaugeCode for __**trt**__ command__\
         \n\n**•  Check here ** [Language codes](https://telegra.ph/Language-codes-11-01)\
        "
    }
)
