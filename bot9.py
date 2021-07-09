from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random

id = 1556864374
bot9 = Client("bot9", '6155580', '11a402cde7b511da28a8e0e4326d545e')

@bot9.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 text = msg.text.split('_raid ', maxsplit=1)[1]
 for _ in range(100):
  msg.reply(text)
  sleep(1)

bot9.run()
