#one.py
import telebot
from telebot import types

bot = telebot.TeleBot('6832822787:AAGaPrI_CiOLbI6HmDUjs-LOl4yjheMXVCk')

@bot.message_handler(commands=['start'])
def start(message):
bot.send_message(message.chat.id, 'Привет! Чтобы начать игру напиши /game')

@bot.message_handler(commands=['help'])
def main(message):
bot.send_message(message.chat.id, 'Если хотите сыграть, напишите /game')

@bot.message_handler(commands=['game'])
def game(message):
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
i1=types.KeyboardButton('легкий')
i2=types.KeyboardButton('средний')
i3=types.KeyboardButton('сложный')
markup.add(i1, i2, i3)
bot.send_message(message.chat.id, 'Выберите уровень сложности', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
if message.text == 'легкий':
def ot10(message):
if (message.text.lower() == 'кот в сапогах') :
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Кот в сапогах')
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
i1 = types.KeyboardButton('средний')
i2 = types.KeyboardButton('сложный')
markup.add(i1, i2)
bot.send_message(message.chat.id, 'Хотите пройти другие уровни?', reply_markup=markup)


def ot9(message):
if (message.text.lower() == 'кунфу панда') or (message.text.lower() == 'кунгфу панда') or (message.text.lower() == 'кунг-фу панда') or (message.text.lower() == 'кун-фу панда'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Кунг-фу панда')
text = "Далее:\U0001F431 \U0001F462 "
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot10)

def ot8(message):
if (message.text.lower() == 'ледниковый период'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Ледниковый период')
text = "Далее:\U0001F44A \U0001F43C"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot9)

def ot7(message):
if (message.text.lower() == 'трансформеры'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Трансформеры')
text = "Далее:\U0001F330 \U0001F43F \U0001F9CA \U0001F30D"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot8)

def ot6(message):
if (message.text.lower() == 'оно'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Оно')
text = "Далее:\U0001F916 \U00002194 \U0001F697"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot7)

def ot5(message):
if (message.text.lower() == 'титаник'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Титаник')
text = "Далее:\U0001F921 \U0001F388 \U0001F631"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot6)

def ot4(message):
if (message.text.lower() == 'король лев') :
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Король Лев')
text = "Далее:\U0001F6E5 \U0001F9CA"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot5)

def ot3(message):
if (message.text.lower() == 'бэтмэн') or (message.text.lower() == 'бетмэн') or (message.text.lower() == 'batman') or (message.text.lower() == 'бэтмен') or (message.text.lower() == 'бетмен'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Бэтмэн')
text = "Далее:\U0001F981 \U0001F451"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot4)

def ot2(message):
if (message.text.lower() == 'вверх') or (message.text.lower() == 'up'):
bot.send_message(message.chat.id, 'Верно')
else :
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Вверх')
text = "Далее:\U0001F935 \U0001F987"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot3)

def ot1(message):
txt = message.text
if (message.text.lower() == 'золушка') or (message.text.lower() == 'cinderella'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Золушка')
text = "Далее:\U00002B06 \U0001F3DA \U0001F388 "
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot2)

text = "\U0001F460 \U0001F48E"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot1)

if message.text == 'средний':
bot.send_message(message.chat.id, 'пока еще нет')

if message.text == 'сложный':
bot.send_message(message.chat.id, 'пока еще нет')

@bot.message_handler()
def priv(message):
if (message.text.lower() == 'здравствуй') or (message.text.lower() == 'здравствуйте') or (message.text.lower() == 'привет') :
bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
else :
bot.send_message(message.chat.id, 'Простите, я вас не понимаю. Напишите /help')

bot.polling(none_stop=True)
