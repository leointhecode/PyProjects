import tkinter as kin
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 50
LONG_BREAK_MIN = 20 * 60
TICK = "✅"
reps = 0
WORK_CYCLES = [1, 3, 5, 7]
REST_CYCLES = [2, 4, 6]
LONG_BREAK_CYCLE = 8
timer = ""
checks = ""


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    if timer == "":
        pass
    else:
        window.after_cancel(timer)
    timer_title.config(text="timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    tick.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps in WORK_CYCLES:
        timer_title.config(text="WORK", fg=RED)
        countdown(WORK_MIN)
    if reps in REST_CYCLES:
        timer_title.config(text="BREAK", fg=PINK)
        countdown(SHORT_BREAK_MIN)
    elif reps == 8:
        timer_title.config(text="LONG BREAK", fg=PINK)
        countdown(LONG_BREAK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global TICK
    minutes = floor(count / 60)
    seconds = count % 60

    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()

        global checks
        if reps in REST_CYCLES or reps == LONG_BREAK_CYCLE:
            checks += TICK
            tick.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = kin.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=30, bg=YELLOW)

# TOMATO
photo_tomato = kin.PhotoImage(file='tomato.png')
canvas = kin.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=photo_tomato)
# COUNT TEXT
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# TITLE IN DISPLAY
timer_title = kin.Label(text="timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_title.grid(column=1, row=0)

# BUTTONS
start_button = kin.Button(text="start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = kin.Button(text="reset", command=reset)
reset_button.grid(column=2, row=2)

# TICKS
tick = kin.Label(fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=4)

window.mainloop()
