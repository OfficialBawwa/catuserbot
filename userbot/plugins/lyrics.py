# credits to @mrconfused (@sandy1709)
import io
import os

import lyricsgenius
from tswift import Song

GENIUS = os.environ.get("GENIUS_API_TOKEN", None)


@bot.on(admin_cmd(outgoing=True, pattern="lyrics ?(.*)"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="lyrics ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "wi8..! I am searching your lyrics....__")
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply.text:
        query = reply.message
    else:
        await catevent.edit("__What I am Supposed to find __")
        return
    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Couldn't find any lyrics for that song! try with artist name along with song if still doesnt work try __.glyrics__"
    else:
        reply = "lyrics not found! try with artist name along with song if still doesnt work try __.glyrics__"
    if len(reply) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to=reply_to_id,
            )
            await catevent.delete()
    else:
        await catevent.edit(reply)


@bot.on(admin_cmd(outgoing=True, pattern="glyrics ?(.*)"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="glyrics ?(.*)"))
async def lyrics(lyric):
    if lyric.pattern_match.group(1):
        query = lyric.pattern_match.group(1)
    else:
        await edit_or_reply(
            lyric,
            "Error: please use '-' as divider for <artist> and <song> \neg: __.glyrics Nicki Minaj - Super Bass__",
        )
        return
    if r"-" not in query:
        await edit_or_reply(
            lyric,
            "Error: please use '-' as divider for <artist> and <song> \neg: __.glyrics Nicki Minaj - Super Bass__",
        )
        return
    if GENIUS is None:
        await edit_or_reply(
            lyric,
            "__Provide genius access token to config.py or Heroku Var first kthxbye!__",
        )
    else:
        genius = lyricsgenius.Genius(GENIUS)
        try:
            args = query.split("-", 1)
            artist = args[0].strip(" ")
            song = args[1].strip(" ")
        except Exception as e:
            await edit_or_reply(lyric, f"Error:\n__{e}__")
            return
    if len(args) < 1:
        await edit_or_reply(lyric, "__Please provide artist and song names__")
        return
    catevent = await edit_or_reply(
        lyric, f"__Searching lyrics for {artist} - {song}...__"
    )
    try:
        songs = genius.search_song(song, artist)
    except TypeError:
        songs = None
    if songs is None:
        await catevent.edit(f"Song **{artist} - {song}** not found!")
        return
    if len(songs.lyrics) > 4096:
        await catevent.edit("__Lyrics is too big, view the file to see it.__")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Search query: \n{artist} - {song}\n\n{songs.lyrics}")
        await lyric.client.send_file(
            lyric.chat_id,
            "lyrics.txt",
            reply_to=lyric.id,
        )
        os.remove("lyrics.txt")
    else:
        await catevent.edit(
            f"**Search query**: \n__{artist} - {song}__\n\n______{songs.lyrics}______"
        )
    return


CMD_HELP.update(
    {
        "lyrics": "**Plugin : **__lyrics__\
        \n\n**Syntax : **__.lyrics <aritst name - song nane>__ __or__ __.lyrics <song_name>__\
        \n**Function : ** __searches a song lyrics and sends you if song name doesnt work try along with artisyt name__\
        \n\n**Syntax : ** .__glyrics <artist name> - <song name>__\
        \n**Function : **__genius lyrics finder for songs__\
        \n__note__: **-** is neccessary when searching the lyrics to divided artist and song\
        \nget this value from __https://genius.com/developers__ \
        \nAdd:-  __GENIUS_API_TOKEN__ and token value in heroku app settings for funtion of glyrics \
    "
    }
)
