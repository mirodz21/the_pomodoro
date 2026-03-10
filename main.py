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

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("The Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
canvas.create_image(100, 110, image=img)
canvas.create_text(103, 130, text="00:00", fill="white", font=("New Times Roman",20,"bold"))
canvas.pack()

window.mainloop()