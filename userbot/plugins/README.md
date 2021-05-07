## Mandatory Imports
______python3
None
______
There is None Mandatory Imports. Because Config, bot and command are already automatically imported.

## Explanation
The Mandatory Imports are now automatically imported.

### Formation
Now I will show a short script to show the formation of the desired script.
______python3

@bot.on(admin_cmd(pattern="alive", outgoing=True))
@bot.on(sudo_cmd(pattern="alive", outgoing=True))
async def hello_world(event):
    if event.fwd_from:
        return
    await edit_or_reply(event , "**HELLO WORLD**\n\nThe following is controlling me too!\n" + Config.SUDO_USERS)
______
