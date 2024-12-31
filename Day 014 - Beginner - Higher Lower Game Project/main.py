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
            choose_component()

    Selected_Already.append(FirstChoice)
    Selected_Already.append(SecondChoice)

    game_on(FirstChoice, SecondChoice)

def game_on(FirstChoice, SecondChoice):
    print(logo)
    print(f"Name: {data[FirstChoice]['name']}")
    print(f"Follower Count: {data[FirstChoice]['follower_count']}")
    print(f"Description: {data[FirstChoice]['description']}")
    print(f"Country: {data[FirstChoice]['country']}")
    print(vs)
    print(f"Name: {data[SecondChoice]['name']}")
    print(f"Follower Count: {data[SecondChoice]['follower_count']}")
    print(f"Description: {data[SecondChoice]['description']}")
    print(f"Country: {data[SecondChoice]['country']}")

    print(len(Selected_Already))
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if player_choice == 'A':

        if data[FirstChoice]['follower_count'] > data[SecondChoice]['follower_count']:
            print("You are right!")
            FirstChoice = SecondChoice
        else:
            print("You are wrong!")
            return
    elif player_choice == 'B':
        if data[FirstChoice]['follower_count'] < data[SecondChoice]['follower_count']:
            print("You are right!")
            FirstChoice = SecondChoice
        else:
            print("You are wrong!")
            return

    print(FirstChoice)
    print(SecondChoice)

    choose_component(FirstChoice,SecondChoice)

choose_component(FirstChoice = Opponent01,SecondChoice = Opponent02)