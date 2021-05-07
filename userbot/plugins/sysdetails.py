"""Get the info your system. Using .neofetch then .sysd"""

# .spc command is ported from  alfianandaa/ProjectAlf
import platform
import sys
from datetime import datetime

import psutil
from telethon import __version__

from . import ALIVE_NAME

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
# ============================================


@bot.on(admin_cmd(outgoing=True, pattern=r"spc$"))
@bot.on(sudo_cmd(allow_sudo=True, pattern=r"spc$"))
async def psu(event):
    uname = platform.uname()
    softw = "**System Information**\n"
    softw += f"__System   : {uname.system}__\n"
    softw += f"__Release  : {uname.release}__\n"
    softw += f"__Version  : {uname.version}__\n"
    softw += f"__Machine  : {uname.machine}__\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"__Boot Time: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}__\n"
    # CPU Cores
    cpuu = "**CPU Info**\n"
    cpuu += "__Physical cores   : " + str(psutil.cpu_count(logical=False)) + "__\n"
    cpuu += "__Total cores      : " + str(psutil.cpu_count(logical=True)) + "__\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"__Max Frequency    : {cpufreq.max:.2f}Mhz__\n"
    cpuu += f"__Min Frequency    : {cpufreq.min:.2f}Mhz__\n"
    cpuu += f"__Current Frequency: {cpufreq.current:.2f}Mhz__\n\n"
    # CPU usage
    cpuu += "**CPU Usage Per Core**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"__Core {i}  : {percentage}%__\n"
    cpuu += "**Total CPU Usage**\n"
    cpuu += f"__All Core: {psutil.cpu_percent()}%__\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "**Memory Usage**\n"
    memm += f"__Total     : {get_size(svmem.total)}__\n"
    memm += f"__Available : {get_size(svmem.available)}__\n"
    memm += f"__Used      : {get_size(svmem.used)}__\n"
    memm += f"__Percentage: {svmem.percent}%__\n"
    # Bandwidth Usage
    bw = "**Bandwith Usage**\n"
    bw += f"__Upload  : {get_size(psutil.net_io_counters().bytes_sent)}__\n"
    bw += f"__Download: {get_size(psutil.net_io_counters().bytes_recv)}__\n"
    help_string = f"{str(softw)}\n"
    help_string += f"{str(cpuu)}\n"
    help_string += f"{str(memm)}\n"
    help_string += f"{str(bw)}\n"
    help_string += "**Engine Info**\n"
    help_string += f"__Python {sys.version}__\n"
    help_string += f"__Telethon {__version__}__"
    await event.edit(help_string)


def get_size(inputbytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if inputbytes < factor:
            return f"{inputbytes:.2f}{unit}{suffix}"
        inputbytes /= factor


@bot.on(admin_cmd(pattern="cpu$"))
@bot.on(sudo_cmd(pattern="cpu$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cmd = "cat /proc/cpuinfo | grep 'model name'"
    o = (await _catutils.runcmd(cmd))[0]
    await edit_or_reply(
        event, f"**[Cat's](tg://need_update_for_some_feature/) CPU Model:**\n{o}"
    )


@bot.on(admin_cmd(pattern=f"sysd$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"sysd$", allow_sudo=True))
async def sysdetails(sysd):
    cmd = "git clone https://github.com/dylanaraps/neofetch.git"
    await _catutils.runcmd(cmd)
    neo = "neofetch/neofetch --off --color_blocks off --bold off --cpu_temp C \
                    --cpu_speed on --cpu_cores physical --kernel_shorthand off --stdout"
    a, b, c, d = await _catutils.runcmd(neo)
    result = str(a) + str(b)
    await edit_or_reply(sysd, "Neofetch Result: __" + result + "__")


CMD_HELP.update(
    {
        "sysdetails": "**Plugin : **__sysdetails__\
        \n\n**Syntax : **__.spc__\
        \n**Function : **__Show system specification.__\
        \n\n**Syntax : **__.sysd__\
        \n**Function : **__Shows system information using neofetch.__\
        \n\n**Syntax : **__.cpu__\
        \n**Function : **__shows the cpu information__\
    "
    }
)
