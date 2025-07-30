import art

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply, divide
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations =  {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary operation
# print(operations["*"](4,8))

def calculator():
    print(art.logo)
    should_accumulate = True
    num_1 = float(input("What's the first number? "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick and operation: ")
        num_2 = float(input("What's the second number? "))
        answer = operations[operation_symbol](num_1, num_2)
        print(f"{num_1} {operation_symbol} {num_2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:  ")

        if choice == "y":
            num_1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()

