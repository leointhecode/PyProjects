from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#ffffff"
FONT = ("Arial", 20, "italic")


class UserWindow(Tk):

    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()

        self.quiz = quiz_brain

        cross_image = PhotoImage(file="images/false.png")
        right_image = PhotoImage(file="images/true.png")

        self.config(width=500, height=600, padx=20, pady=20, bg=THEME_COLOR)
        self.title("Quizler")

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="", font=FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.cross_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, command=self.false_button)
        self.cross_button.grid(column=0, row=2, pady=20, padx=20)
        self.right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=self.true_button)
        self.right_button.grid(column=1, row=2, pady=20, padx=20)

        self.score = Label(text=f"score: {self.quiz.score}", bg=THEME_COLOR, fg=WHITE, font=("Arial", 12, "bold"))
        self.score.grid(row=0, column=1, pady=20, padx=20)

        self.next_q()

        self.mainloop()

    def next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="This is the end of the quiz.")
            self.cross_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def true_button(self):
        self.is_it_right(self.quiz.check_answer('True'))

    def false_button(self):
        self.is_it_right(self.quiz.check_answer('False'))

    def is_it_right(self, answer):
        if answer:
            self.canvas.config(bg="GREEN")
        else:
            self.canvas.config(bg="RED")
        self.after(1000, self.next_q)
