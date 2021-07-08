from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


app = Client("app", '3591508', '04da780758f80e6127ff1d757e9dba3b')

@app.on_message(filters.command("ping", prefixes="."))
def ping(self, message):
 message.edit('Понг!')

app.run()