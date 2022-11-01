import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ")
    word_list = [letter.upper() for letter in word]
    try:
        result = [nato_alphabet[letter] for letter in word_list]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
