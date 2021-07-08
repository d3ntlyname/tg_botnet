from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


bot11 = Client("bot11", '2477268', 'f5fdf29f62907faf4e5934b0eabac1ea')

@bot11.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 for _ in range(100):
  msg.reply("ГРУППА ВЗЛОМАНА BY @DENTLY")
  sleep(1)

bot11.run()
