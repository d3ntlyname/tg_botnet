from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


bot12 = Client("bot12", '6738465', '3ef33ae76a74cf199cdc352e4a4bbd9d')

@bot12.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 for _ in range(100):
  msg.reply("ВАС ЗАРЕЙДИЛ @DENTLY 😋")
  sleep(1)

bot12.run()