# @xmartperson

from pyrogram.types import InlineKeyboardButton


def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
                InlineKeyboardButton("乂sᴜᴘᴘᴏʀᴛ乂", url=f"https://t.me/Rockerz_Updates"),
                InlineKeyboardButton(
                    "乂ᴄʜᴀɴɴᴇʟ乂", url=f"https://t.me/Rockerz_Updates"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons
