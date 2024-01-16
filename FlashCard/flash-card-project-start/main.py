import tkinter as kin
import pandas as pd
import random as rd

# DATA
try:
    data = pd.read_csv("flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    origin_data = pd.read_csv("flash-card-project-start/data/words.csv")
    data_dict = origin_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
BLACK = "#000000"
FONT_WORD = ("Arial", 80, "bold")
FONT_TITLE = ("Arial", 40, "italic")
card = rd.choice(data_dict)


# -RIGHT ANS------------------------------------------------------------------------------------------------------------
def next_card():
    global flip_timer, card
    card = rd.choice(data_dict)
    window.after_cancel(flip_timer)

    canvas.itemconfig(word, text=card['Language'], fill=BLACK)
    canvas.itemconfig(title, text="Lanuage", fill=BLACK)
    canvas.itemconfig(flash_card, image=front_card)

    flip_timer = window.after(3000, translation)


# -TRANSLATION----------------------------------------------------------------------------------------------------------
def translation():
    canvas.itemconfig(word, text=card['English'], fill=WHITE)
    canvas.itemconfig(title, text="English", fill=WHITE)
    canvas.itemconfig(flash_card, image=back_card)


# -WRONG ANS------------------------------------------------------------------------------------------------------------
def is_known():
    data_dict.remove(card)
    to_learn_final = pd.DataFrame(data_dict)
    to_learn_final.to_csv("flash-card-project-start/data/words_to_learn.csv", index=False)

    next_card()


# -UI SETUP-------------------------------------------------------------------------------------------------------------
window = kin.Tk()
window.title("FlashCard for languages")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, translation)

# IMAGE
front_card = kin.PhotoImage(file="flash-card-project-start/images/card_front.png")
back_card = kin.PhotoImage(file="flash-card-project-start/images/card_back.png")
right_image = kin.PhotoImage(file="flash-card-project-start/images/right.png")
wrong_image = kin.PhotoImage(file="flash-card-project-start/images/wrong.png")

canvas = kin.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

flash_card = canvas.create_image(405, 270, image=front_card)
word = canvas.create_text(400, 290, text="word", font=FONT_WORD)
title = canvas.create_text(390, 150, text="title", font=FONT_TITLE)

canvas.grid(row=0, column=0, columnspan=3, rowspan=2)

# BUTTONS
right_button = kin.Button(image=right_image, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=2, column=2)

wrong_button = kin.Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=2, column=0)

next_card()

window.mainloop()
