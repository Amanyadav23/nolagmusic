import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/CAADAQADzwIAAobwIEX9tbOxsFEmEgI.png",
        caption=f"""**๐๐ก๐ข๐ฌ ๐๐ฌ ๐๐๐ฏ๐๐ง๐๐ ๐ฅ๐๐๐ฅ๐๐ ๐ซ๐๐ฆ ๐๐ฎ๐ฌ๐ข๐ ๐ถ ๐๐จ๐ญ ๐๐ฎ๐ง ๐๐ง ๐๐ซ๐ข๐ฏ๐๐ญ๐ ๐ฅ ๐๐ฉ๐ฌ ๐ซ๐๐๐ซ๐ฏ๐๐ซ ๐ ๐๐๐๐ฅ โค๏ธ ๐๐ข๐ ๐ก ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐ง ๐๐ง ๐๐ ๐๐๐ฏ๐๐ฅ๐จ๐ฉ๐๐ ๐๐ฒ = [รเน4เนใปรMรรเนYรDรVเนรffรฎรงรฎร l](https://t.me/A_4_AMAN_OFFIICIAL)

๐๐ซ๐๐๐ญ๐จ๐ซ :- [รเน4เนใปรMรรเนYรDรVเนรffรฎรงรฎร l](https://t.me/A_4_AMAN_Offiicial)
๐๐๐๐ :- [๐๐๐๐๐](https://t.me/Vashu_baap)
๐๐ข๐ฌ๐๐ฎ๐ฌ๐ฌ :- (https://t.me/FUFYG7G7

๐๐ ๐๐จ๐ฎ ๐๐๐ฏ๐ ๐๐ง๐ฒ ๐๐ฎ๐๐ฌ๐ญ๐ข๐จ๐ง๐ฌ ๐๐ง๐ ๐๐๐ฅ๐ฉ ๐๐ก๐๐ง ๐๐ฆ ๐๐ฒ ๐๐จ๐ฌ๐ฌ = [รเน4เนใปรMรรเนYรDรVเนรffรฎรงรฎร l](https://t.me/A_4_AMAN_Offiicial)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ Jแดษชษด Hแดสแด & Sแดแดแดแดสแด โจ", url=f"https://t.me/FUFYG7G7")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/5f3af650e4c26e68287a8.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ Cสษชแดแด Mแด Tแด Gแดแด Rแดแดแด ๐", url=f"https://github.com/Amanyadav23/nolagmusic")
                ]
            ]
        ),
    )
