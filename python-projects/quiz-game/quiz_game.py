print("===== Python Quiz Game =====")

questions = [
    {
        "question": "Which language is known as a programming language?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /* */", "C. #", "D. <!-- -->"],
        "answer": "C"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["A. print()", "B. output()", "C. display()", "D. show()"],
        "answer": "A"
    },
    {
        "question": "Which data type is used to store whole numbers?",
        "options": ["A. float", "B. string", "C. int", "D. boolean"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    }
]

score = 0

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n===== Quiz Finished =====")
print("Your Score:", score, "/", len(questions))