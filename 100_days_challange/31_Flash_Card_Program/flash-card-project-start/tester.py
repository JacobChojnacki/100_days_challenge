import pandas as pd
import random

WORDS = pd.read_csv("./data/french_words.csv").to_dict(orient="records")

words_with_translate = []

for word in WORDS:
    words_with_translate.append((word["French"], word["English"]))

french, english = random.choice(words_with_translate)
print(len(words_with_translate))
print(words_with_translate)
words_with_translate.remove((french, english))
print(len(words_with_translate))
print(words_with_translate)
data = pd.DataFrame(words_with_translate)
data.to_csv("XD.csv",header=["French", "English"])