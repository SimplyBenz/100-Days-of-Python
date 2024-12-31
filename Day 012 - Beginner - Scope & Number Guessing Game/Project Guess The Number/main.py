import art
import random
# from random import randint
# from art import logo

level = ""
attempt = 0
selected_number = 0
correct_number = 0

def game_on(selected, correct, tryin):

    if tryin > 0 and selected == correct:
        print(f"Yes!! the number is {correct}. You win")
    elif tryin > 0 and selected < correct:
        print("Too low.")
        print("Guess again.")
        print(f"You have {tryin} attempts remaining to guess the number.")
        selected = int(input("Guess number :"))
        tryin -= 1
        game_on(selected, correct, tryin)
    elif tryin > 0 and selected > correct:
        print("Too High.")
        print("Guess again.")
        print(f"You have {tryin} attempts remaining to guess the number.")
        tryin -= 1
        selected = int(input("Guess number :"))
        game_on(selected, correct, tryin)
    elif tryin <=0:
        print("You Loose")
        print(f"You have {tryin} attempts and the correct number is {correct}")


correct_number = int(random.randint(1, 100))

print (art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(f"pssss... the collect number is {correct_number}")
level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

if level == "easy":
    attempt = 10
elif level == "hard":
    attempt = 5

selected_number = int(input("Guess number :"))
attempt -= 1 # -1 attempt because player just guess it one time before function start
game_on(selected=selected_number,correct=correct_number,tryin=attempt)