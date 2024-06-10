#Calculator
from art import logo

#Add
def add(n1, n2):
    """ Takes two numbers and sums them together"""
    return n1 + n2

#Subtract
def subtract(n1, n2):
    """ Takes two numbers and subtracts them from each other"""
    return n1 - n2

#Multiply
def multiply(n1, n2):
    """ Takes two numbers and gets their product."""
    return n1 * n2

#Divide
def divide(n1, n2):
    """ Takes two numbers as input and divides them."""
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    continue_calculating = True

    while continue_calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'y':
            num1 = answer
        else:
            continue_calculating = False
            #calculator()

calculator()
