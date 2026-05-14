# Don't Remove Credit @SUPREME_BOTz
# Subscribe YouTube Channel For Amazing Bot @SUPREME_BOTz
# Ask Doubt on telegram @SUPREME_BOTz

from pyrogram import Client, filters
from info import CHANNELS
from database.ia_filterdb import save_file

media_filter = filters.document | filters.video

@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    media = getattr(message, message.media.value, None)
    media.caption = message.caption
    await save_file(media)
