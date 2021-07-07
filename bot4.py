from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


bot4 = Client("bot4", '5435853', '96d1fbc874681053e19ecd49897fac51')

@bot4.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 for _ in range(100):
  msg.reply("Рейд от: @dently")
  sleep(1)

bot4.run()
