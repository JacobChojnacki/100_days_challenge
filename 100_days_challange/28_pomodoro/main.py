import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
countdown = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(countdown)
    global REPS
    REPS = 0
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=RED)
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global countdown
        countdown = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
timer = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, 'bold'))
timer.grid(column=1, row=0)

# Canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

# Buttons
start_button = tkinter.Button(text="Start",
                              command=start_timer,
                              width=5,
                              highlightthickness=0)

reset_button = tkinter.Button(text="Reset",
                              command=reset_timer,
                              width=5,
                              highlightthickness=0)

start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

# Check marks
check_marks = tkinter.Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
