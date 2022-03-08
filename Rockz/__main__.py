#
# Copyright (C) 2021-2022 by S780821@Github, < https://github.com/S780821 >.
#
# This file is part of < https://github.com/S780821/Rock-Music-V2 > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/S780821/Rock-Music-V2/blob/xmarty/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Rockz import LOGGER, app, userbot
from Rockz.core.call import Rock
from Rockz.plugins import ALL_MODULES
from Rockz.utils.database import get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("RockBot").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Rockz.plugins" + all_module)
    LOGGER("Rockz.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Rock.start()
    try:
        await RockBot.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Rockz").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Rock.decorators()
    LOGGER("Rockz").info("🥌 Rock Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Rockz").info("Stopping 🥌 Rock Music Bot! GoodBye")
