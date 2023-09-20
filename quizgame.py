import random
questions = [
    {
        'question': 'Who served as the 14th President of India',
        'choices': ['a) Pranab Mukherjee', 'b) Ram Nath Kovind', 'c) Pratibha Patil', 'd) Droupadi Murmu'],
        'correct_answer': 'a) Pranab Mukherjee'
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'choices': ['Mars', 'Earth', 'Jupiter', 'Venus'],
        'correct_answer': 'Jupiter'
    },
    {
        'question': 'Who wrote "Romeo and Juliet"?',
        'choices': ['Charles Dickens', 'William Shakespeare', 'Mark Twain', 'Jane Austen'],
        'correct_answer': 'William Shakespeare'
    },
    {
        'question': 'The chemical symbol for gold is?',
        'choices': ['Go', 'Au', 'Ag', 'Ge'],
        'correct_answer': 'Au'
    },
    {
        'question': 'What is 9 x 7?',
        'correct_answer': '63'
    }
]

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice and fill-in-the-blank questions.")
    print("Let's get started!\n")

def ask_question(question_data):
    question = question_data['question']
    choices = question_data.get('choices')
    correct_answer = question_data.get('correct_answer')

    print(question)

    if choices:
        for i, choice in enumerate(choices, start=1):
            print(f"{i}. {choice}")

        user_answer = input("Enter the number of your choice: ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(choices):
            user_answer = choices[int(user_answer) - 1]
        else:
            user_answer = None
    else:
        user_answer = input("Your answer: ")

    return user_answer, correct_answer

def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}\n")
        return False

def play_quiz():
    score = 0
    total_questions = len(questions)
    random.shuffle(questions)

    display_welcome_message()

    for question_data in questions:
        user_answer, correct_answer = ask_question(question_data)
        if evaluate_answer(user_answer, correct_answer):
            score += 1

    print(f"You answered {score}/{total_questions} questions correctly.")
    if score == total_questions:
        print("Congratulations! You got a perfect score!\n")
    else:
        print("Keep practicing and try again!\n")

if __name__ == "__main__":
    while True:
        play_quiz()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye.")
            break