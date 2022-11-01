import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        # Score
        self.score_label = tkinter.Label(text=f"Score: {self.quiz.score}", fg="#FFF", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        # CANVAS
        self.canvas = tkinter.Canvas(width=300, height=250, bg="#FFF")
        self.question = self.canvas.create_text(150, 125,
                                                width=280,
                                                text="XD", fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # BUTTONS
        self.agree_img = tkinter.PhotoImage(file="./images/true.png")
        self.agree_btn = tkinter.Button(image=self.agree_img, highlightthickness=0, command=self.good_answer)
        self.disagree_img = tkinter.PhotoImage(file="./images/false.png")
        self.disagree_btn = tkinter.Button(image=self.disagree_img, highlightthickness=0, command=self.false_answer)
        self.agree_btn.grid(column=0, row=2)
        self.disagree_btn.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="#FFF")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="END")
            self.agree_btn.config(state="disabled")
            self.disagree_btn.config(state="disabled")

    def good_answer(self):
        answer = self.quiz.check_answer("True")
        self.feedback(answer)

    def false_answer(self):
        answer = self.quiz.check_answer("False")
        self.feedback(answer)

    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)