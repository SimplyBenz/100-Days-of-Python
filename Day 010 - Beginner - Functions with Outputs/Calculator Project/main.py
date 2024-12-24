import art

def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

number01 = 0
number02 = 0
output_number = 0
math_operator = ""
conti = "n"

while 1 == 1:

    if conti == "n":
        print(art.logo)
        number01 = int(input("What is the first number?: "))
    elif conti == "y":
        number01 = output_number

    math_operator = input("+\n-\n*\n/\nPick and operation: ")
    number02 = int(input("What is the second number?: "))

    if math_operator == "+":
        output_number = add(number01,number02)
    elif math_operator == "-":
        output_number = minus(number01,number02)
    elif math_operator == "*":
        output_number = multiply(number01,number02)
    elif math_operator == "/":
        output_number = divide(number01, number02)

    print(f"{number01} {math_operator} {number02} = {output_number}")
    
    conti = input(f"Type 'y' to start continue with {output_number}, or type 'n' to start new calculation: ")