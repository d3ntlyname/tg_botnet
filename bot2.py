from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


bot2 = Client("bot2", '5235407', '07423ead8b4192e7650b14bb532fa037')

@bot2.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 for _ in range(100):
  msg.reply("😡")
  sleep(1)

bot2.run()

