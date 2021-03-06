"""
[summary]

[extended_summary]
"""

# region[Imports]

import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from rich import print as rprint, inspect as rinspect
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter, ImageOps, ImageEnhance, ImageFile, ImageColor, ImageStat, ImagePalette, ImageSequence, ImageMath, ImageCms, ImageWin, ImageShow, ImageMode, ImagePath
import gidlogger as glog
from antipetros_discordbot.init_userdata.user_data_setup import ParaStorageKeeper
# endregion [Imports]

# region [TODO]


# endregion [TODO]

# region [AppUserData]


# endregion [AppUserData]

# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion[Logging]

# region [Constants]

APPDATA = ParaStorageKeeper.get_appdata()
BASE_CONFIG = ParaStorageKeeper.get_config('base_config')
COGS_CONFIG = ParaStorageKeeper.get_config('cogs_config')
THIS_FILE_DIR = os.path.abspath(os.path.dirname(__file__))

# endregion[Constants]


def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)


def make_perfect_fontsize(font_file, text: str, image_width: int, image_height: int):
    padding_width = image_width // 10
    padding_height = image_height // 10
    font_size = 16
    font = ImageFont.truetype(font_file, font_size)
    text_size = get_text_dimensions(text, font)
    while text_size[0] <= (image_width - padding_width) and text_size[1] <= (image_height - padding_height):
        font_size += 1
        font = ImageFont.truetype(font_file, font_size)
        text_size = get_text_dimensions(text, font)
    log.debug(f"found perfect font size -> {font_size-1}")
    return ImageFont.truetype(font_file, font_size - 1)


def find_min_fontsize(font_file, text_lines: list, image_width: int, image_height: int):
    sizes = []
    for line in text_lines:
        padding_width = image_width // 10
        padding_height = image_height // 10
        font_size = 1
        font = ImageFont.truetype(font_file, font_size)
        text_size = get_text_dimensions(line, font)
        while text_size[0] <= (image_width - padding_width) and text_size[1] <= (image_height - padding_height):
            font_size += 1
            font = ImageFont.truetype(font_file, font_size)
            text_size = get_text_dimensions(line, font)
        log.debug(f"found perfect font size -> {font_size-1}")
        sizes.append(font_size - 1)
        font_size = 16
    return ImageFont.truetype(font_file, min(sizes))

# region[Main_Exec]


if __name__ == '__main__':
    pass

# endregion[Main_Exec]