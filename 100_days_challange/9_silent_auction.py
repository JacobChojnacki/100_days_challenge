from os import system, name
from additional_files.art_09 import logo
print(logo)
bidders_info = {}
while True:
    name_player = input("What is your name?: ")
    bid = int(input("What's you bid?: "))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    bidders_info[name_player] = bid
    maximum = 0
    winner = ""
    for bidder in bidders_info:
        value = bidders_info[bidder]
        if value > maximum:
            winner = bidder
            maximum = value
    if other_bidders == "no":
        print(f"The winner is {winner} ")
        break
    else:
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
