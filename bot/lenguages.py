greeting_start_ukr = "Привіт, "
greeting_end_ukr = "Я бот зі школи англійської мови CTRLSHIFT і " "я допоможу тобі визначити твій рівень англійської"
greeting_start_eng = "Hello, "
greeting_end_eng = "I am a bot from CTRLSHIFT English school and I'll help you define your level"

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
start_eng = "Pres /start to repeat"

question_result_ukr = "Отримати результат?"
result_ukr = "Твій результат"
start_ukr = "Натисни /start щоб спробувати ще раз"


class TextLanguage:
    language = "English"
    greeting_start = greeting_start_eng
    greeting_end = greeting_end_eng
    button_lets_go = button1_eng
    button_next = button2_eng
    button_i_dont_know = button3_eng
    button_get_result = button4_eng
    question_result = question_result_eng
    result = result_eng
    start = start_eng

    @classmethod
    def choose_language(cls, user_lang):
        cls.language = user_lang
        if cls.language == "Українська":
            cls.greeting_start = greeting_start_ukr
            cls.greeting_end = greeting_end_ukr
            cls.button_lets_go = button1_ukr
            cls.button_next = button2_ukr
            cls.button_i_dont_know = button3_ukr
            cls.button_get_result = button4_ukr
            cls.question_result = question_result_ukr
            cls.result = result_ukr
            cls.start = start_ukr
        elif cls.language == "English":
            cls.greeting_start = greeting_start_eng
            cls.greeting_end = greeting_end_eng
            cls.button_lets_go = button1_eng
            cls.button_next = button2_eng
            cls.button_i_dont_know = button3_eng
            cls.button_get_result = button4_eng
            cls.question_result = question_result_eng
            cls.result = result_eng
            cls.start = start_eng
