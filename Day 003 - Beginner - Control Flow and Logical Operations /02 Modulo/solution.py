# Modulo

# The modulo operator gives you the remainder of a division.

# 6 % 2 #will be 0

# 6 % 5 #will be 1

# 6 % 4 #will be 2

# PAUSE 1 - What is 10 % 3?
# What do you think this will output?

# print(10 % 3)

# PAUSE 2 - Check Odd or Even
# Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".

#  Hint 
# 1. First get the user input using the input() function.
# 2. Next, convert the input into an int using the int() function.
# 3. Now store the number in a variable.
# 4. Use the modulo (%) to check if the user input number can be divided cleanly by 2.
# 5. Use if/else to check if the result of the modulo check in step 4 is equal to 0 then that input number is even, otherwise it's odd.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")