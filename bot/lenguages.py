import random


greeting_start_ukr = "Привіт, "
greeting_end_ukr = "Я бот зі школи англійської мови CTRLSHIFT і " \
                   "я допоможу тобі визначити твій рівень англійської"
greeting_start_eng = "Hello, "
greeting_end_eng = (
    ". I am a bot from CTRLSHIFT English school and "
    "I'll help you define your level"
)

msg_ukr = [
    "чудово, далі...",
    "молодець, так тримати...",
    "це було не складно, далі...",
    "ага, зрозумів...",
    "не поспішай, часу вдосталь...",
]
msg_eng = [
    "great, go on...",
    "it was esy)...",
    "ok, understood...",
    "ofcourse you can, come on...",
]

rand_msg_ukr = random.choice(msg_ukr)
rand_msg_eng = random.choice(msg_eng)

button1_eng = "Let's go"
button2_eng = "Next"
button3_eng = "I don't know, skip"
button4_eng = "Get result"

button1_ukr = "Почати"
button2_ukr = "Наступний"
button3_ukr = "Не знаю, пропустити"
button4_ukr = "Отримати результат"

question_result_eng = "Get result?"
result_eng = "Your result"

question_result_ukr = "Отримати результат?"
result_ukr = "Твій результат"


class TextLanguage:
    language = "English"
    msg = msg_eng
    greeting_start = greeting_start_eng
    greeting_end = greeting_end_eng
    button1 = button1_eng
    button2 = button2_eng
    button3 = button3_eng
    button4 = button4_eng
    question_result = question_result_eng
    result = result_eng

    @classmethod
    def choose_language(cls, user_lang):
        cls.language = user_lang
        if cls.language == "Українська":
            cls.msg = msg_ukr
            cls.greeting_start = greeting_start_ukr
            cls.greeting_end = greeting_end_ukr
            cls.button1 = button1_ukr
            cls.button2 = button2_ukr
            cls.button3 = button3_ukr
            cls.button4 = button4_ukr
            cls.question_result = question_result_ukr
            cls.result = result_ukr
        elif cls.language == "English":
            cls.msg = msg_eng
            cls.greeting_start = greeting_start_eng
            cls.greeting_end = greeting_end_eng
            cls.button1 = button1_eng
            cls.button2 = button2_eng
            cls.button3 = button3_eng
            cls.button4 = button4_eng
            cls.question_result = question_result_eng
            cls.result = result_eng
