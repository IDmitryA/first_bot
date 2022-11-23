class Test:
    question_list = [
        {"1. I ___ from Canada.\n\n" "A. is\nB. are\nC. am\nD. to be": "C"},
        {"2. This is my friend. ___ name is Mike.\n\n" "A. Her\nB. His\nC. Our\nD. He's": "B"},
        {
            "3. Mike is ___.\n\n"
            "A. my sister's teammate\nB. teammate my sister\nC. my sister teammate\nD. my sister teammate's": "A"
        },
        {"4. -Are you fine?\n    - No, I ___.\n\n" "A. am colding\n" "B. am cold\nC. have cold\nD. was cold": "B"},
        {
            "5. -What do you do?\n    - ___\n\n"
            "A. I am fine, thanks. And you?\nB. I am Mike.\nC. I am a project manager.\nD. Your new neighbor.": "C"
        },
        {
            "6. -Who are you?\n    - ___\n\n"
            "A. I am a project manager.\nB. I'm OK, thanks.\nC. I'm Mike, your new teammate.\nD. I'm American.": "C"
        },
        {"7. ___ 20 people in this room.\n\n" "A. This is\n" "B. There is" "\nC. They are\nD. There are": "D"},
        {"8. Sorry, I can't speak. I ___ right now.\n\n" "A. driving\n" "B. drive\n" "C. 'm driving\nD. drives": "C"},
        {"9. I speak Spanish, but Lisa ___ .\n\n" "A. don't speaks\nB. doesn't\nC. not speaks\n" "D. not speak": "B"},
        {"10. She ___ at work last week.\n\n" "A. didn't be\nB. wasn't\nC. weren't\nD. isn't": "B"},
        {
            "11. - ___ do you go to the gym?\n    - Twice a week. .\n\n"
            "A. How often\nB. Why\nC. How\n"
            "D. How many": "A"
        },
        {"12. I like ___ before bedtime.\n\n" "A. read\nB. to reading\nC. am reading\nD. reading": "D"},
        {"13. I ___ when I was 4 years old.\n\n" "A. can swim\nB. could swim\nC. could to swim\n" "D. can't swim": "B"},
        {
            "14. They ___ in the office when suddenly there was a blackout.\n\n"
            "A. worked\nB. was working\nC. are working\nD. were working": "D"
        },
        {
            "15. ___ this guy before? .\n\n"
            "A. Did you ever seen\nB. Are you ever see\nC. Have you ever seen\nD. Do you ever see": "C"
        },
        {
            "16. I went to the bookshop ___ 'Harry Potter'.\n\n"
            "A. for buy\nB. to buy\nC. to buying\nD. for to buy": "B"
        },
        {"17. We will stay at home if it ___ tomorrow. .\n\n" "A. rains\nB. will rain\n" "C. raining\nD. is rain": "A"},
        {"18. Mike plays football ___ than me.\n\n" "A. more good\nB. more better\nC. best\nD. better": "D"},
        {
            "19. He doesn't smoke now  but he ___ much 20 years ago.\n\n"
            "A. used to smoke\nB. was smoking\nC. has smoked\nD. was smoked": "A"
        },
        {"20. He passed his English evaluation very ___.\n\n" "A. easy\nB. easier\nC. good\nD. easily": "D"},
        {"21. I can't stand ___ in a stuffy office.\n\n" "A.  to work\nB. working\nC. work\n" "D. to working": "B"},
        {
            "22. Let's go somewhere else. There's ___ noise in this room.\n\n"
            "A. too many\nB. too much\nC. enough\nD. too": "B"
        },
        {
            "23. It's going to be a very long day. I won't get home ___ 9 pm.\n\n"
            "A. since\nB. to\nC. towards\nD. until": "D"
        },
        {
            "24. They usually ___ at home but today they ___ lunch in a restaurant.\n\n"
            "A. are eating, have\nB. eat, have\nC. eat, are having\nD. are eating, are having": "C"
        },
        {
            "25.  I think most people ___ English for their jobs in the future.\n\n"
            "A. need\nB. are needing\nC. will need\nD. will needed": "C"
        },
        {
            "26. I have received 20 messages from him ___.\n\n"
            "A. yesterday\nB. on Friday\nC. this week\nD. two days ago": "C"
        },
        {
            "27. I ___ a zoom meeting when the phone ___. That's why I didn't pick up.\n\n"
            "A. had, rang\nB. was having, rang\nC. was having, was ringing\nD. had, has rung": "B"
        },
        {
            "28. You ___ spend any time fixing this issue, it has already been fixed.\n\n"
            "A. can't\nB. mustn't\nC. should\nD. don't have to": "D"
        },
        {
            "29. I haven't heard from Mike for ages. I wonder ___.\n\n"
            "A. how has he been\nB. how is he\nC. how does she\nD. how he is": "D"
        },
        {
            "30. If you don't want to burn out at work, you ___ work without rest days.\n\n"
            "A. won't\nB. don't\nC. shouldn't\nD. couldn't": "C"
        },
        {"31. If I have enough money next year, I ___ to the USA.\n\n" "A. will go\nB. go\nC. would go\nD. went": "A"},
        {
            "32. It's the best movie ___. You should go and see it.\n\n"
            "A. I ever saw\nB. I've already seen\nC. I've never seen\nD. I've ever seen": "D"
        },
        {
            "33. They went to Australia after my friend ___ me about its wonderful nature.\n\n"
            "A. was telling\nB. has told\nC. had told\nD. had been told": "C"
        },
        {
            "34. I always have my power bank with me ___ I need to charge my phone.\n\n"
            "A. however\nB. despite\nC. in case\nD. as": "C"
        },
        {
            "35. By the time we arrived, everyone ___ already..\n\n"
            "A. will have left\nB. left\nC. had left\nD. have left": "C"
        },
        {
            "36. I ___ be late for work this morning. I've got a lot to do before midday.\n\n"
            "A. don't have to\nB. couldn't\nC. don't\nD. mustn't": "D"
        },
        {"37. I ___ here for 2 years now.\n\n" "A. work\nB. am working\nC. have been working\nD. worked": "C"},
        {
            "38. A lot ___ to the house before we can move in.\n\n"
            "A. needs be doing\nB. needs done\nC. needs do\nD. needs to be done": "D"
        },
        {
            "39. You can't use my laptop, it ___ .\n\n"
            "A. is repaired\nB. is being repaired\nC. is repairing\nD. repairs": "B"
        },
        {
            "40. When he arrived, his fans ___ for ten hours to greet him.\n\n"
            "A. had been waiting\nB. were waiting\nC. have been waiting\nD. are waiting": "A"
        },
        {
            "41. My mobile phone ___. I need a new one.\n\n"
            "A. has been stolen\nB. has stolen\nC. have been stolen\nD. stole": "A"
        },
        {
            "42. I had a part time job in McDonald's when I ___ my diploma paper at the university.\n\n"
            "A. have been writing\nB. have been written\nC. had written\nD. was writing": "D"
        },
        {
            "43. Look at the pile of work I have today! It ___ a hard day.\n\n"
            "A. will be\nB. is going to be\nC. will\nD. might be": "B"
        },
        {"44. I think you ___ see a doctor.\n\n" "A. need\nB. would\nC. should\nD. have to": "C"},
        {"45. I am fed up ___ this task.\n\n" "A. to do\nB. to doing\nC. with doing\nD. for doing": "C"},
        {"46. If I were rich, I ___ a Ferrari.\n\n" "A. 'd drive\nB. 'll drive\nC. will be driving\nD. drive": "A"},
        {
            "47. If only he  ___ more time for his family. But he was always busy\n\n"
            "A. had had\nB. had\nC. has\nD. has had": "A"
        },
        {
            "48. ___ the better team, we lost the match.\n\n"
            "A. Despite being\nB. Despite of being\nC. Although\nD. Despite the fact": "A"
        },
        {
            "49. If they ___ next to each other on the plane, they wouldn't have made friends.\n\n"
            "A. hadn't sat\nB. had sat\nC. sat\nD. didn't sit": "A"
        },
        {
            "50. When I got home I realized that someone ___ the window.\n\n"
            "A. broke\nB. was broken\nC. had broken\nD. hadn't break": "C"
        },
        {"51. We'll need to have the house ___.\n\n" "A. renovating\nB. renovate\nC. renovated\nD. to renovate": "C"},
        {
            "52. At first I ___ starting work so early, but now I am OK with that.\n\n"
            "A. didn't use to\nB. wouldn't\nC. didn't have to\nD. wasn't used to": "D"
        },
        {
            "53. I can't find my keys, I ___ them.\n\n"
            "A. may lose\nB. might have lost\nC. should have lost\nD. must lost": "B"
        },
        {
            "54. He was made ___ a sweater with a snowman last Christmas.\n\n"
            "A. to wear\nB. wearing\nC. wear\nD. to wearing": "A"
        },
        {"55. I saw Mike ___ the room.\n\n" "A. left\nB. to leave\nC. to leaving\nD. leave": "D"},
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
