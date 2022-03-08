# @xmartperson

import sys

from pyrogram import Client

import config

from ..logging import LOGGER


class RockBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Sᴛᴀʀᴛɪɴɢ Bᴏᴛ")
        super().__init__(
            "Rock-Music-2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "Bᴏᴛ Sᴛᴀʀᴛᴇᴅ"
            )
        except:
            LOGGER(__name__).error(
                "Bᴏᴛ ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ Gʀᴏᴜᴘ. Mᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀᴅᴍɪɴ!"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Pʟᴇᴀsᴇ ᴘʀᴏᴍᴏᴛᴇ Bᴏᴛ ᴀs Aᴅᴍɪɴ ɪɴ Lᴏɢɢᴇʀ Gʀᴏᴜᴘ"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MᴜsɪᴄBᴏᴛ Sᴛᴀʀᴛᴇᴅ ᴀs {self.name}")
