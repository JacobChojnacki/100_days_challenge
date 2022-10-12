def calculator():
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bill? $"))
    percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    peoples_to_split = int(input("How many people to split the bill?"))
    return f"Each person should pay: ${(total_bill + (total_bill * (percentage_tip / 100))) / peoples_to_split:.2f}"


print(calculator())
