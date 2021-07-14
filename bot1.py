from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random

bot1 = Client("bot1e", "6630105", "8508c1bcfdb0c54ccc610f29fc041d99")

@bot1.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 text = msg.text.split('_raid ', maxsplit=1)[1]
 for _ in range(100):
  msg.reply(text)
  sleep(1)

bot1.run()
