#one.py
import telebot
from telebot import types

bot = telebot.TeleBot('6832822787:AAGaPrI_CiOLbI6HmDUjs-LOl4yjheMXVCk')

@bot.message_handler(commands=['start'])
def start(message):
bot.send_message(message.chat.id, 'Чтобы начать игру, напишите /game')

@bot.message_handler(commands=['help'])
def main(message):
bot.send_message(message.chat.id, 'Если хотите сыграть, напишите /game')

@bot.message_handler(commands=['game'])
def game(message):
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
i1=types.KeyboardButton('мультфильмы')
i2=types.KeyboardButton('фильмы')
markup.add(i1, i2)
bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
if message.text == 'фильмы':
def ot15(message):
if (message.text.lower() == 'пираты карибского моря'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Пираты Карибского моря')
bot.send_message(message.chat.id, 'Игра пройдена!')

def ot14(message):
if (message.text.lower() == 'тор') :
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Тор')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U00002620 \U0001F30A \U000026F5 \U0001F9AA \U000026AB"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot15)

def ot13(message):
if (message.text.lower() == 'хатико'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Хатико')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F528 \U000026A1"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot14)

def ot12(message):
if (message.text.lower() == 'гарри поттер') or (message.text.lower() == 'гари потер') or (message.text.lower() == 'гарри потер') or (message.text.lower() == 'гари поттер'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Гарри Поттер')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F686 \U0001F415"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot13)

def ot11(message):
if (message.text.lower() == 'капитан америка') or (message.text.lower() == 'первый мститель') :
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Капитан Америка')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F9D1 \U0001F453 \U000026A1 \U0001FA84"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot12)

def ot10(message):
if (message.text.lower() == 'сумерки') :
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Сумерки ')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F6E1 \U0001F4AA \U0001F1FA\U0001F1F8"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot11)

def ot9(message):
if (message.text.lower() == 'гарфилд') or (message.text.lower() == 'garfield'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Гарфилд')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F9DB \U00002764 \U0001F469 "
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot10)

def ot8(message):
if (message.text.lower() == 'планета обезьян'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Планета обезьян')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F431 \U0001F4A4"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot9)

def ot7(message):
if (message.text.lower() == 'трансформеры'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Трансформеры')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F30E \U0001F412 \U0001F412 \U0001F412"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot8)

def ot6(message):
if (message.text.lower() == 'оно'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Оно')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F916 \U00002194 \U0001F697"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot7)

def ot5(message):
if (message.text.lower() == 'титаник'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Титаник')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F921 \U0001F388 \U0001F631"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot6)

def ot4(message):
if (message.text.lower() == 'маска') :
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Маска')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F6E5 \U0001F9CA"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot5)

def ot3(message):
if (message.text.lower() == 'бэтмэн') or (message.text.lower() == 'бетмэн') or (message.text.lower() == 'batman') or (message.text.lower() == 'бэтмен') or (message.text.lower() == 'бетмен'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Бэтмэн')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F3AD \U0001F935"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot4)

def ot2(message):
if (message.text.lower() == 'призрачный гонщик') :
bot.send_message(message.chat.id, 'Верно')
else :
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Призрачный гонщик ')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F935 \U0001F987"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot3)

def ot1(message):
txt = message.text
if (message.text.lower() == 'один дома') :
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Один дома')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F525 \U0001F480 \U0001F3CD"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot2)

text = "\U0001F471 \U0001F3E0 \U0001F631"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot1)

if message.text == 'мультфильмы':
def ot15(message):
if (message.text.lower() == 'покемон') or (message.text.lower() == 'покемоны'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Покемоны')
bot.send_message(message.chat.id, 'Игра пройдена!')

def ot14(message):
if (message.text.lower() == 'тайна коко'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Тайна Коко')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F52E \U0001F38A \U0001F431 \U000026A1"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot15)

def ot13(message):
if (message.text.lower() == 'красавица и чудовище'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Красавица и чудовище')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F9D1 \U0001FA95 \U0001FA98 \U0001FA87 \U0001F480"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot14)

def ot12(message):
if (message.text.lower() == 'рататуй'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Рататуй')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F479 \U0001F339 \U0001F478"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot13)

def ot11(message):
if (message.text.lower() == '101 далматинец') or (message.text.lower() == 'сто один далматинец'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: 101 далматинец')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F400 \U0001F373"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot12)

def ot10(message):
if (message.text.lower() == 'том и джери') or (message.text.lower() == 'том и джерри') :
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Том и Джерри')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F436 \U00002B1B \U00002B1C"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot11)

def ot9(message):
if (message.text.lower() == 'труп невесты'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Труп невесты')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F63C \U0001F19A \U0001F42D"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot10)

def ot8(message):
if (message.text.lower() == 'зверополис'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Зверополис')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F470 \U0001F480"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot9)

def ot7(message):
if (message.text.lower() == 'наруто'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Наруто')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F98A \U0001F454 \U0001F430 \U0001F693 "
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot8)

def ot6(message):
if (message.text.lower() == 'приручить дракона') or (message.text.lower() == 'как приручить дракона'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Как приручить даркона')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F343 \U0001F365 \U0001F35C"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot7)

def ot5(message):
if (message.text.lower() == 'кот в сапогах'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Кот в сапогах')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F9D1 \U0001F44B \U0001F432"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot6)

def ot4(message):
if (message.text.lower() == 'король лев') :
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Король Лев')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F431 \U0001F462"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot5)

def ot3(message):
if (message.text.lower() == 'унесенная призраками') or (message.text.lower() == 'унесеная призраками') or (message.text.lower() == 'унесённая призраками') or (message.text.lower() == 'унесёная призраками'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Унесенная призраками ')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F981 \U0001F451"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot4)

def ot2(message):
if (message.text.lower() == 'вверх') or
(message.text.lower() == 'up'):
bot.send_message(message.chat.id, 'Верно')
else :
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Вверх')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U0001F467 \U0001F4A8 \U0001F47B \U0001F46B \U00002194 \U0001F437"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot3)

def ot1(message):
txt = message.text
if (message.text.lower() == 'скубиду') or (message.text.lower() == 'скуби-ду') or (message.text.lower() == 'скуби ду'):
bot.send_message(message.chat.id, 'Верно')
else:
bot.send_message(message.chat.id, 'Неверно. Правильный ответ: Скуби-ду ')
bot.send_message(message.chat.id, 'Далее: ')
text = "\U00002B06 \U0001F3DA \U0001F388 "
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot2)

text = "\U0001F436 \U0001F47B \U0001F631"
bot.send_message(message.chat.id, text=text)
bot.register_next_step_handler(message, ot1)

bot.polling(none_stop=True)
