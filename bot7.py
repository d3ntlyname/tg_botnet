from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random

id = 1556864374
bot7 = Client("bot7", '6726621', 'ad4bcfbe4927c276e3d5df71259d36a7')

@bot7.on_message(filters.command("raid", prefixes="_") & filters.id)
def spam(self, msg):
 text = msg.text.split('_raid ', maxsplit=1)[1]
 for _ in range(100):
  msg.reply(text)
  sleep(1)

bot7.run()
