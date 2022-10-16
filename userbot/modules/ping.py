# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

import redis
from speedtest import Speedtest

from userbot import (
    CMD_HANDLER as cmd,
    ALIVE_NAME,
    CMD_HELP,
    DEVS, 
    StartTime,
)
from userbot.events import register
from userbot.utils import toni_cmd, edit_or_reply

absen = [
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak** 😉",
    "**Hadir bang Tonic** 😁",
    "**Hadir kak maap telat** 🥺",
    "**Absen teros ajg**😊",
]

pacar = [
    "**Kamu mau jadi pacar aku ga?** 💘",
    "**Tonic mending sama aku** 😎",
    "**Hai ganteng** 🐷",
    "**Mau ga bang jadi pacar aku?** 😁",
    "**Mending pc aku bang** 🥺",
]

cping = [
    "**Hadir bang** `𓆩79.08𓆪` ",
    "**Hadir kak** `𓆩99.65𓆪` ",
    "**Hadir om** `𓆩76.89𓆪` ",
    "**Hadir sayang** `𓆩72.69𓆪` ",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=DEVS, pattern=r"^.absen$")
async def _(tonic):
    await tonic.reply(random.choice(absen))


@register(incoming=True, from_users=DEVS, pattern=r"^.pacar$")
async def _(asadekontol):
    await asadekontol.reply(random.choice(pacar))


@register(incoming=True, from_users=DEVS, pattern=r"^.cping$")
async def _(tonic):
    await tonic.reply(random.choice(cping))


@toni_cmd(pattern="sping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**🐖 ADA BABI🐖 **")
    await pong.edit("**🐖🐖 ADA BABI 🐖🐖**")
    await pong.edit("**🐖🐖🐖 ADA BABI 🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖 LU BABI 🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖 OINKK 🐖🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖🐖 OINKK 🐖🐖🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖🐖🐖 OINKK 🐖🐖🐖🐖🐖🐖🐖**")
    await pong.edit("`.................🐖`")
    await pong.edit("`................🐖.`")
    await pong.edit("`...............🐖..`")
    await pong.edit("`..............🐖...`")
    await pong.edit("`.............🐖....`")
    await pong.edit("`............🐖.....`")
    await pong.edit("`...........🐖......`")
    await pong.edit("`..........🐖.......`")
    await pong.edit("`.........🐖........`")
    await pong.edit("`........🐖.........`")
    await pong.edit("`.......🐖..........`")
    await pong.edit("`......🐖...........`")
    await pong.edit("`.....🐖............`")
    await pong.edit("`....🐖.............`")
    await pong.edit("`...🐖..............`")
    await pong.edit("`..🐖...............`")
    await pong.edit("`.🐖................`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**{ALIVE_NAME}**        \n"
        f"**➾Kecepatan : ** %sms  \n"
        f"**➾Branch : ** Tonic-Userbot \n" % (duration)
    )


@toni_cmd(pattern="lping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lping = await edit_or_reply(pong, "`Connecting...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await lping.edit(
        f"**`{ALIVE_NAME}`**\n"
        f"✧ **-ꜱɪɢɴᴀʟ- :** "
        f"`%sms` \n"
        f"✧ **-ᴜᴘᴛɪᴍᴇ- :** "
        f"`{uptime}` \n" % (duration)
    )


@toni_cmd(pattern="xping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await edit_or_reply(pong, "__Sedang Memuat.__")
    await xping.edit("__Sedang Memuat..__")
    await xping.edit("__Sedang Memuat...__")
    await xping.edit("__Sedang Memuat..__")
    await xping.edit("__Sedang Memuat.__")
    await xping.edit("__Sedang Memuat...__")
    await xping.edit("__Sedang Memuat..__")
    await xping.edit("__Sedang Memuat.__")
    await xping.edit("__Sedang Memuat..__")
    await xping.edit("__Sedang Memuat...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"**✨ ᴛᴏɴɪᴄ ᴜsᴇʀʙᴏᴛ ✨**\n"
        f"➾ __Signal__    __:__ "
        f"`%sms` \n"
        f"➾ __Uptime__ __:__ "
        f"`{uptime}` \n" % (duration)
    )


@toni_cmd(pattern="sinyal$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    sinyal = await edit_or_reply(pong, "**Mengecek Sinyal...**")
    await sinyal.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await sinyal.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await sinyal.edit("**40% ████▒▒▒▒▒▒**")
    await sinyal.edit("**60% ██████▒▒▒▒**")
    await sinyal.edit("**80% ████████▒▒**")
    await sinyal.edit("**100% ██████████**")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await sinyal.edit(
        f"**✨ ᴛᴏɴɪᴄ ᴜsᴇʀʙᴏᴛ ✨**\n\n"
        f"** ▹  Sɪɢɴᴀʟ   :** "
        f"`%sms` \n"
        f"** ▹  Uᴘᴛɪᴍᴇ  :** "
        f"`{uptime}` \n"
        f"** ▹  Oᴡɴᴇʀ   :** `{ALIVE_NAME}` \n" % (duration)
    )


@toni_cmd(pattern="ping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping = await edit_or_reply(pong, "**✣**")
    await ping.edit("**✣✣**")
    await ping.edit("**✣✣✣**")
    await pong.edit("**◕‿- PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await ping.edit(
        f"**PONG!!🏓**\n"
        f"➥ **ᴘɪɴɢ:** "
        f"`%sms` \n"
        f"➥ **ᴜᴘᴛɪᴍᴇ:** "
        f"`{uptime}` \n"
        f"**➳ ᴍʏ ɴᴀᴍᴇ:** `{ALIVE_NAME}`" % (duration)
    )


@toni_cmd(pattern="kecepatan$")
async def speedtst(spd):
    """For .speed command, use SpeedTest to check server speeds."""
    kecepatan = await edit_or_reply(spd, "**Sedang Menjalankan Tes Kecepatan Jaringan,Mohon Tunggu...**")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await kecepatan.edit(
        "**Kecepatan Jaringan:\n**"
        " ━━━━━━━━━━━━━━━━━ \n"
        f"✧ **Dimulai Pada :**  \n"
        f"`{result['timestamp']}` \n"
        "✧ **Download:** "
        f"`{speed_convert(result['download'])}` \n"
        "✧ **Upload:** "
        f"`{speed_convert(result['upload'])}` \n"
        "✧ **Signal:** "
        f"`{result['ping']}` \n"
        "✧ **ISP:** "
        f"`{result['client']['isp']}` \n"
        "✧ **BOT:** ✨ ᴛᴏɴɪᴄ ᴜsᴇʀʙᴏᴛ ✨"
    )


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@toni_cmd(pattern="pong$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    pong = await edit_or_reply(pong, "**◕‿- P**")
    await pong.edit("**◕‿- PO**")
    await pong.edit("**◕‿- PON**")
    await pong.edit("**◕‿- PONG**")
    await pong.edit("**◕‿- PONG🏓**")
    await asyncio.sleep(1)
    await pong.edit("✨")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**⚡Oᴡɴᴇʀ : {ALIVE_NAME}**\n📗 `%sms`" % (duration))


@toni_cmd(pattern="pink$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    pink = await edit_or_reply(pong, "8✊===D")
    await pink.edit("8=✊==D")
    await pink.edit("8==✊=D")
    await pink.edit("8===✊D")
    await pink.edit("8==✊=D")
    await pink.edit("8=✊==D")
    await pink.edit("8✊===D")
    await pink.edit("8=✊==D")
    await pink.edit("8==✊=D")
    await pink.edit("8===✊D")
    await pink.edit("8==✊=D")
    await pink.edit("8=✊==D")
    await pink.edit("8✊===D")
    await pink.edit("8=✊==D")
    await pink.edit("8==✊=D")
    await pink.edit("8===✊D")
    await pink.edit("8===✊D💦")
    await pink.edit("8====D💦💦")
    await pink.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pink.edit(
        f"**KONTOL!! **\n**NGENTOT** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


CMD_HELP.update(
    {
        "ping": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ping` | `{cmd}lping` | `{cmd}xping` | `{cmd}sinyal` | `{cmd}sping` | `{cmd}pink`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}kecepatan`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}pong`\
         \n↳ : Sama Seperti Perintah Ping."
    }
)