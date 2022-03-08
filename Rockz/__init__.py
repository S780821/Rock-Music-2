#
# Copyright (C) 2021-2022 by S780821@Github, < https://github.com/S780821 >.
#
# This file is part of < https://github.com/S780821/Rock-Music-V2 > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/S780821/Rock-Music-V2/blob/xmarty/LICENSE >
#
# All rights reserved.

from Rockz.core.bot import YukkiBot
from Rockz.core.dir import dirr
from Rockz.core.git import git
from Rockz.core.userbot import Userbot
from Rockz.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = YukkiBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
