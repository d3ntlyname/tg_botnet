from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random
from datetime import datetime

app = Client("app", '3591508', '04da780758f80e6127ff1d757e9dba3b')

@app.on_message(filters.command("ping", prefixes=".") & filters.me)
def ping(self, message):
 message.edit('<b>Измеряю...</b>')
 ping_msg = []
 ping_data = []
 for _ in range(5):
  start = datetime.now()
  msg = app.send_message(777000, '¿')
  end = datetime.now()
  duration = (end - start).microseconds / 1000
  ping_data.append(duration)
  ping_msg.append(msg)
 ping = sum(ping_data) / len(ping_data)
 message.edit(f"<b>Пинг: {str(ping)[0:5]} мс</b>")
 for msg in ping_msg:
  msg.delete()

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(self, message):
 args = message.text.split(".type ", maxsplit=1)[1]
 orig = args
 space = ""
 typing = "|"
 while space != args:
  text = space + typing
  message.edit(str(text))
  sleep(0.20)
  space = space + args[0]
  args = args[1:]
  message.edit(str(space))
  sleep(0.20)
 message.edit(f"{orig[:len(orig)-1]}")
 
@app.on_message(filters.command("tik", prefixes=".") & filters.me)
def tik(self, message):
  args = message.text.split('.tik ', maxsplit=1)[1]
 if not args:
  message.edit('<b>Нету аргументов.</b>')
  return
 message.edit('<b>Загрузка...</b>')
 r = app.inline_query('tikdobot', args)
 app.send_file(message.chat.id, r[1].result.content.url)
 message.delete()

app.run()
