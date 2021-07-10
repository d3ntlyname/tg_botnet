from os import system as terminal
terminal('clear')
dethree = '''╭━━━╮╱╱╭╮╭╮╱╱╱╱╱╱╱╱╱╱╱╭━━━━╮╱╭╮
╰╮╭╮┃╱╭╯╰┫┃╱╱╱╱╱╱╱╱╱╱╱┃╭╮╭╮┃╱┃┃
╱┃┃┃┣━┻╮╭┫╰━┳━┳━━┳━━╮╱╰╯┃┃┣┻━┫┃╭━━┳━━┳━┳━━┳╮╭╮
╱┃┃┃┃┃━┫┃┃╭╮┃╭┫┃━┫┃━╋━━╮┃┃┃┃━┫┃┃┃━┫╭╮┃╭┫╭╮┃╰╯┃
╭╯╰╯┃┃━┫╰┫┃┃┃┃┃┃━┫┃━╋━━╯┃┃┃┃━┫╰┫┃━┫╰╯┃┃┃╭╮┃┃┃┃
╰━━━┻━━┻━┻╯╰┻╯╰━━┻━━╯╱╱╱╰╯╰━━┻━┻━━┻━╮┣╯╰╯╰┻┻┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
Создатель: @Dently
Канал: @DethreeBot'''
print(f'{dethree}\n\nУстановка...')
req = ['pyrogram', 'tgcrypto', 'asyncio']
for req in req:
 terminal(f'pip3 install {req}')
import subprocess
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random
import asyncio
import requests 
from pyrogram.handlers import MessageHandler
from datetime import datetime

app = Client("tex", '6957164', '3a40466f38b1d3c5e951f6881e64c028')
with app:
 app.join_chat('dethreebot')
 terminal('clear')
 print(f'{dethree}\n\nDethree-Telegram успешно установлен.\nВведите .help в Telegram\'е, чтобы продолжить.\n\nОшибки [логи]:')
 global afk
 afk = 0

@app.on_message(filters.command("ping", prefixes=".") & filters.me)
def ping(self, message):
 message.edit('<i>Измеряю...</i>')
 ping_msg = []
 ping_data = []
 for _ in range(5):
  start = datetime.now()
  msg = app.send_message(777000, "<a href='https://t.me/dethreebot'>¿</a>")
  end = datetime.now()
  duration = (end - start).microseconds / 1000
  ping_data.append(duration)
  ping_msg.append(msg)
 ping = sum(ping_data) / len(ping_data)
 message.edit(f"<b>Пинг:</b> <code>{str(ping)[0:5]}</code> <b>мс</b>")
 for msg in ping_msg:
  msg.delete()

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(self, message):
 text = message.text.split('.type', maxsplit=1)[1]
 if not text:
  message.edit('<b>Нету аргументов.\nПример:</b> <code>.type <текст></code>')
  return
 space = ""
 orig = text
 for typing in text:
  space += typing
  if typing not in [" ", "\n"]:
   message.edit(space+"|")
   sleep(0.2)
 message.edit(orig)
  
@app.on_message(filters.command("help", prefixes=".") & filters.me)
def help(self, message):
 message.edit(f'''<b>Помощь <a href='https://t.me/dethreebot'>Dethree-Telegram</a></b>

<b>Доступные модули:</b>
➜ <b>Тестер:</b> <code>ping</code>
➜ <b>Печать:</b> <code>type</code>
➜ <b>АФК:</b> <code>afk</code>, <code>unafk</code>
➜ <b>Погода:</b> <code>aw</code>
➜ <b>Чистка:</b> <code>del</code>, <code>purge</code>
➜ <b>Спам:</b> <code>spam</code>''')

@app.on_message(filters.private & ~filters.me)
async def afkread(client, message):
 global start, end, reason, afk
 end = datetime.now().replace(microsecond=0)
 afk_time = (end - start)
 if afk == 1:
  await message.reply(f'<b>Я сейчас в AFK (уже {afk_time})</b>\n{reason}')
 else:
  pass

@app.on_message(filters.command("afk", prefixes=".") & filters.me)
async def afk(self, message):
 global start, end, afk, reason
 afk = 1
 start = datetime.now().replace(microsecond=0)
 if len(message.text.split()) >= 2:
  reason = "<b>Причина:</b> <i>" + message.text.split(' ', maxsplit=1)[1] + '</i>'
 else:
  reason = ' '
 await message.edit('<b>Я теперь в AFK</b>')

@app.on_message(filters.command('unafk', prefixes='.') & filters.me)
async def unafk(self, message):
 global start, afk, end, reason
 end = datetime.now().replace(microsecond=0)
 afk_time = end - start
 reason = ' '
 afk = 0
 await message.edit('<b>Я теперь не в AFK</b>')

@app.on_message(filters.command('aw', prefixes='.') & filters.me)
def aw(self, message):
 city = message.text.split('.aw', maxsplit=1)[1]
 if not city:
  message.edit('<b>Нету аргументов.\nПример:</b> <code>.aw <город></code>')
  return
 city = city.replace(' ', '')
 err = f""">>>    _  _    _  _  _        
>>>   | || |  / _ \| || |         
>>>   | || |_| | | | || |_         
>>>   |   _| |_| |   _|         
>>>      |_|  \_/   |_|       
>>>                          
>>>   404 НЕИЗВЕСТНОЕ МЕСТОПОЛОЖЕНИЕ: {city}"""
 message.edit('<i>Узнаю погоду...</i>')
 r = requests.get(f'https://wttr.in/{city}?0?q?T&lang=ru')
 if err == r.text:
  message.edit('<b>Неизвестный город.\nПример:</b> <code>.aw <город></code>')
  return
 message.edit(f"""**Погода:**
     `Город: {r.text}`""", parse_mode='markdown')
 terminal('clear')
 print(f'{dethree}\n\nDethree-Telegram успешно установлен.\nВведите .help в Telegram\'е, чтобы продолжить.\n\nОшибки [логи]:')

@app.on_message(filters.command('del', prefixes='.') & filters.me)
async def d3l(self, message):
 if message.reply_to_message:
  msg_id = message.reply_to_message.message_id
  await message.delete()
  await self.delete_messages(message.chat.id, msg_id)
 else:
  await message.edit('<b>Нету реплая.\nПример:</b> <code>.del <реплай></code>')

@app.on_message(filters.command('purge', '.') & filters.me)
async def purge(self, message):
 if message.reply_to_message:
  r = message.reply_to_message.message_id
  m = message.message_id
  await message.delete()
  while r != m:
   await self.delete_messages(message.chat.id, int(r))
   r += 1
  r = message.reply_to_message.message_id
  while r != m:
   await self.delete_messages(message.chat.id, int(r))
   r += 1
 else:
  await message.edit(f'<b>Нету реплая.\nПример:</b> <code>.purge <реплай></code>')
   
@app.on_message(filters.command('spam', prefixes='.') & filters.me)
async def spam(self, message):
 arg = ' '.join(message.command[2])
 if not arg:
  message.edit('<b>Нету аргументов.\nПример:</b> <code>.spam <кол-во> <текст></code>')
  return
 qua = message.command[1]
 spam_text = ' '.join(message.command[2:])
 qua = int(qua)
 await message.delete()
 for u in range(qua):
  msg = await app.send_message(message.chat.id, spam_text)
  await asyncio.sleep(0.30)

app.run()
