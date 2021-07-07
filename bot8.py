from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


bot8 = Client("bot8", '6166017', '47c5478bf994bd24505d08b7efd5a86a')

@bot8.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 for _ in range(100):
  msg.reply("РЕЙД ОТ @DENTLY ✌🏻")
  sleep(1)

bot8.run()
