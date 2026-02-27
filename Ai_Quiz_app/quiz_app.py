# -----------------------------------------
# AI Technology Quiz App (Beginner Version)
# -----------------------------------------

# 1. Define quiz questions
questions = [
    {
        "question": "1. What does AI stand for?",
        "options": ["A. Automated Input", "B. Artificial Intelligence", "C. Auto Integration"],
        "answer": "b"
    },
    {
        "question": "2. Which of these is a type of machine learning?",
        "options": ["A. Supervised Learning", "B. Mechanical Learning", "C. Manual Learning"],
        "answer": "a"
    },
    {
        "question": "3. Which company created ChatGPT?",
        "options": ["A. Google", "B. Meta", "C. OpenAI"],
        "answer": "c"
    },
    {
        "question": "4. What is the brain of an AI model called?",
        "options": ["A. Neural Network", "B. Data Engine", "C. Logic Box"],
        "answer": "a"
    },
    {
        "question": "5. Which language is most used in AI development?",
        "options": ["A. Python", "B. C#", "C. HTML"],
        "answer": "a"
    },
    {
        "question": "6. What is NLP in AI?",
        "options": ["A. Natural Language Processing", "B. Neural Logic Program", "C. Numeric Learning Pattern"],
        "answer": "a"
    },
    {
        "question": "7. Which AI model is used for image generation?",
        "options": ["A. DALL·E", "B. Excel", "C. PowerPoint"],
        "answer": "a"
    },
    {
        "question": "8. What is training data?",
        "options": ["A. Data used to teach AI", "B. Data used for sports training", "C. Random numbers"],
        "answer": "a"
    },
    {
        "question": "9. Which of these is an AI assistant?",
        "options": ["A. Siri", "B. Windows Media Player", "C. Notepad"],
        "answer": "a"
    },
    {
        "question": "10. What is a chatbot?",
        "options": ["A. A robot that chats", "B. A program that simulates conversation", "C. A messaging app"],
        "answer": "b"
    }
]

# 2. Define participants
participants = ["Participant 1", "Participant 2", "Participant 3"]

# 3. Initialize scores
scores = {name: 0 for name in participants}

print("\nWelcome to the AI Technology Quiz!")
print("There are 10 questions. Type A, B, or C for each answer.\n")

# 4. Quiz loop
for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    print()

    # Ask each participant
    for p in participants:
        answer = input(f"{p}, enter your answer (A/B/C): ").lower()

        # Validate input
        while answer not in ("a", "b", "c"):
            answer = input("Invalid input. Please enter A, B, or C: ").lower()

        # Update score
        if answer == q["answer"]:
            scores[p] += 1

    print("-" * 40)

# 5. Display final results
print("\nFinal Results:")
print("==============")
for p, s in scores.items():
    print(f"{p}: {s} / {len(questions)}")

# 6. Announce winner(s)
max_score = max(scores.values())
winners = [p for p, s in scores.items() if s == max_score]

print("\nWinner:")
print("--------")
for w in winners:
    print(f"{w} with {max_score} points!")

#7.Save Results to file
with open("results.txt", "w") as f:
    for p, s in scores.items():
        f.write(f"{p}: {s}\n")
