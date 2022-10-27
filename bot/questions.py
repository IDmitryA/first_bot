class Test:
    question_list = [
        {"1. I ___ from Canada.\n\nA. is\nB. are\nC. am\nD. to be": "C"},
        {
            "2. This is my friend. ___ name is Mike.\n\n"
            "A. Her\nB. His\nC. Our\nD. He's": "B"
        },
        {
            "3. Mike is ___.\n\nA. my sister's teammate\n"
            "B. teammate my sister\nC. my sister teammate\n"
            "D. my sister teammate's": "A"
        },
        {
            "4. -Are you fine?\n    - No, I ___.\n\nA. am colding\n"
            "B. am cold\nC. have cold\nD. was cold": "B"
        },
        {
            "5. -What do you do?\n    - __\n\nA. I am fine, thanks. And you?\n"
            "B. I am Mike.\nC. I am a project manager.\n"
            "D. Your new neighbor.": "C"
        },
        {
            "6. -Who are you?\n    - ___\n\nA. I am a project manager.\n"
            "B. I'm OK, thanks.\nC. I'm Mike, your new teammate.\n"
            "D. I'm American.": "C"
        },
        {
            "7. ___ 20 people in this room.\n\nA. This is\n"
            "B. There is\nC. They are\nD. There are": "D"
        },
        {
            "8. Sorry, I can't speak. I ___ right now.\n\nA. driving\n"
            "B. drive\nC. 'm driving\nD. drives": "C"
        },
    ]
    question_counter = 0
    count_right_answers = 0
    counter = 0
    counter_for_answers = -1
    questions_left = len(question_list)
    current_item = question_list[counter]
    current_question = list(current_item.keys())[0]
    item_for_r_answer = question_list[counter_for_answers]
    right_answer = list(item_for_r_answer.values())[0]

    @staticmethod
    def change_counter():
        Test.counter += 1
        Test.current_item = Test.question_list[Test.counter]
        Test.current_question = list(Test.current_item.keys())[0]

    @staticmethod
    def change_right_answer():
        Test.question_counter += 1
        Test.counter_for_answers += 1
        Test.item_for_r_answer = Test.question_list[Test.counter_for_answers]
        Test.right_answer = list(Test.item_for_r_answer.values())[0]


english_test = Test()
