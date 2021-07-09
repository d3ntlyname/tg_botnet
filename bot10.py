from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


bot10 = Client("bot10", '6415285', '5c4914f4ac3351e5e64ddf0db6216abb')

@bot10.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 text = msg.text.split('_raid ', maxsplit=1)[1]
 for _ in range(100):
  msg.reply(text)
  sleep(1)

bot10.run()
