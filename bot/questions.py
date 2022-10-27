class Test:
    question_list = [
        {"What is your name?\nA. Oleg\nB. Kate\nC. Semen\nD. Bot": "D"},
        {"What is your last name?\nA. Kot\nB. Petrov\nC. BOT\nD. Vandam": "C"},
    ]

    count_right_answers = 0
    counter = 0
    counter_for_answers = -1
    questions_left = len(question_list)
    current_item = question_list[counter]
    current_question = list(current_item.keys())[0]
    item_for_right_answer = question_list[counter_for_answers]
    right_answer = list(item_for_right_answer.values())[0]

    @staticmethod
    def change_counter():
        Test.counter += 1
        Test.counter_for_answers += 1
        Test.current_item = Test.question_list[Test.counter]
        Test.current_question = list(Test.current_item.keys())[0]
        Test.item_for_right_answer = \
            Test.question_list[Test.counter_for_answers]
        Test.right_answer = list(Test.item_for_right_answer.values())[0]


english_test = Test()
