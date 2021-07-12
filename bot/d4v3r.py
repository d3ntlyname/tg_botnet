import os, io, sys, time, requests, random; from datetime import datetime
os.system('clear'); run = 0; dethree = requests.get('https://github.com/Dethree/Files/raw/main/Logo.txt').text; print(dethree); cfg = os.path.exists('config.ini')
rep = os.path.exists('rep.txt')
if rep == False:
    with open("rep.txt", "w+") as f:
        rep = 0; repo = str(rep); f.write(repo); f.close()
        
if cfg == False:
	with open('config.ini', 'w+') as cfg:
		api = requests.get('https://github.com/Dethree/Files/raw/main/Token.ini').text; api = str(api); run = 1; cfg.write(api); cfg.close()
if run == 1:
	 requirements = ['pyrogram', 'asyncio', 'tgcrypto', 'translate', 'wikipedia', 'covid', 'gtts']; print('Установка зависимостей...')
	 for requirements in requirements:
	 	os.system(f'python3 -m pip install {requirements}')
elif run == 0:
	print('Подключение к Telegram...')
import asyncio, wikipedia; from covid import Covid; from translate import Translator; from pyrogram.types import InlineKeyboardMarkup,  InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ChatPermissions, Message,pyrogram; from pyrogram.errors import FloodWait, RPCError; from pyrogram import Client as client; from pyrogram import filters; app = client('dethree')
with app:
	app.join_chat('dethreebot'); os.system('clear'); print(dethree); print(f'Dethree-Telegram успешно запущен.\nНапишите .help в Телеграме, чтобы продолжить.'); global afk, cafk; afk = 0; cafk = []
				
@app.on_message(filters.command('help', prefixes='.') & filters.me)
async def help(client, message):
	help = requests.get('https://github.com/Dethree/Files/raw/main/Help.txt').text
	await message.edit(help, disable_web_page_preview=1)
	
@app.on_message(filters.command('ping', prefixes='.') & filters.me)
async def ping(client, message):
	await message.edit('<i>Измеряем...</i>')
	msgs = []
	data = []
	for _ in range(5):
		start = datetime.now()
		msg = await app.send_message(777000, '¿ƃuod')
		end = datetime.now()
		dur = (end - start).microseconds / 1000
		data.append(dur)
		msgs.append(msg)
	ping = sum(data) / len(data)
	await message.edit(f'<b>Понг > {str(ping)[0:5]} мс</b>')
	for msg in msgs:
		await msg.delete()

@app.on_message(filters.command('spam', prefixes='.') & filters.me)
async def spam(client, message):
	if not message.text.split('.spam', maxsplit=1)[1]:
		await message.edit('<i>Нету аргументов.</i>')
		return
	count = message.command[1]
	text = ' '.join(message.command[2:])
	count = int(count)
	await message.delete()
	for _ in range(count):
		await app.send_message(message.chat.id, text)
		await asyncio.sleep(0.2)
		
@app.on_message(filters.command('del', prefixes='.') & filters.me)
async def delete(client, message):
	if message.reply_to_message:
		msg_id = message.reply_to_message.message_id
		await message.delete()
		await client.delete_messages(message.chat.id, msg_id)
	else:
		await message.edit('<i>А где реплай?</i>')
		
@app.on_message(filters.command('purge', prefixes='.') & filters.me)
async def purge(client, message):
	if message.reply_to_message:
		r = message.reply_to_message.message_id
		m = message.message_id
		msgs = []
		await message.delete()
		v = m - r
		while r != m:
			msgs.append(int(r))
			r += 1
		await client.delete_messages(message.chat.id, msgs)
		r = message.reply_to_message.message_id
		msgs = []
		while r != m:
			msgs.append(int(r))
			r += 1
		await client.delete_messages(message.chat.id, msgs)
		await app.send_message(message.chat.id, f'<b>Удалено > {v} сообщений!</b>')
	else:
			await message.edit('<i>А где реплай?</i>')
			
@app.on_message(filters.private & ~filters.me)
async def afkread(client, message):
	global start, end, afk, reason, cafk
	nm = 0
	for _ in cafk:
		nm = 1
	if afk == 1 and nm == 0:
		end = datetime.now().replace(microsecond=0)
		afk_time = (end - start)
		await app.send_message(f'<b>Я сейчас в AFK (уже {afk_time})</b>\n{reason}', reply_to_message_id=message.message_id)
		cafk.append(message.chat.id)
	else:
		pass
			
@app.on_message(filters.command('afk', prefixes='.') & filters.me)
async def afk(client, message):
	global start, end, afk, reason
	afk = 1
	start = datetime.now().replace(microsecond=0)
	if len(message.text.split()) >= 2:
		reason = "<b>Причина:</b> <i>" + message.text.split(' ', maxsplit=1)[1] + "</i>"
	else:
		reason = ' '
	await message.edit('<b>Я теперь в AFK</b>')
	
@app.on_message(filters.command('unafk', prefixes='.') & filters.me)
async def unafk(client, message):
	global start, end, afk, reason, cafk
	afk = 0; cafk = []
	reason = ' '
	await message.edit('<b>Я теперь не в AFK</b>')
	
@app.on_message(filters.command('type', prefixes='.') & filters.me)
async def type(client, message):
	text = message.text.split('.type', maxsplit=1)[1]
	space = ''
	orig = text
	if not text:
		await message.edit('<i>Нету аргументов.</i>')
		return
	for typing in text:
		space += typing
		if typing not in [' ', '\n']:
			await message.edit(space+"|")
			await asyncio.sleep(0.3)
	await message.edit(orig)
			
@app.on_message(filters.command('hide', prefixes='.') & filters.me)
async def hide(client, message):
	args = message.text.split('.hide', maxsplit=1)[1]
	if not args:
		await message.edit('<i>Нету аргументов.</i>')
		return
	count = len(args)
	r = 1
	args = args.replace(' ', '_'); args = args[1:]
	while r != count:
		args = args[:len(args)-1]
		await message.edit(args)
		r += 1
		time.sleep(0.2)
	await message.delete()
		#
@app.on_message(filters.command(['trnsl', 'трнсл'], '.') & filters.me)
async def switch(client, message):
    text = ' '.join(message.command[1:])
    ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,"""
    en_keys = """eicykengшщzh_fiwaproldgeiчsmit_bu.E"№;%:?ICYKENGШЩZH_FIWAPROLDGEIЧSMIT_BU,"""
    if text == '':
        if message.reply_to_message:
            reply_text = message.reply_to_message.text
            change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
            reply_text = str.translate(reply_text, change)
            await message.edit(reply_text)
        else:
            await message.edit('<i>Нету аргументов.</i>')
    else:
        change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
        text = str.translate(text, change)
        await message.edit(text)
        
@app.on_message(filters.command('clap', prefixes='.') & filters.me)
async def clap(client, message):
	if len(message.text.split()) >= 2:
		args = message.text.split('.clap', maxsplit=1)[1]
		args += ' '
		args = args.replace(' ', ' 👏 '); args = args.replace('.', '')
		await message.edit(args)
	else:
		if message.reply_to_message:
			args = message.reply_to_message.text
			args = ' ' + args + ' '
			args = args.replace(' ', ' 👏 '); args = args.replace('.', '')
			await message.edit(args)
		else:
			await message.edit('<i>Нету аргументов.</i>')
			
@app.on_message(filters.command('shout', prefixes='.') & filters.me)
async def shout(client, message):
	if len(message.text.split()) >= 2:
		text = message.text.split('.shout ', maxsplit=1)[1]
		v = 0; r = ''; i = ''
		while v != len(text):
			sh = text[v:v+1]; v += 1; sh = r + sh; r += '\u0020'; sh += '\n'; i += sh
		await message.edit(i)
	else:
		if message.reply_to_message:
			text = message.reply_to_message.text
			v = 0; r = ''; i = ''
			while v != len(text):
				sh = text[v:v+1]; v += 1; sh = r + sh; r += '\u0020'; sh += '\n'; i += sh
			await message.edit(i)
		else:
			await message.edit('<i>Нету аргументов.</i>')
			
@app.on_message(filters.command("tagall", prefixes=".") & filters.me)
async def tagall(client, message):
    args = ''
    if len(message.text.split()) >= 2:
        args = message.text.split('.tagall ', maxsplit=1)[1]
        args = args + '\n\n'
    await message.delete()
    chat_id = message.chat.id
    string = ""
    limit = 1
    members = client.iter_chat_members(chat_id)
    async for member in members:
        tag = member.user.username
        if limit <= 5:
            list = ['😀', '👿', '🧐', '😳', '🤑', '🤖', '🎃', '😎', '🙂', '😡', '🙄', '😓', '🌝', '🤗', '🥺', '😋', '🍬', '👤', '⚡', '✌🏻', '🥶', '🥵', '😯', '😖', '👏', '🐯', '🌹', '🤸', '🌈', '🌴', '🍁', '🦇', '💋', '🤐', '🤧', '👺', '🧁', '🐏', '🦄', '🚧', '🐲', '🍉', '🥝', '🍺']
            if tag != None:
                w = random.choice(list)
                string += f"<a href='https://t.me/{tag}'>{w}</a> "
            else:
                w = random.choice(list)
                string += f"<a href='tg://user?id={member.user.id}'>{w}</a> "
            limit += 1
        else:
            await client.send_message(chat_id, text=f"{args}{string}", disable_web_page_preview=1)
            limit = 1
            string = ""
            await asyncio.sleep(2)
            
@app.on_message(filters.command("wiki", prefixes=".") & filters.me)
async def wiki(client, message):
    lang = message.command[1]
    user_request = ' '.join(message.command[2:])
    if user_request == '':
        wikipedia.set_lang("ru")
        user_request = ' '.join(message.command[1:])
    try:
        if lang == 'en':
            wikipedia.set_lang("en")

        result = wikipedia.summary(user_request)
        await message.edit(f'''<b>Запрос:</b>
<code>{user_request}</code>

<b>Значение:</b>
<code>{result}</code>''')
    except Exception as exc:
        await message.edit(f'''<b>Request:</b>
<code>{user_request}</code>

<b>Result:</b>
<code>{exc}</code>''')

@app.on_message(filters.command("covid", prefixes=".") & filters.me)
async def covid(client, message):
    region = ' '.join(message.command[1:])
    await message.edit('<i>Загрузка...</i>')
    covid = Covid(source="worldometers")
    try:
        local_status = covid.get_status_by_country_name(region)
        regio = local_status['country'] if local_status['country'] == 0 else 'Россия'
        await message.edit(f"<b>Страна</b>:\n<code>{regio}</code>\n" +
                           f"<b>Новые заражения</b>:\n<code>{local_status['new_cases']}</code>\n" +
                           f"<b>Новые смерти</b>:\n<code>{local_status['new_deaths']}</code>\n" +
                           f"<b>Подтверждённые</b>:\n<code>{local_status['confirmed']}</code>\n" +
                           f"<b>Зараженные:</b>\n<code>{local_status['active']}</code>\n" +
                           f"<b>Критически</b>:\n<code>{local_status['critical']}</code>\n" +
                           f"<b>Смертей</b>:\n<code>{local_status['deaths']}</code>\n" +
                           f"<b>Спасенно</b>:\n<code>{local_status['recovered']}</code>\n")
    except ValueError:
        await message.edit(f'<i>Нету страны с названием > "{region}"</i>')
				
@app.on_message(filters.command('toru', prefixes='.') & filters.me)
async def enru(self, message):
	trans = Translator(to_lang="Russian")
	if len(message.text.split()) >= 2:
		t = trans.translate(message.text.split('.toru ', maxsplit=1)[1])
		await message.edit(t)
	else:
		if message.reply_to_message:
			t = trans.translate(message.reply_to_message.text)
			await message.edit(t)
		else:
			await message.edit('<i>Нету аргументов.</i>')
				
@app.on_message(filters.command("pin", prefixes=".") & filters.me & ~filters.private)
async def pin(client, message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        message_id = message.reply_to_message.message_id
        await client.pin_chat_message(message.chat.id, message_id)
        await message.edit('<b>Закреплено успешно!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')

@app.on_message(filters.command("unpin", prefixes=".") & filters.me & ~filters.private)
async def pin(client, message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        message_id = message.reply_to_message.message_id
        await client.unpin_chat_message(message.chat.id, message_id)
        await message.edit('<b>Откреплено успешно!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')

@app.on_message(filters.command("ban", prefixes=".") & filters.me & ~filters.private)
async def ban(client, message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        reply = message.reply_to_message
        await app.kick_chat_member(message.chat.id, reply.from_user.id)
        await message.edit(f'<b><a href="tg://user?id={reply.from_user.id}">{reply.from_user.first_name}</a> забанен!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')
        
@app.on_message(filters.command("kick", prefixes=".") & filters.me & ~filters.private)
async def kick(client, message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        reply = message.reply_to_message
        await app.kick_chat_member(message.chat.id, reply.from_user.id)
        await app.unban_chat_member(message.chat.id, reply.from_user.id)
        await message.edit(f'<b><a href="tg://user?id={reply.from_user.id}">{reply.from_user.first_name}</a> кикнут!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')
        
@app.on_message(filters.command("mute", prefixes=".") & filters.me & ~filters.private)
async def mute(client, message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        reply = message.reply_to_message
        await app.restrict_chat_member(message.chat.id, reply.from_user.id, ChatPermissions(can_send_messages=False)) 
        await message.edit(f'<b><a href="tg://user?id={reply.from_user.id}">{reply.from_user.first_name}</a> замучен!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')
        
@app.on_message(filters.command("unmute", prefixes=".") & filters.me & ~filters.private)
async def unmute(client, message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        reply = message.reply_to_message
        await app.restrict_chat_member(message.chat.id, reply.from_user.id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_polls=True, can_send_other_messages=True, can_add_web_page_previews=True, can_change_info=False, can_invite_users=True, can_pin_messages=False)) 
        await message.edit(f'<b><a href="tg://user?id={reply.from_user.id}">{reply.from_user.first_name}</a> размучен!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')
        
@app.on_message(filters.command("unban", prefixes=".") & filters.me & ~filters.private)
async def unban(client, message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        reply = message.reply_to_message
        await app.restrict_chat_member(message.chat.id, reply.from_user.id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_polls=True, can_send_other_messages=True, can_add_web_page_previews=True, can_change_info=False, can_invite_users=True, can_pin_messages=False)) 
        await message.edit(f'<b><a href="tg://user?id={reply.from_user.id}">{reply.from_user.first_name}</a> разбанен!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')

@app.on_message(filters.command('vapor', prefixes='.') & filters.me)
async def vapor(client, message):
	if len(message.text.split()) >= 2:
		args = message.text.split('.vapor ', maxsplit=1)[1]
		args = args.replace(' ', '  '); args = args.replace('', ' ')
		await message.edit(f'<b>{args}</b>')
	else:
		if message.reply_to_message:
			args = message.reply_to_message.text
			args = args.replace(' ', '  '); args = args.replace('', ' ')
			await message.edit(f'<b>{args}</b>')
		else:
			await message.edit('<i>Нету аргументов.</i>')

@app.on_message(filters.command('logout', prefixes='.') & filters.me)
async def logout(self, message):
	await message.edit('<b>Dethree-Telegram успешно выключен!</b>')
	await asyncio.sleep(0.6)
	os.system('exit;exit')
	
@app.on_message(filters.text & filters.incoming & filters.regex('^\-$') & filters.reply)
async def rep(client, message):
    if message.reply_to_message.from_user.is_self:
        with open("rep.txt", "r+") as f:
            data = f.read(); data = int(data); rep = data - 1; repo = str(rep); f.close()
        with open("rep.txt", "w+") as f:
            repo = str(rep); f.write(repo); f.close(); text = "<b>Ты понизил мою репутацию :(</b>\n<b>Теперь моя репутация > " + str(repo) + '</b>'
            await message.reply_text(text)

@app.on_message(filters.text & filters.incoming & filters.regex('^\+$') & filters.reply)
async def rep(client, message):
    if message.reply_to_message.from_user.is_self:
        with open("rep.txt", "r+") as f:
            data = f.read(); data = int(data); rep = data + 1; repo = str(rep); f.close()
        with open("rep.txt", "w+") as f:
            repo = str(rep); f.write(repo); f.close(); text = "<b>Ты повысию мою репутацию :)</b>\n<b>Теперь моя репутация > " + str(repo) + '</b>'
            await message.reply_text(text)

@app.on_message(filters.command('clrep', prefixes='.') & filters.me)
async def clrep(client, message):
	with open('rep.txt', 'w+') as f:
		e = 0; f.write(str(e)); f.close()
		await message.edit('<b>Моя репутация > успешно очищена!</b>')
		
@app.on_message(filters.command('myrep', prefixes='.') & filters.me)
async def myrep(client, message):
	with open('rep.txt', 'r+') as f:
		data = f.read(); f.close()
		await message.edit(f'<b>Моя репутация > {data}</b>')
	
@app.on_message(filters.command('exec', '.') & filters.me)
def exec(client, message):
    code = ''
    try:
        code = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        try:
            code = message.text.split(" \n", maxsplit=1)[1]
        except IndexError:
            pass

    result = sys.stdout = io.StringIO()
    try:
        exec(code)

        pass
    except:
        message.edit(f"<i>exec:</i>\n<b>Не удалось выполнить выражение:</b>\n"
                           f"<code>{code}</code>\n\n"
                           f"<b>Ошибка:</b>\n"
                           f"<code>{sys.exc_info()[0].__name__}: {sys.exc_info()[1]}</code>")
                           
@app.on_message(filters.command('eval', '.') & filters.me)
def eval(client, message):
    code = ''
    try:
        code = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        try:
            code = message.text.split(" \n", maxsplit=1)[1]
        except IndexError:
            pass

    result = sys.stdout = io.StringIO()
    try:
        exec(code)

        message.edit(f"<i>eval:</i>\n<b>Выполненное выражение:</b>\n"
                           f"<code>{code}</code>\n\n"
                           f"<b>Возвращено</b>:\n"
                           f"<code>{result.getvalue()}</code>")
    except:
        message.edit(f"<i>eval:</i>\n<b>Не удалось выполнить выражение:</b>\n"
                           f"<code>{code}</code>\n\n"
                           f"<b>Ошибка:</b>\n"
                           f"<code>{sys.exc_info()[0].__name__}: {sys.exc_info()[1]}</code>")

from gtts import gTTS
from io import BytesIO


@app.on_message(filters.command('tts', '.') & filters.me)
async def tts(client, message):
    lang = 'ru'
    text = ' '.join(message.command[1:])
    await message.edit('<i>Загрузка...</i>')
    tts = gTTS(text, lang=lang)
    voice = BytesIO()
    tts.write_to_fp(voice)
    voice.name = 'voice.ogg'
    await message.delete()
    if message.reply_to_message:
        await client.send_audio(message.chat.id, voice, reply_to_message_id=message.reply_to_message.message_id)
    else:
        await client.send_audio(message.chat.id, voice)

def get_pic(city):
    file_name = f'{city}.png'
    with open(file_name, 'wb') as pic:
        response = requests.get(f'http://wttr.in/{citys}_2&lang=en.png', stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            pic.write(block)
        return file_name

@app.on_message(filters.command('aw', '.') & filters.me)
async def weather(client, message):
    if len(message.text.split()) < 2:
    	await message.edit('<i>Нету аргументов.</i>')
    	return
    city = message.command[1]
    await message.edit("<i>Загрузка...</i>")
    r = requests.get('https://wttr.in/{}?m?M?0?q?T&lang=en'.format(city))
    await message.edit(f"<b>Погода:</b>\n      Город: {r.text}")
    await client.send_document(chat_id=message.chat.id, document=get_pic(city), reply_to_message_id=message.message_id)
    os.remove(f'{city}.png')

@app.on_message(filters.command('webshot', ".") & filters.me)
async def webshot(client, message):
    try:
        if len(message.text.split()) < 2:
        	await message.edit('<i>Нету аргументов.</i>')
        	return
        user_link = message.command[1]
        await message.delete()
        full_link = f'https://webshot.deam.io/{user_link}/?delay=2000'
        await client.send_document(message.chat.id, full_link, caption=f'{user_link}')
    except:
        await message.edit('<i>Неизвестный сайт.</i>')
        
app.run()
