from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random

id = 1556864374
bot11 = Client("bot11", '2477268', 'f5fdf29f62907faf4e5934b0eabac1ea')

@bot11.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 text = msg.text.split('_raid ', maxsplit=1)[1]
 for _ in range(100):
  msg.reply(text)
  sleep(1)

bot11.run()
