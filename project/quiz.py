# A Python Quiz Game Using API Requests..
# Requests module to make HTTP connections, Random to Shuffle Answers List, Time to simulate Realism, Math to Format Numbers
import math
import requests
import random
import time

# API URL
api_url = 'https://opentdb.com/api.php?amount=02'

# Fetch Questions From the URL and Convert to Python Objects..


def get_question():
    response = requests.get(api_url)
    data = response.json()
    results = data['results']
    return results


# State To Track Quiz in Memory..
correct_answer = 0
wrong_answer = 0
wild = 0
game_loop = True

# Get Player Details..
print("Quiz is Starting...")
player_name = input('Enter your Name: ')
print(f"Your Quiz is about to begin, Get set {player_name}")

# Print Answers List..


def print_list(list):
    for answer, index in enumerate(list):
        print(answer + 1, index)
        time.sleep(0.5)


# Run Game In a Loop
try:
    while game_loop:
        results = get_question()
        start_time = time.time()
        for i in results:
            # Prepare Quiz
            question = i['question']
            answer = i['correct_answer']
            incorrect_answers = i['incorrect_answers']
            incorrect_answers.append(answer)
            random.shuffle(incorrect_answers)

            # Start Quiz
            print(question)
            time.sleep(1)
            print_list(incorrect_answers)
            option = input(
                "Enter Your answer Either by Specifying the Index or Option's Value: ")
            if option.isdecimal():
                option = int(option)
                if incorrect_answers[option - 1] == answer:
                    correct_answer += 1
                else:
                    wrong_answer += 1
            else:
                if option.lower() == answer.lower():
                    correct_answer += 1
                else:
                    wrong_answer += 1
        if correct_answer > wrong_answer:
            print(f"You did a good Job! {player_name}")
            if correct_answer == len(results):
                print(
                    f"Genius, You really are the smartest alive {player_name}")
        elif correct_answer == wrong_answer:
            print(f"You did a Fair job {player_name}")
        else:
            print(f"You can do better {player_name}")
            if correct_answer == 0:
                print(f"If you Work Harder {player_name}")
        wild += 1

        end_time = time.time() - start_time
        print(f"You Spent {math.floor(end_time)} seconds on this Quiz")
        # Confirm If User Wants to play Again..
        decide = input(
            "Would You Like to play Again? Y for yes and any other key to break: ")

        # Evaluate Decision..
        if decide.lower() == 'y':
            continue
        else:
            game_loop = False
            break
except IndexError:
    print("You Entered Invalid Answer")

# Print Amount of Attemted Questions, Correct Answers and Wrong Answers..
if wild > 1:
    print(f"You Attempted {len(results)} Questions")
    print(f"You Got {correct_answer} Right and {wrong_answer} Wrong")
