from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


bot1 = Client("bot1", '6379199', '856b127610166f52be190bc9ba5b922b')

@bot1.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 text = message.text.split('_raid ', maxsplit=1)[1]
 for _ in range(100):
  msg.reply(text)
  sleep(1)

bot1.run()
