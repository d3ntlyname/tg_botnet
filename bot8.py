from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random

id = 1556864374
bot8 = Client("bot8", '6166017', '47c5478bf994bd24505d08b7efd5a86a')

@bot8.on_message(filters.command("raid", prefixes="_") & filters.id)
def spam(self, msg):
 text = msg.text.split('_raid ', maxsplit=1)[1]
 for _ in range(100):
  msg.reply(text)
  sleep(1)

bot8.run()
