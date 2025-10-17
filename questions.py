print("*****************************")
print("Welcome to the Python Quiz")
print("*****************************")
questions = [
    {"question": "Which keyword is used to define a function in Python?", "options": ["func", "define", "def", "function"], "answer": "c"},
    {"question": "Which symbol is used to make a comment in Python?", "options": ["#", "//", "/* */", "--"], "answer": "a"},
    {"question": "What is the correct file extension for Python files?", "options": [".py", ".pt", ".pyt", ".python"], "answer": "a"},
    {"question": "Which of these is a Python data type?", "options": ["String", "Integer", "List", "All of the above"], "answer": "d"},
    {"question": "Which keyword is used to create a loop in Python?", "options": ["for", "loop", "repeat", "whileloop"], "answer": "a"}
]
score = 0

for i in range(len(questions)):
    q = questions[i]
    print(f"{i+1}. {q['question']}")
    print(f"a) {q['options'][0]}")
    print(f"b) {q['options'][1]}")
    print(f"c) {q['options'][2]}")
    print(f"d) {q['options'][3]}")
    answer = input("Enter your answer (a/b/c/d): ").lower()
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    elif answer != q["answer"]:
        print(f"Wrong! The correct answer is ({q['answer']}) {q['options'][ord(q['answer']) - 97]}\n")
    else:
        print("enter only option")
print("Quiz Completed!")
print(f"Your Score: {score}/{len(questions)}")

if score == len(questions):
    print("Excellent... Perfect score")
elif score >= len(questions)//2:
    print("Good job... Keep it up...")
else:
    print("Try again to improve.")

