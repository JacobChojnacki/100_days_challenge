import random
from additional_files import hangman_words
from additional_files import hangman_art

stages = hangman_art.stages

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
lives = 6
end_of_game = False
print(hangman_art.logo)
display = ["_" for x in range(len(chosen_word))]
guesses = []
while not end_of_game:
    print(" ".join(display))
    guess = input("Guess a letter: ").lower()
    for i in range(len(display)):
        if chosen_word[i] == guess and guess not in guesses:
            display[i] = chosen_word[i]
    if guess in guesses:
        print("You've already guessed t")
    if guess not in chosen_word and guess not in guesses:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        lives -= 1
    if "_" not in display:
        end_of_game = True
        print(" ".join(display))
        print("You win.")
    if lives <= 0:
        print(stages[lives])
        end_of_game = True
        print("You loose")
    guesses.append(guess)

