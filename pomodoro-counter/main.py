from tkinter import *
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
reps = 0
check_text = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    label_timer.config(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED, font=(FONT_NAME, 30, "bold"))
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK, font=(FONT_NAME, 30, "bold"))
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label_timer.config(text="Work", fg=GREEN, font=(FONT_NAME, 30, "bold"))
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check_text
    global reps
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 9 == 0:
            check_label.config(bg=YELLOW, fg=GREEN)
            check_text = ''
        if reps % 2 == 0:
            check_text += '✔'
            check_label.config(text=check_text, bg=YELLOW, fg=GREEN)
        else:
            check_label.config(text=check_text, bg=YELLOW, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW, highlightthickness=0)
label_timer = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW)
image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start_button = Button(text="Start", font=(FONT_NAME, 15, "normal"), command=start_timer)
start_button.grid(column=0, row=2)
check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)
reset_button = Button(text="Reset", font=(FONT_NAME, 15, "normal"), command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()