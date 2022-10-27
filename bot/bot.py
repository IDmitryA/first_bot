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
            if (
                questions.english_test.question_counter
                < questions.english_test.questions_left
            ):
                bot.send_message(
                    message.chat.id,
                    questions.english_test.current_question,
                    reply_markup=markup,
                )
            if (
                questions.english_test.question_counter
                < questions.english_test.questions_left - 1
            ):
                questions.english_test.change_counter()
                questions.english_test.change_right_answer()
            else:
                if (
                    questions.english_test.counter_for_answers
                    < questions.english_test.questions_left - 1
                ):
                    questions.english_test.change_right_answer()
                else:
                    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button11 = types.KeyboardButton("Get result")
                    markup1.add(button11)
                    bot.send_message(
                        message.chat.id,
                        "click 'Get result'", reply_markup=markup1
                    )
                    bot.register_next_step_handler(message, end_of_test)

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


def end_of_test(message):
    if message.text == "Get result":
        bot.send_message(message.chat.id, "Congrats")
        bot.send_message(
            message.chat.id,
            f"Your result - {questions.english_test.count_right_answers}",
        )


bot.polling(none_stop=True)
