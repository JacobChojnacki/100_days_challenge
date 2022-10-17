import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}
word = input("Enter a word: ")
word_list = [letter.upper() for letter in word]
result = [nato_alphabet[letter] for letter in word_list]
print(result)
