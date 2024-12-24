# Password Generator Project
#
# The program will ask:

# How many letters would you like in your password?
# How many symbols would you like?
# How many numbers would you like?
# The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

# Demo
# https://appbrewery.github.io/python-day5-demo/

# Easy Version
# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants

# 4 letters 2 symbols and 3 numbers then the password might look like this:

# fgdx$*924

# You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy LV

# for pass_letter in range(1,nr_letters):
#     print(random.choice(letters),end="")
# for pass_symbols in range(1,nr_symbols):
#     print(random.choice(symbols),end="")
# for pass_number in range(1,nr_numbers):
#     print(random.choice(numbers),end="")

#Head LV

GenPass_List=[]
password =""

for pass_letter in range(1,nr_letters+1):
    GenPass_List.append(random.choice(letters))
for pass_symbols in range(1,nr_symbols+1):
    GenPass_List.append(random.choice(symbols))
for pass_number in range(1,nr_numbers+1):
    GenPass_List.append(random.choice(numbers))

# Even this method use less code, But It allowed to use more same character
#
# for char in GenPass_List:
#     password += random.choice(GenPass_List)

# This shuffle method is better
random.shuffle(GenPass_List)
print(GenPass_List)

for char in GenPass_List:
    password += char

print(password)



