#Task 1: Develop a list of questions and answers.

import random

print("A quiz for Sir Lancelot of Camelot")
questions = ["What is your name?", "What is your quest?", "What is your favorite color?"]
answers = ["sir lancelot of camelot", "to seek the holy grail", "blue"]


#Task 2: Write a function that quizzes the user and takes their answers.

def quiz(question_list, answer_list):

    correct_answers = 0

    while len(question_list) > 0:
        q_index = question_list.index(random.choice(question_list))
        print(question_list[q_index])
        answer = input().lower()

        if answer == answer_list[q_index]:
            correct_answers += 1
        
        question_list.remove(question_list[q_index])
        answer_list.remove(answer_list[q_index])


#Task 3: Score the quiz and give the user feedback on their performance.

    if correct_answers == 0:
        print("No correct answers? You might just not be paying attention.")
    elif correct_answers == 1:
        print("1 correct answer. Honestly that was a freebie.")
    elif correct_answers == 2:
        print("2 correct asnwers, but you are still cast into the Gorge of Eternal Peril!")
    else:
        print("3 correct asnwers. Right, off you go")
            
quiz(questions, answers)