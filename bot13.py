from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


bot13 = Client("bot13", '3591508', '04da780758f80e6127ff1d757e9dba3b')

@bot13.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 for _ in range(100):
  msg.reply("ГРУППА ВЗЛОМАНА BY @DENTLY")
  sleep(1)

bot13.run()
