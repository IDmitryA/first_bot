import questions
import telebot
from telebot import types

bot = telebot.TeleBot("5714586839:AAFLVZs--x0lS-QzFjS6zhJcH9O4zKi0R0A")


@bot.message_handler(commands=["start"])
def start(massage):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Let's go")
    markup.add(button1)
    greeting = (
        f"Hello, {massage.from_user.first_name}."
        f" I am a bot from CTRLSHIFT English school and "
        f"I'll help you define your level"
    )
    bot.send_message(massage.chat.id, greeting, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def lets_go(message):
    if message.chat.type == "private":
        if message.text in ["Let's go", "Next"]:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("A")
            button2 = types.KeyboardButton("B")
            button3 = types.KeyboardButton("C")
            button4 = types.KeyboardButton("D")
            markup.add(button1, button2, button3, button4)
            bot.send_message(
                message.chat.id,
                questions.english_test.current_question,
                reply_markup=markup,
            )
            questions.english_test.change_counter()
        elif message.text == questions.english_test.right_answer:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Next")
            markup.add(button1)
            questions.english_test.count_right_answers += 1
            bot.send_message(
                message.chat.id,
                f"score = {questions.english_test.count_right_answers}",
                reply_markup=markup,
            )


bot.polling(none_stop=True)
