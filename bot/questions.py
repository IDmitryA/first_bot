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
        {"7. ___ 20 people in this room.\n\nA. This is\n" "B. There is"
         "\nC. They are\nD. There are": "D"},
        {"8. Sorry, I can't speak. I ___ right now.\n\nA. driving\n" "B. drive\n"
         "C. 'm driving\nD. drives": "C"},
        {"9. I speak Spanish, but Lisa ___ .\n\nA. don't speaks\nB. doesn't\nC. not speaks\n"
         "D. not speak": "B"},
        {"10. She ___ at work last week.\n\nA. didn't be\nB. wasn't\nC. weren't\nD. isn't": "B"},
        {"11. - ___ do you go to the gym? - Twice a week. .\n\nA. How often\nB. Why\nC. How\n"
         "D. How many": "A"},
        {"12. I like ___ before bedtime.\n\nA. read\nB. to reading\nC. am reading\nD. reading": "D"},
        {"13. I ___ when I was 4 years old.\n\nA. can swim\nB. could swim\nC. could to swim\n"
         "D. can't swim": "B"},
        {"14. They ___ in the office when suddenly there was a blackout.\n\nA. worked\n"
         "B. was working\nC. are working\nD. were working": "D"},
        {"15. ___ this guy before? .\n\nA. Did you ever seen\nB. Are you ever see\n"
         "C. Have you ever seen\nD. Do you ever see": "C"},
        {"16. I went to the bookshop ___ 'Harry Potter'.\n\nA. for buy\nB. to buy\nC. to buying\n"
         "D. for to buy": "B"},
        {"17. We will stay at home if it ___ tomorrow. .\n\nA. rains\nB. will rain\n"
         "C. raining\nD. is rain": "A"},
        {"18. Mike plays football ___ than me.\n\nA. more good\nB. more better\nC. best\nD. better": "D"},
        {"19. He doesn't smoke now  but he ___ much 20 years ago.\n\nA. used to smoke\nB. was smoking\n"
         "C. has smoked\nD. was smoked": "A"},
        {"20. He passed his English evaluation very ___.\n\nA. easy\nB. easier\nC. good\nD. easily": "D"},
        {"21. I can't stand ___ in a stuffy office.\n\nA.  to work\nB. working\nC. work\n"
         "D. to working": "B"},
        {"22. Let's go somewhere else. There's ___ noise in this room.\n\nA. too many\nB. too much\n"
         "C. enough\nD. too": "B"},
        {"23. It's going to be  a very long day. I won't get home ___ 9 pm.\n\nA. since\nB. to\n"
         "C. towards\nD. until": "D"},
        {"24. They usually ___ at home but today they ___ lunch in a restaurant.\n\nA. are eating, have\n"
         "B. eat, have\nC. eat, are having\nD. are eating, are having": "C"},
        {"25.  I think most people ___ English for their jobs in the future.\n\nA. need\nB. are needing\n"
         "C. will need\nD. will needed": "C"},
        {"26. I have received 20 messages from him ______.\n\nA. yesterday\nB. on Friday\nC. this week\n"
         "D. two days ago": "C"}
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
        if right_answers < 15:
            self.user_level = "A1 - Elementary"
        elif 15 <= right_answers < 30:
            self.user_level = "A2 - Pre-Intermediate"
        elif 30 <= right_answers < 45:
            self.user_level = "B1 - Intermediate"
        elif 45 <= right_answers < 50:
            self.user_level = "B2 - Upper-Intermediate"
        elif right_answers >= 50:
            self.user_level = "C1 - Advanced"
