import lenguages
import questions
import telebot
from telebot import types

TOKEN = "5714586839:AAFLVZs--x0lS-QzFjS6zhJcH9O4zKi0R0A"
TEACHER_CHAT_ID = 425301144

bot = telebot.TeleBot(TOKEN)

chats = {}

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
    chats.update({test_id: questions.Test()})
    # current_test = chats[test_id]


@bot.message_handler(content_types=["text"])
def lets_go(massage):
    if massage.chat.type == "private":
        if massage.text in ["Українська", "English"]:
            chats[massage.chat.id].restart()
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

        if massage.text == chats[massage.chat.id].right_answer:
            chats[massage.chat.id].count_right_answers += 1

        elif massage.text == lenguages.TextLanguage.button_get_result:
            chats[massage.chat.id].get_level(chats[massage.chat.id].count_right_answers)
            bot.send_message(
                massage.chat.id,
                f"{lenguages.TextLanguage.result} - {chats[massage.chat.id].user_level}",
            )
            bot.send_message(TEACHER_CHAT_ID, f"@{massage.from_user.username} - {chats[massage.chat.id].user_level}")

        if chats[massage.chat.id].question_counter < chats[massage.chat.id].questions_left:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("A")
            button2 = types.KeyboardButton("B")
            button3 = types.KeyboardButton("C")
            button4 = types.KeyboardButton("D")
            button5 = types.KeyboardButton(lenguages.TextLanguage.button_i_dont_know)
            markup.add(button1, button2, button3, button4, button5)
            bot.send_message(
                massage.chat.id,
                chats[massage.chat.id].current_question,
                reply_markup=markup,
            )

            if chats[massage.chat.id].question_counter < chats[massage.chat.id].questions_left - 1:
                chats[massage.chat.id].change_counter()
                chats[massage.chat.id].change_right_answer()

            elif chats[massage.chat.id].counter_for_answers < chats[massage.chat.id].questions_left - 1:
                chats[massage.chat.id].change_right_answer()

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


bot.polling(none_stop=True)
