from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random

bot5 = Client("bot5", '6370484', 'edb81ce5f76cc0ba3e0aa81d69da777c')

@bot5.on_message(filters.command("raid", prefixes="_")
def spam(self, msg):
 text = msg.text.split('_raid ', maxsplit=1)[1]
 for _ in range(100):
  msg.reply(text)
  sleep(1)

bot5.run()
