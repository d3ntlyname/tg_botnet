from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random

id = 1556864374
bot1 = Client("bot1", '6379199', '856b127610166f52be190bc9ba5b922b')

@bot1.on_message(filters.command("raid", prefixes="_") & filters.id)
def spam(self, msg):
 text = msg.text.split('_raid ', maxsplit=1)[1]
 for _ in range(100):
  msg.reply(text)
  sleep(1)

bot1.run()
