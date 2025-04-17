import requests
import random

# Send request
response = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple")

# Check if response is OK
if response.status_code != 200:
    print(f"Error: Could not fetch questions (Status Code: {response.status_code})")
    exit()

data = response.json()

# Check if questions are returned
if not data['results']:
    print("No questions returned. Try changing category or difficulty.")
    exit()

# Game starts
score = 0
print("🎮 Welcome to the Trivia Quiz Game! 🎮\n")

for question in data['results']:
    print(f"Question: {question['question']}")
    options = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(options)

    print("Options: ")
    for idx, option in enumerate(options, 1):
        print(f"{idx}) {option}")

    try:
        answer = int(input("\nChoose your answer (1-4): "))
        if options[answer - 1] == question['correct_answer']:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Oops! The correct answer was: {question['correct_answer']}")
    except (ValueError, IndexError):
        print("Invalid input. Skipping this question.")

    print()

print(f"Your score: {score}/{len(data['results'])}")
