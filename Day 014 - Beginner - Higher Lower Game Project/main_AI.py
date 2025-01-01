#This version I used a AI to handle the fixed opponent selection and the game logic 

import random
from art import logo, vs
from game_data import data

# Number of items in data
NumDataItem = len(data)
# List to track already selected opponents
Selected_Already = []


# Function to get a random opponent who hasn't been selected yet
def get_random_opponent(exclude=[]):
    while True:
        choice = random.randint(0, NumDataItem - 1)
        if choice not in exclude:
            return choice


# Function to handle the game logic
def game_on(A, B):
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

    # Print the count of selected opponents
    print(f"Selected opponents so far: {len(Selected_Already)}")

    # Get player's choice
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Determine if the player's choice is correct
    if player_choice == 'A':
        if data[A]['follower_count'] > data[B]['follower_count']:
            print("You are right!")
            return A  # Continue with A as the next opponent
        else:
            print("You are wrong!")
            return None  # Game ends
    elif player_choice == 'B':
        if data[B]['follower_count'] > data[A]['follower_count']:
            print("You are right!")
            return B  # Continue with B as the next opponent
        else:
            print("You are wrong!")
            return None  # Game ends
    else:
        print("Invalid input! Please type 'A' or 'B'.")
        return game_on(A, B)  # Retry on invalid input


# Main function to start the game
def choose_component(A, B):
    global Selected_Already
    while True:
        # Add selected opponents to the list
        Selected_Already.extend([A, B])

        # Play the game round
        winner = game_on(A, B)
        if winner is None:
            print("Game Over!")
            break  # End the game if the player is wrong

        # Get a new opponent who hasn't been selected yet
        A = winner
        B = get_random_opponent(exclude=Selected_Already)


# Initial setup for the game
Opponent01 = get_random_opponent()
Opponent02 = get_random_opponent(exclude=[Opponent01])

# Start the game
choose_component(Opponent01, Opponent02)
