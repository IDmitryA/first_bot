class Test:
    question_list = [
        {"1. I ___ from Canada.\n\nA. is\nB. are\nC. am\nD. to be": "C"},
        {"2. This is my friend. ___ name is Mike.\n\n" "A. Her\nB. His\nC. Our\nD. He's": "B"},
        {
            "3. Mike is ___.\n\nA. my sister's teammate\n"
            "B. teammate my sister\nC. my sister teammate\n"
            "D. my sister teammate's": "A"
        },
        {"4. -Are you fine?\n    - No, I ___.\n\nA. am colding\n" "B. am cold\nC. have cold\nD. was cold": "B"},
        {
            "5. -What do you do?\n    - ___\n\n"
            "A. I am fine, thanks. And you?\n"
            "B. I am Mike.\nC. I am a project manager.\n"
            "D. Your new neighbor.": "C"
        },
        {
            "6. -Who are you?\n    - ___\n\nA. I am a project manager.\n"
            "B. I'm OK, thanks.\nC. I'm Mike, your new teammate.\n"
            "D. I'm American.": "C"
        },
        {"7. ___ 20 people in this room.\n\nA. This is\n" "B. There is\nC. They are\nD. There are": "D"},
        {"8. Sorry, I can't speak. I ___ right now.\n\nA. driving\n" "B. drive\nC. 'm driving\nD. drives": "C"},
    ]
    question_counter = 0
    count_right_answers = 0
    counter = 0
    counter_for_answers = -1
    questions_left: int = len(question_list)  # number of questions
    current_item = question_list[counter]  # {question: answer} position
    current_question = list(current_item.keys())[0]
    item_for_r_answer = question_list[counter_for_answers]
    right_answer = list(item_for_r_answer.values())[0]
    user_level = "A1 - Elementary"

    def change_counter(self):
        self.counter += 1
        self.current_item = self.question_list[self.counter]
        self.current_question = list(self.current_item.keys())[0]

    def change_right_answer(self):
        self.question_counter += 1
        self.counter_for_answers += 1
        self.item_for_r_answer = self.question_list[self.counter_for_answers]
        self.right_answer = list(self.item_for_r_answer.values())[0]

    def restart(self):
        self.question_counter = 0
        self.count_right_answers = 0
        self.counter = 0
        self.counter_for_answers = -1
        self.questions_left: int = len(self.question_list)
        self.current_item = self.question_list[self.counter]
        self.current_question = list(self.current_item.keys())[0]
        self.item_for_r_answer = self.question_list[self.counter_for_answers]
        self.right_answer = list(self.item_for_r_answer.values())[0]
        self.user_level = "A1 - Elementary"

    def get_level(self, right_answers):
        if right_answers < 15:  # 15
            self.user_level = "A1 - Elementary"
        elif 15 <= right_answers < 30:
            self.user_level = "A2 - Pre-Intermediate"
        elif 30 <= right_answers < 45:
            self.user_level = "B1 - Intermediate"
        elif 45 <= right_answers < 50:
            self.user_level = "B2 - Upper-Intermediate"
        elif right_answers >= 50:
            self.user_level = "C1 - Advanced"
