import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

RPS_list = [rock, paper, scissors]

x = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))
if x == 0 or x == 1 or x == 2:
    print(RPS_list[x])
    print("Computer chose:")

    y = random.randint(0, 2)
    print(RPS_list[y])

    z = (x - y) % 3

    print(z)

    if z == 0:
        print("Draw")
    elif z == 1:
        print("You win")
    else:
        print("Computer win")
else:
    print("please select 0, 1 or 2.")