from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    START_TEXT = """
Hi {} 
I am Powerful Url Uploader Bot
 
"""

    HELP_TEXT = """
# Send me the Google Drive | ytdl | direct links.
# Select the desired option.
# Then be relaxed your file will be uploaded soon..
 
"""

# give credit to developer

    ABOUT_TEXT = """
<b>โป๏ธ My Name</b> : Url Uploader Bot
<b>๐ Channel</b> : <a href="https://t.me/TMWAD">@TMWAD</a>
<b>๐บ Heroku</b> : <a href="https://heroku.com/">Heroku</a>
<b>๐ Language :</b> <a href="https://www.python.org/">Python 3.10.5</a>
<b>๐ต๐ฒ Framework :</b> <a href="https://docs.pyrogram.org/">Pyrogram 2.0.30</a>
<b>๐ฒ Developer :</b> <a href="https://t.me/kinu6">@kinu6</a>
"""

    PROGRESS = """
๐ฐ Speed : {3}/s\n\n
๐ Done : {1}\n\n
๐ฅ Tแดแดแดส sษชแดขแด  : {2}\n\n
โณ Tษชแดแด สแดาแด : {4}\n\n
"""
    ID_TEXT = """
๐ Your Telegram ID ๐ข๐ฌ :- <code>{}</code>
"""

    INFO_TEXT = """
 ๐คน First Name : <b>{}</b>
 ๐ดโโ๏ธ Second Name : <b>{}</b>
 ๐ง๐ปโ๐ Username : <b>@{}</b>
 ๐ Telegram Id : <code>{}</code>
 ๐ Profile Link : <b>{}</b>
 ๐ก Dc : <b>{}</b>
 ๐ Language : <b>{}</b>
 ๐ฒ Status : <b>{}</b>
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('โ Help', callback_data='help'),
            InlineKeyboardButton('๐ฆ About', callback_data='about')
        ], [
            InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('๐  Home', callback_data='home'),
            InlineKeyboardButton('๐ฆ About', callback_data='about')
        ], [
            InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('๐  Home', callback_data='home'),
            InlineKeyboardButton('โ Help', callback_data='help')
        ], [
            InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = "Now Select the desired formats"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "Trying to Download โ\n\n <i>{} </i>"
    UPLOAD_START = "<i>{} </i>\n\n๐ค Uploading Please Wait "
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dแดแดกษดสแดแดแดแดแด ษชษด {} sแดแดแดษดแดs.\n\nTสแดษดแดs Fแดส Usษชษดษข Mแด\n\nUแดสแดแดแดแดแด ษชษด {} sแดแดแดษดแดs"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "โ Media cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
