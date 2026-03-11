import math
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    timer(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def timer(n):
    t_min = math.floor(n / 60)
    t_sec = n % 60
    if t_sec < 10:
        t_sec = "0"f"{t_sec}"
    canvas.itemconfig(cd_text, text=f"{t_min}:{t_sec}")
    if n >0:
        window.after(1000, timer, n -1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("The Pomodoro")
window.config(padx=100, pady=50, bg=PINK)
window.minsize(width=200, height=200)




img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
canvas.create_image(100, 110, image=img)
cd_text = canvas.create_text(103, 130, text="00:00", fill="white", font=("New Times Roman",20,"bold"))
canvas.grid(column=1, row=2)

title_text = Label(text="Timer")
title_text.config(font=("New Times Roman", 20, "bold"), fg="white", background=PINK)
title_text.grid(column=1, row=0)

btn_1 =Button(text="Start", command=start_timer)
btn_1.config(font=FONT_NAME,padx=5,pady=5,  highlightthickness=0)
btn_1.grid(column=0, row=3)

btn_2 =Button(text="Reset", command=reset_timer)
btn_2.config(font=FONT_NAME,padx=5,pady=5, highlightthickness=0)
btn_2.grid(column=3, row=3)

check_label = Label(text = "✔",fg=GREEN, background=PINK)
check_label.grid(column=1, row=4)

window.mainloop()