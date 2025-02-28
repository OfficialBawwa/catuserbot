# CatUserbot module for getting the weather of a city.

# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
import io
import json
from datetime import datetime

import aiohttp
import requests
from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz

from ..utils import errors_handler
from .sql_helper.globals import addgvar, gvarstatus


async def get_tz(con):
    # Get time zone of the given country. Credits: @aragon12 and @zakaryan2004.
    for c_code in c_n:
        if con == c_n[c_code]:
            return tz(c_tz[c_code][0])
    try:
        if c_n[con]:
            return tz(c_tz[con][0])
    except KeyError:
        return


@bot.on(admin_cmd(outgoing=True, pattern="climate( (.*)|$)"))
@bot.on(sudo_cmd(pattern="climate( (.*)|$)", allow_sudo=True))
@errors_handler
async def get_weather(weather):
    if weather.fwd_from:
        return
    if not Config.OPEN_WEATHER_MAP_APPID:
        return await edit_or_reply(
            weather, "__Get an API key from__ https://openweathermap.org/ __first.__"
        )
    input_str = "".join(weather.text.split(maxsplit=1)[1:])
    if not input_str:
        CITY = gvarstatus("DEFCITY") or "Delhi"
    else:
        CITY = input_str
    timezone_countries = {
        timezone: country
        for country, timezones in c_tz.items()
        for timezone in timezones
    }
    if "," in CITY:
        newcity = CITY.split(",")
        if len(newcity[1]) == 2:
            CITY = newcity[0].strip() + "," + newcity[1].strip()
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f"{country}"]
            except KeyError:
                return await edit_or_reply(weather, "__Invalid country.__")
            CITY = newcity[0].strip() + "," + countrycode.strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={Config.OPEN_WEATHER_MAP_APPID}"
    async with aiohttp.ClientSession() as _session:
        async with _session.get(url) as request:
            requeststatus = request.status
            requesttext = await request.text()
    result = json.loads(requesttext)
    if requeststatus != 200:
        return await edit_or_reply(weather, "__Invalid country.__")
    cityname = result["name"]
    curtemp = result["main"]["temp"]
    humidity = result["main"]["humidity"]
    min_temp = result["main"]["temp_min"]
    max_temp = result["main"]["temp_max"]
    pressure = result["main"]["pressure"]
    feel = result["main"]["feels_like"]
    desc = result["weather"][0]
    desc = desc["main"]
    country = result["sys"]["country"]
    sunrise = result["sys"]["sunrise"]
    sunset = result["sys"]["sunset"]
    wind = result["wind"]["speed"]
    winddir = result["wind"]["deg"]
    cloud = result["clouds"]["all"]
    ctimezone = tz(c_tz[country][0])
    time = datetime.now(ctimezone).strftime("%A, %I:%M %p")
    fullc_n = c_n[f"{country}"]
    # dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
    #        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    div = 360 / len(dirs)
    funmath = int((winddir + (div / 2)) / div)
    findir = dirs[funmath % len(dirs)]
    kmph = str(wind * 3.6).split(".")
    mph = str(wind * 2.237).split(".")

    def fahrenheit(f):
        temp = str(((f - 273.15) * 9 / 5 + 32)).split(".")
        return temp[0]

    def celsius(c):
        temp = str((c - 273.15)).split(".")
        return temp[0]

    def sun(unix):
        return datetime.fromtimestamp(unix, tz=ctimezone).strftime("%I:%M %p")

    await edit_or_reply(
        weather,
        f"🌡**Temperature:** __{celsius(curtemp)}°C | {fahrenheit(curtemp)}°F__\n"
        + f"🥰**Human Feeling** __{celsius(feel)}°C | {fahrenheit(feel)}°F__\n"
        + f"🥶**Min. Temp.:** __{celsius(min_temp)}°C | {fahrenheit(min_temp)}°F__\n"
        + f"🥵**Max. Temp.:** __{celsius(max_temp)}°C | {fahrenheit(max_temp)}°F__\n"
        + f"☁️**Humidity:** __{humidity}%__\n"
        + f"🧧**Pressure** __{pressure} hPa__\n"
        + f"🌬**Wind:** __{kmph[0]} kmh | {mph[0]} mph, {findir}__\n"
        + f"⛈**Cloud:** __{cloud} %__\n"
        + f"🌄**Sunrise:** __{sun(sunrise)}__\n"
        + f"🌅**Sunset:** __{sun(sunset)}__\n\n\n"
        + f"**{desc}**\n"
        + f"__{cityname}, {fullc_n}__\n"
        + f"__{time}__\n",
    )


@bot.on(admin_cmd(outgoing=True, pattern="setcity(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="setcity(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def set_default_city(city):
    if city.fwd_from:
        return
    if not Config.OPEN_WEATHER_MAP_APPID:
        return await edit_or_reply(
            city, "__Get an API key from__ https://openweathermap.org/ __first.__"
        )
    if not city.pattern_match.group(1):
        CITY = gvarstatus("DEFCITY") or "Delhi"
    else:
        CITY = city.pattern_match.group(1)
    timezone_countries = {
        timezone: country
        for country, timezones in c_tz.items()
        for timezone in timezones
    }
    if "," in CITY:
        newcity = CITY.split(",")
        if len(newcity[1]) == 2:
            CITY = newcity[0].strip() + "," + newcity[1].strip()
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f"{country}"]
            except KeyError:
                return await edit_or_reply(city, "__Invalid country.__")
            CITY = newcity[0].strip() + "," + countrycode.strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={Config.OPEN_WEATHER_MAP_APPID}"
    request = requests.get(url)
    result = json.loads(request.text)
    if request.status_code != 200:
        return await edit_or_reply(city, "__Invalid country.__")
    addgvar("DEFCITY", CITY)
    cityname = result["name"]
    country = result["sys"]["country"]
    fullc_n = c_n[f"{country}"]
    await edit_or_reply(city, f"__Set default city as {cityname}, {fullc_n}.__")


@bot.on(admin_cmd(pattern="weather ?(.*)"))
@bot.on(sudo_cmd(pattern="weather ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        input_str = gvarstatus("DEFCITY") or "Delhi"
    output = requests.get(f"https://wttr.in/{input_str}?mnTC0&lang=en").text
    await edit_or_reply(event, output, parse_mode=parse_pre)


@bot.on(admin_cmd(pattern="wttr ?(.*)"))
@bot.on(sudo_cmd(pattern="wttr ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    if not input_str:
        input_str = gvarstatus("DEFCITY") or "Delhi"
    async with aiohttp.ClientSession() as session:
        sample_url = "https://wttr.in/{}.png"
        response_api_zero = await session.get(sample_url.format(input_str))
        response_api = await response_api_zero.read()
        with io.BytesIO(response_api) as out_file:
            await event.reply(
                f"**City : **__{input_str}__", file=out_file, reply_to=reply_to_id
            )
    try:
        await event.delete()
    except Exception as e:
        LOGS.info(str(e))


CMD_HELP.update(
    {
        "climate": "**Plugin : **__climate__\
        \n\n•  **Syntax : **__.climate <city>__\
        \n•  **Function : **__Gets the weather of a city. By default it is Delhi, change it by setcity__\
        \n\n•  **Syntax : **__.setcity <city> or <country name/code>__\
        \n•  **Function : **__Sets your default city so you can just use .weather or .climate.__\
        \n\n•  **Syntax : **__.weather <city>__\
        \n•  **Function : **__Gets the simple climate/weather information a city. By default it is Delhi, change it by setcity cmd__\
        \n\n•  **Syntax : **__.wttr <city> __\
        \n•  **Function : **__sends you the weather information for upcoming 3 days from today.__"
    }
)
