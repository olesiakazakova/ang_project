#one.py
import telebot
from telebot import types

bot = telebot.TeleBot('6832822787:AAGaPrI_CiOLbI6HmDUjs-LOl4yjheMXVCk')

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, '')
	bot.send_message(message.chat.id, '')

@bot.message_handler(commands=['play'])
def play(message):

@bot.message_handler()
def priv(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
	elif message.text.lower() != 'привет':
		bot.send_message(message.chat.id, 'Прости, я не понимаю. Напиши /help')

bot.polling(none_stop=True) 
