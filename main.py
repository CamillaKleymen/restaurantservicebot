import telebot
from telebot import types

bot = telebot.TeleBot('6989967497:AAEdT16N26Gemg1bXQN8TpziPkQS7mPitYU')
my_chat_id = 631104511
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Меню")
    item2 = types.KeyboardButton("Часы работы")
    item3 = types.KeyboardButton("Обратная связь")
    item4 = types.KeyboardButton("Связаться с менеджером")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите опцию:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Меню":
        show_menu(message)
    elif message.text == "Часы работы":
        show_hours(message)
    elif message.text == "Обратная связь":
        request_feedback(message)
    elif message.text == "Связаться с менеджером":
        contact_manager(message)
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понял. Пожалуйста, выберите опцию из меню.")

def show_menu(message):
    markup = types.InlineKeyboardMarkup()
    dish1 = types.InlineKeyboardButton("Блюдо 1", callback_data='dish1')
    dish2 = types.InlineKeyboardButton("Блюдо 2", callback_data='dish2')
    dish3 = types.InlineKeyboardButton("Блюдо 3", callback_data='dish3')
    markup.add(dish1, dish2, dish3)
    bot.send_message(message.chat.id, "Выберите блюдо из меню:", reply_markup=markup)

def show_hours(message):
    bot.send_message(message.chat.id, "Мы работаем с 9 до 21 каждый день.")

def request_feedback(message):
    msg = bot.send_message(message.chat.id, "Пожалуйста, напишите ваш отзыв или предложение:")
    bot.register_next_step_handler(msg, feedback)

def feedback(message):
    bot.send_message(my_chat_id, f"Отзыв: {message.text}")
    bot.send_message(message.chat.id, "Спасибо за ваш отзыв!")

def contact_manager(message):
    bot.send_message(message.chat.id, "Для связи с менеджером позвоните по телефону: +1234567890 или напишите на email: manager@example.com")

if __name__ == '__main__':
    bot.infinity_polling()
