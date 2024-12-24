# Condition Check
# Learn to use conditionals in Python to check a conditions and tell the computer what to do in each case. e.g.

# if <this condition is true>:

#     <then execute this line of code>

# What if the condition is false?
# The else keyword is used to define a block of code that will execute if the condition checked in the if statement is false.

# if pigs can fly:

#     <Some code that will never execute>

# else:

#     print("This is real life")

# Python Indentation
# Understand the importance of indentation in Python as a way to make certain lines of code subsidaries of other lines of code.

# e.g.

# if 5 > 2: #This is a parent line of code

#     print("yes") #this is a child line of code

# Comparator Operators
# use for > Greater than
# use for < Less than
# use for >= Greater than or equal to
# use for <= Less than or equal to
# use for == Equal to
# use for != Not equal to

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")