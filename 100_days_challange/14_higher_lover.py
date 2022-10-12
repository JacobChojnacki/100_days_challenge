from additional_files.art_14 import logo, vs
from additional_files.game_data_14 import data
import random
import os


def draw_player():
    player = random.choice(data)
    return player


player1 = draw_player()


def higher_lower(score=0):
    os.system('cls')
    print(logo)
    player2 = draw_player()
    print(f"Compare A: {player1['name']}, {player1['description']}, from {player1['country']}.")
    print(vs)
    print(f"Against B: {player2['name']}, {player2['description']}, from {player2['country']}.")
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == 'a':
            if player1['follower_count'] > player2['follower_count']:
                score += 1
                return higher_lower(score=score)
            else:
                return f"Sorry, that's wrong. Final score: {score}"
        else:
            if player1['follower_count'] < player2['follower_count']:
                score += 1
                return higher_lower(score=score)
            else:
                return f"Sorry, that's wrong. Final score: {score}"


print(higher_lower())
