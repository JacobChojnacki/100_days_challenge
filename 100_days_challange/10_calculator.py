from additional_files.art_10 import logo

print(logo)

results = []


def add(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplicity(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtraction,
    "*": multiplicity,
    "/": divide
}


def calculator():
    first_number = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    while True:
        operation_choice = input("Pick an operation: ")
        second_number = float(input("What's the next operation?: "))
        calculation_function = operations[operation_choice]
        result = calculation_function(first_number, second_number)
        print(f"{first_number} {operation_choice} {second_number} = {result}")
        again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if again == 'y':
            first_number = result
        else:
            calculator()


calculator()
