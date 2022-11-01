import random
import tkinter

import pandas
import pandas as pd

# ------------------------ CONSTANTS ---------------------#
BACKGROUND_COLOR = "#B1DDC6"
try:
    WORDS = pd.read_csv("./data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    WORDS = pd.read_csv("./data/french_words.csv").to_dict(orient="records")
english = ""
french = ""
# ------------------------ UPLOAD RANDOM WORDS --------------#
words_with_translate = []
for word in WORDS:
    words_with_translate.append((word["French"], word["English"]))


def next_card():
    global french, english, flipper_timer
    window.after_cancel(flipper_timer)
    french, english = random.choice(words_with_translate)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{french}", fill="black")
    canvas.itemconfig(card_type, image=card_front)
    flipper_timer = window.after(3000, func=flipper)


# --------------- SET UP TIMER TO SWITCH CARDS ------------------#
def flipper():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{english}", fill="white")
    canvas.itemconfig(card_type, image=card_back)


# -------------------- SAVE MECHANISM ----------------------#
def right_answer_clicked():
    global words_with_translate
    words_with_translate.remove((french, english))
    data = pd.DataFrame(words_with_translate)
    data.to_csv("./data/words_to_learn.csv", header=["French", "English"])
    next_card()


# ---------------------   window setup ---------------------#
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flipper_timer = window.after(3000, func=flipper)
# ---------------------   CANVAS ----------------------------#
canvas = tkinter.Canvas(width=800, height=526, highlightthickness=False, bg=BACKGROUND_COLOR)

card_front = tkinter.PhotoImage(file='./images/card_front.png')
card_back = tkinter.PhotoImage(file='./images/card_back.png')

right_answer = tkinter.PhotoImage(file='./images/right.png')
wrong_answer = tkinter.PhotoImage(file='./images/wrong.png')

# Canvas card back
card_type = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, 'bold'))

# --------------------------------- BUTTONS -------------------------------------------------#
right_answer_button = tkinter.Button(image=right_answer, highlightthickness=0, command=right_answer_clicked)
wrong_answer_button = tkinter.Button(image=wrong_answer, highlightthickness=0, command=next_card)

right_answer_button.grid(row=1, column=0)
wrong_answer_button.grid(row=1, column=1)

window.mainloop()
