from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


bot3 = Client("bot3", '6531400', 'c1b044b3cb11b14d79b4e0e2c11b5cc1')

@bot3.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 for _ in range(100):
  msg.reply("××× ВАС ЗАРЕЙДИЛ: @DENTLY ×××")
  sleep(1)

bot3.run()
