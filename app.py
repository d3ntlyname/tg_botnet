from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


app = Client("app", '3591508', '04da780758f80e6127ff1d757e9dba3b')

@app.on_message(filters.command("ping", prefixes=".") & filters.me)
def ping(self, message):
 ping_msg = []
 ping_data = []
 for _ in range(5):
  start = datetime.now()
  msg = await message.app.send_message('me', 'Понг!')
  end = datetime.now()
  duration = (end - start).microseconds / 1000
  ping_data.append(duration)
  ping_msg.append(msg)
 ping = sum(ping_data) / len(ping_data)
 await message.edit(f"""<b>Пинг: {str(ping)[0:5]} мс</b>""", parse_mode='html')
 for msg in ping_msg:
  await msg.delete()

app.run()
