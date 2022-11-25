import lenguages
import questions
import telebot
from telebot import types

TOKEN = "5714586839:AAFLVZs--x0lS-QzFjS6zhJcH9O4zKi0R0A"
TEACHER_CHAT_ID = 425301144
CHATS = {"test_id": questions.Test()}

bot = telebot.TeleBot(TOKEN)

# удалять пройденый тест из словаря, попробовать chats сделать отребутом класса


@bot.message_handler(commands=["start"])
def start(massage):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Українська")
    button2 = types.KeyboardButton("English")
    markup.add(button1, button2)
    greeting = "Оберіть мову спілкування"
    bot.send_message(massage.chat.id, greeting, reply_markup=markup)
    test_id = massage.chat.id
    CHATS.update({test_id: questions.Test()})


@bot.message_handler(content_types=["text"])
def lets_go(massage):
    if massage.chat.type == "private" and massage.chat.id in CHATS:
        if massage.text in ["Українська", "English"]:
            CHATS[massage.chat.id].restart()
            if massage.text == "Українська":
                lenguages.TextLanguage.choose_language("Українська")
            elif massage.text == "English":
                lenguages.TextLanguage.choose_language("English")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton(lenguages.TextLanguage.button_lets_go)
            markup.add(button1)
            greeting = (
                f"{lenguages.TextLanguage.greeting_start}"
                f"{massage.from_user.first_name}. "
                f"{lenguages.TextLanguage.greeting_end}"
            )
            bot.send_message(massage.chat.id, greeting, reply_markup=markup)

        elif massage.text == lenguages.TextLanguage.button_lets_go:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("A")
            button2 = types.KeyboardButton("B")
            button3 = types.KeyboardButton("C")
            button4 = types.KeyboardButton("D")
            button5 = types.KeyboardButton(lenguages.TextLanguage.button_i_dont_know)
            markup.add(button1, button2, button3, button4, button5)

        if massage.text == CHATS[massage.chat.id].right_answer:
            CHATS[massage.chat.id].count_right_answers += 1

        elif massage.text == lenguages.TextLanguage.button_get_result:
            CHATS[massage.chat.id].get_level(CHATS[massage.chat.id].count_right_answers)
            bot.send_message(
                massage.chat.id,
                f"{lenguages.TextLanguage.result}: {CHATS[massage.chat.id].user_level}",
            )
            bot.send_message(TEACHER_CHAT_ID, f"@{massage.from_user.username} - {CHATS[massage.chat.id].user_level}")
            CHATS.pop(massage.chat.id)

        if massage.chat.id in CHATS:
            if CHATS[massage.chat.id].question_counter < CHATS[massage.chat.id].questions_left:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button1 = types.KeyboardButton("A")
                button2 = types.KeyboardButton("B")
                button3 = types.KeyboardButton("C")
                button4 = types.KeyboardButton("D")
                button5 = types.KeyboardButton(lenguages.TextLanguage.button_i_dont_know)
                markup.add(button1, button2, button3, button4, button5)
                bot.send_message(
                    massage.chat.id,
                    CHATS[massage.chat.id].current_question,
                    reply_markup=markup,
                )

                if CHATS[massage.chat.id].question_counter < CHATS[massage.chat.id].questions_left - 1:
                    CHATS[massage.chat.id].change_counter()
                    CHATS[massage.chat.id].change_right_answer()

                elif CHATS[massage.chat.id].counter_for_answers < CHATS[massage.chat.id].questions_left - 1:
                    CHATS[massage.chat.id].change_right_answer()

            else:
                if massage.text != lenguages.TextLanguage.button_get_result:
                    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button11 = types.KeyboardButton(lenguages.TextLanguage.button_get_result)
                    markup1.add(button11)
                    bot.send_message(
                        massage.chat.id,
                        lenguages.TextLanguage.question_result,
                        reply_markup=markup1,
                    )
        else:
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button11 = types.KeyboardButton("/start")
            markup1.add(button11)
            bot.send_message(massage.chat.id, lenguages.TextLanguage.start, reply_markup=markup1)

        print(CHATS)
        print(massage.from_user.id)


bot.polling(none_stop=True)
