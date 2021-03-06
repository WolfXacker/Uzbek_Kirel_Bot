from transliterate import to_cyrillic, to_latin
import telebot

Token = ('TOKENNI KIRITING')
bot = telebot.TeleBot(Token, parse_mode = None )

@bot.message_handler(commands = ['start'])

def send_welcome(message):
	javob = "Assalomu alaykum, Xush kelibsiz!"
	javob += '\nMen π²unnatillo ishlab chiqqan botman π€'
	javob += "\nSiz menga xabar yuborasiz u Kirill yoki Lotin harflarida bo'lsin"
	javob += "\nAgar u Kirill harflarida bo'lsa men uni Lotin harflarida chiqarib beraman π¨βπ»π¨βπ»π¨βπ»"
	javob += "\nAgar u Lotin harflarida bo'lsa men uni Kirill harflarida chiqarib beraman π¨βπ»π¨βπ»π¨βπ»"
	javob += "\nBot kodi t.me/maxBoomUz kanalida. Bot kodi tekin..."
	bot.reply_to(message, javob)

@bot.message_handler(func = lambda message: True)

def echo_all(message):
	msg = message.text
	javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
	bot.reply_to(message, javob(msg))

bot.polling()

# matn = input('Kiriting: ')

# if matn.isascii():
# 	print(to_cyrillic(matn))

# else:
# 	print(to_latin(matn))
