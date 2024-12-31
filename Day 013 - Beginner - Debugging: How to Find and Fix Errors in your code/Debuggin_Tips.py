# 1. Describe the problem
#       a. Describe the Problem - Write your answers as comments:
# 		    - What is the for loop doing?
# 		    - When is the function meant to print "You got it"?
# 		    - What are your assumptions about the value of i?
# 		    - etc...

# 2. Reproduce the Bug - Some bugs are sneaky, they only occur under certain conditions. In order to debug them, we need to be able to reliably reproduce the bug and diagnose our problem to figure out which conditions trigger the bug.

# 3. Play Computer (Act as you are a compiler) - Playing computer is an important skill in debugging. You need to be able to go through your code line by line as if you were the computer to help you figure out what is going wrong.

# 4. Fix the Errors - Fix any errors (red underlines) that show up in the editor before you run your code. The warnings (yellow) are optional fixes, sometimes it will cause a problem down the line other times it's fine and the editor just doesn't understand what you are trying to do.
#
# Catching Exceptions
# You can use a try/except block in Python to catch any exceptions that might occur. For example if you imagine there could be a chance of user error. You can prevent it crashing your code by anticipating it. You trap the dangerous code inside a try block and use an except block to catch any potential errors. Then you define what should happen when that error occurs instead of simply just crashing and stopping the code.
#
####### try except block example #######
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
########################################

# 5. Print ("is your friend") - print() is your friend. It can help expose hidden values while your code is running. In a for loop, the loop will follow some rules to perform a repeated block of code. But during the loop it's difficult to see the intermediate values, that's a perfect example of how you can use print to expose those intermediate values and help you debug your code.

# 6. Use a Debugger - Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging. This is normally known as the debugger. In many ways, they are like print statements on steroids.
#
# Debuggers allows us to peek into our code during execution and pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.
#
# There are a couple of things that are the same in most IDEs which you should be familiar with:
#
# Breakpoint - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). This line will be where the program pauses during debug run.
#
# Step Over - This button will go through the execution of your code line by line and allow you to view the intermediate values of your variables.
#
# Step Into - This will enter into any other modules that your code references. e.g. If you use a function from the random module it will show you the original code for that function so you can better understand its functionality and how it relates to your problems.
#
# Step Into My Code - This does the same thing as Step Into, but it limits the scope to your own project code and ignores library code such as random.

# 7. Take a break - take nap, take bath, walk, sandwich and cup of tea, etc.

# 8. Ask a friend - yes can ask your friend, but make sure you have done your homework before asking your friend.

# 9. Run often (Run code often step by step) - Running your code often will help you catch bugs early and make it easier to trace back to the source of the problem. Running your code often will help you catch bugs early and make it easier to trace back to the source of the problem.

# 10. Ask StackOverflow (or Use AI , listen but prove!) - StackOverflow is a great resource for finding answers to common problems. You can search for your problem and find answers that have been given by other developers. It's a great way to learn and find solutions to your problems.