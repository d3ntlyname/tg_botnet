from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random

bot13 = Client("bot13", '6171271', '6484936aedda96ff8c6948834fbbb19e')

@bot13.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 text = msg.text.split('_raid ', maxsplit=1)[1]
 for _ in range(100):
  msg.reply(text)
  sleep(1)

bot13.run()
