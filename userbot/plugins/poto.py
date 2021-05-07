#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
----------------------------------------------------------------
All Thenks goes to Emily ( The creater of This Plugin)
\nSome credits goes to me ( @kirito6969 ) for ported this plugin
\nand __SnapDragon for__ Helping me.
----------------------------------------------------------------

Type __.poto__ for get **All profile pics of that User**
\nOr type __.poto (number)__ to get the **desired number of photo of a User** .
"""


name = "Profile Photos"


@bot.on(admin_cmd(pattern="poto ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="poto ?(.*)", allow_sudo=True))
async def potocmd(event):
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) > (len(photos)):
            return await edit_delete(
                event, "__No photo found of this NIBBA / NIBBI. Now u Die!__"
            )
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    elif uid.strip() == "all":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await edit_delete(event, "__This user has no photos to show you__")
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await edit_or_reply(
                    event, "______number Invalid!______ **Are you Comedy Me ?**"
                )
                return
        except BaseException:
            await edit_or_reply(event, "__Are you comedy me ?__")
            return
        if int(uid) > (len(photos)):
            return await edit_delere(
                event, "__No photo found of this NIBBA / NIBBI. Now u Die!__"
            )

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()


CMD_HELP.update(
    {
        "poto": """**Plugin : **__poto__

•  **Syntax : **__.poto__
•  **Function : **__reply to user to get his profile pic use command along \
with profile pic number to get desired pic else use .poto all to get all if you dont reply then gets group pics__"""
    }
)
