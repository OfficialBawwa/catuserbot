# corona virus stats for catuserbot
from covid import Covid

from . import covidindia


@bot.on(admin_cmd(pattern="covid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="covid(?: |$)(.*)", allow_sudo=True))
async def corona(event):
    if event.pattern_match.group(1):
        country = (event.pattern_match.group(1)).title()
    else:
        country = "World"
    catevent = await edit_or_reply(event, "__Collecting data...__")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data["confirmed"] + country_data["new_cases"]
        hmm2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\n⚠️ Confirmed   : __{hmm1}__"
        data += f"\n😔 Active           : __{country_data['active']}__"
        data += f"\n⚰️ Deaths         : __{hmm2}__"
        data += f"\n🤕 Critical          : __{country_data['critical']}__"
        data += f"\n😊 Recovered   : __{country_data['recovered']}__"
        data += f"\n💉 Total tests    : __{country_data['total_tests']}__"
        data += f"\n🥺 New Cases   : __{country_data['new_cases']}__"
        data += f"\n😟 New Deaths : __{country_data['new_deaths']}__"
        await catevent.edit(
            "<b>Corona Virus Info of {}:\n{}</b>".format(country, data),
            parse_mode="html",
        )
    else:
        data = await covidindia(country)
        if data:
            cat1 = int(data["new_positive"]) - int(data["positive"])
            cat2 = int(data["new_death"]) - int(data["death"])
            cat3 = int(data["new_cured"]) - int(data["cured"])
            result = f"<b>Corona virus info of {data['state_name']}\
                \n\n⚠️ Confirmed   : __{data['new_positive']}__\
                \n😔 Active           : __{data['new_active']}__\
                \n⚰️ Deaths         : __{data['new_death']}__\
                \n😊 Recovered   : __{data['new_cured']}__\
                \n🥺 New Cases   : __{cat1}__\
                \n😟 New Deaths : __{cat2}__\
                \n😃 New cured  : __{cat3}__ </b>"
            await catevent.edit(result, parse_mode="html")
        else:
            await edit_delete(
                catevent,
                "__Corona Virus Info of {} is not avaiable or unable to fetch__".format(
                    country
                ),
                5,
            )


CMD_HELP.update(
    {
        "covid": "**Plugin : **__covid__\
        \n\n  •  **Syntax : **__.covid <country name>__\
        \n  •  **Function :** __Get an information about covid-19 data in the given country.__\
        \n\n  •  **Syntax : **__.covid <state name>__\
        \n  •  **Function :** __Get an information about covid-19 data in the given state of India only.__\
        "
    }
)
