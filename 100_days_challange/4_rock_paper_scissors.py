import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lista = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
print(lista[player_choice])
print("Computer choose:")
print(lista[computer_choice])
if player_choice == computer_choice:
    print("Draw")
elif player_choice == 0 and computer_choice == 2:
    print("You win")
elif player_choice == 0 and computer_choice == 1:
    print("You lose")
elif player_choice == 1 and computer_choice == 0:
    print("You win")
elif player_choice == 1 and computer_choice == 2:
    print("You lose")
elif player_choice == 2 and computer_choice == 1:
    print("You win")
else:
    print("You loose")