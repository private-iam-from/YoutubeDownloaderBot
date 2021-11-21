from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Request", url="https://t.me/TAMILROCKERS_REQUEST"), InlineKeyboardButton("Creator", url="https://telegram.me/OO7ROBot") ],
        [InlineKeyboardButton(
            "⚡ DEV ⚡", url="@Robert_Pattinson119")]
    ])
    welcomed = f"""Hey <b>{message.from_user.first_name}</b>\nA Simple YouTube Downloader Bot that can:
  ➠ Download YouTube videos
  ➠ Download audio from YouTube videos \n\n Made with ♥️ by @Robert_Pattinson119"""
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
