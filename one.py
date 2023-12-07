#one.py
import telebot

bot = telebot.TeleBot('6832822787:AAGaPrI_CiOLbI6HmDUjs-LOl4yjheMXVCk')

@bot.message_handler(commands=['start'])
def main(message):
	bot.send_message(message.chat.id, 'Привет')

bot.polling(none_stop=True)
