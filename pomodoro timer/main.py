from tkinter import *
import math
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
# GREEN = "#9bdeac"
GREEN = "#7A4069"
YELLOW = "#f7f5dd"
r_red = "#FFB4B4"
blue = "#B2A4FF"
p_green = "#7DCE13"
green = "#D9F8C4"
pinky = "#FFB4B4"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=YELLOW)
        messagebox.showinfo(title="Now ", message="Its your break time!!")
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Prachi")
window.config(padx=100, pady=50, bg=blue)

title_label = Label(text="Timer", fg=GREEN, bg=blue, font=(FONT_NAME, 45))
title_label.grid(column=1, row=0)

canvas = Canvas(width=220, height=234, bg=blue, highlightthickness=0)

# logo = PhotoImage(file="Prachi.logo.png")
# canvas.create_image(10,6,image=logo)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 117, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00.00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=RED, bg=blue)
check_marks.grid(column=1, row=3)

window.mainloop()
