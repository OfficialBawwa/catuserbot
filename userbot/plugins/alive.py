import time
from platform import python_version

from telethon import version

from . import ALIVE_NAME, StartTime, catversion, get_readable_time, mention, reply_id

DEFAULTUSER = ALIVE_NAME or "cat"
CAT_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "✮ ඇයි ඇයි ආආහ්, එහා පැත්තේ run වෙනවා සොව්ඩි ✮"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  ✥ "


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        cat_caption += f"**{EMOJI} Database :** __{check_sgnirts}__\n"
        cat_caption += f"**{EMOJI} Tele uththe version :** __{version.__version__}\n__"
        cat_caption += f"**{EMOJI} Fkin userbot Version :** __{catversion}__\n"
        cat_caption += f"**{EMOJI} Pykana Version :** __{python_version()}\n__"
        cat_caption += f"**{EMOJI} Uptime :** __{uptime}\n__"
        cat_caption += f"**{EMOJI} My Fkin Master:** {mention}\n"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**{EMOJI} Database :** __{check_sgnirts}__\n"
            f"**{EMOJI} Tele uththe Version :** __{version.__version__}\n__"
            f"**{EMOJI} Fkin userbot Version :** __{catversion}__\n"
            f"**{EMOJI} Pykana Version :** __{python_version()}\n__"
            f"**{EMOJI} Uptime :** __{uptime}\n__"
            f"**{EMOJI} My Fkin Master:** {mention}\n",
        )


@bot.on(admin_cmd(outgoing=True, pattern="ialive$"))
@bot.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    reply_to_id = await reply_id(alive)
    cat_caption = f"**Cer, Your fkin userbot is Up and Running**\n"
    cat_caption += f"**  -Tele uththe version :** __{version.__version__}\n__"
    cat_caption += f"**  -FK userbot Version :** __{catversion}__\n"
    cat_caption += f"**  -Pykana Version :** __{python_version()}\n__"
    cat_caption += f"**  -My Fkin Master:** {mention}\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "**Plugin :** __alive__\
      \n\n  •  **Syntax : **__.alive__ \
      \n  •  **Function : **__status of bot will be showed__\
      \n\n  •  **Syntax : **__.ialive__ \
      \n  •  **Function : **__inline status of bot will be shown.__\
      \nSet __ALIVE_PIC__ var for media in alive message"
    }
)
