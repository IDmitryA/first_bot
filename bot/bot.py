import questions
import lenguages
import telebot
from telebot import types
import random

bot = telebot.TeleBot("5714586839:AAFLVZs--x0lS-QzFjS6zhJcH9O4zKi0R0A")


@bot.message_handler(commands=["start"])
def start(massage):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Українська")
    button2 = types.KeyboardButton("English")
    markup.add(button1, button2)
    greeting = f"Оберіть мову спілкування"
    bot.send_message(massage.chat.id, greeting, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def lets_go(massage):
    if massage.chat.type == "private":
        if massage.text in ["Українська", "English"]:
            questions.Test.restart()
            if massage.text == "Українська":
                lenguages.TextLanguage.choose_language("Українська")
            elif massage.text == "English":
                lenguages.TextLanguage.choose_language("English")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton(lenguages.TextLanguage.button1)
            markup.add(button1)
            greeting = f"{lenguages.TextLanguage.greeting_start}{massage.from_user.first_name}. {lenguages.TextLanguage.greeting_end}"
            bot.send_message(massage.chat.id, greeting, reply_markup=markup)
        elif massage.text in [lenguages.TextLanguage.button1, lenguages.TextLanguage.button2]:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("A")
            button2 = types.KeyboardButton("B")
            button3 = types.KeyboardButton("C")
            button4 = types.KeyboardButton("D")
            button5 = types.KeyboardButton(lenguages.TextLanguage.button3)
            markup.add(button1, button2, button3, button4, button5)
            if (
                questions.english_test.question_counter
                < questions.english_test.questions_left
            ):
                bot.send_message(
                    massage.chat.id,
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
                    button11 = types.KeyboardButton(lenguages.TextLanguage.button4)
                    markup1.add(button11)
                    bot.send_message(
                        massage.chat.id, lenguages.TextLanguage.question_result, reply_markup=markup1
                    )

                    bot.register_next_step_handler(massage, end_of_test)

        elif massage.text == questions.english_test.right_answer:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton(lenguages.TextLanguage.button2)
            markup.add(button1)
            questions.english_test.count_right_answers += 1
            bot.send_message(
                massage.chat.id,
                random.choice(lenguages.TextLanguage.msg),
                reply_markup=markup,
            )
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton(lenguages.TextLanguage.button2)
            markup.add(button1)
            bot.send_message(
                massage.chat.id,
                random.choice(lenguages.TextLanguage.msg),
                reply_markup=markup,
            )


def end_of_test(message):

    if message.text == lenguages.TextLanguage.button4:
        bot.send_message(
            message.chat.id,
            f"{lenguages.TextLanguage.result} - {questions.english_test.count_right_answers}",
        )


bot.polling(none_stop=True)
# сбросить каунтеры после завершения теста
