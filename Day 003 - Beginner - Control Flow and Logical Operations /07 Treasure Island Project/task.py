# Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.

# Use the flow chart linked here to create the game logic.

# Once you've completed the project, you can always extend the game and make it more interesting!

#  Hint 
# Demo
# https://appbrewery.github.io/python-day3-demo/

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_r
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# 1st chapter
route = input("1st chapter condition, please type left or right.")

if route == "left" or route == "Left":
    # 2nd chapter
    route = input("you pass 1st chapter go to 2nd chapter condition, please type swim or wait.")
    if route == "Wait" or route == "wait":
        route = input("you pass 2nd chapter go to 2nd chapter condition, please type red, blue or yellow.")
        if route == "red" or route == "Red":
            print("Burnd by fire. Game Over")
        elif route == "blue" or route == "Blue":
            print ("Eaten by beasts. Game Over")
        elif route == 'yellow' or route == 'Yellow':
            print("Yey! You found a treasure.")
        else:
            print("Game OVer")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over")