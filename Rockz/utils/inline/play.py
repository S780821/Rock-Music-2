#
# Copyright (C) 2021-2022 by S780821@Github, < https://github.com/S780821 >.
#
# This file is part of < https://github.com/S780821/Rock-Music-V2 > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/S780821/Rock-Music-V2/blob/xmarty/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton


def track_markup(_, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v",
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
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text=_["PL_B_3"], switch_inline_query_current_chat=""
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
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_3"], switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"RockPlaylists {videoid}|{user_id}|{ptype}|a",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"RockPlaylists {videoid}|{user_id}|{ptype}|v",
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
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v",
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
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}",
            ),
        ],
    ]
    return buttons
