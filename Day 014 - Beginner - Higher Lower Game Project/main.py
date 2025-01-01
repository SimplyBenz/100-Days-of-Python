import random
from art import logo, vs
from game_data import data

NumDataItem = len(data)
Selected_Already = []
Opponent01 = random.randint(0, len(data) - 1)
Opponent02 = random.randint(0, len(data) - 1)

while Opponent01 == Opponent02:
    Opponent02 = random.randint(0, len(data) - 1)

def choose_component(FirstChoice,SecondChoice):

    SecondChoice  = random.randint(0, len(data) - 1)

    for i in Selected_Already:
        if FirstChoice == i or SecondChoice == i:
            choose_component(FirstChoice,SecondChoice)

    Selected_Already.append(FirstChoice)
    Selected_Already.append(SecondChoice)

    game_on(A=FirstChoice, B=SecondChoice)

def game_on(A,B):
    print(logo)
    print(f"Name: {data[A]['name']}")
    print(f"Follower Count: {data[A]['follower_count']}")
    print(f"Description: {data[A]['description']}")
    print(f"Country: {data[A]['country']}")
    print(vs)
    print(f"Name: {data[B]['name']}")
    print(f"Follower Count: {data[B]['follower_count']}")
    print(f"Description: {data[B]['description']}")
    print(f"Country: {data[B]['country']}")

    print(len(Selected_Already))
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if player_choice == 'A':

        if data[A]['follower_count'] > data[B]['follower_count']:
            print("You are right!")
            A = B
        else:
            print("You are wrong!")
            return
    elif player_choice == 'B':
        if data[A]['follower_count'] < data[B]['follower_count']:
            print("You are right!")
            A = B
        else:
            print("You are wrong!")
            return

    print(A)
    print(B)

    choose_component(A,B) #FIXME: Fix the bug that the function is not returning to the function after the player has made a choice

choose_component(FirstChoice = Opponent01,SecondChoice = Opponent02)