TOKEN  = '718885403:AAFmKX2Qv44au92cZ1Y0n5k-oxpnjr4qioE'
URL = f'https://api.telegram.org/bot{token}/'

import telebot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
