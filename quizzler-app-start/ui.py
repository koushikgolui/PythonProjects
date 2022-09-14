from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.config(bg="white")
        self.quiz_text = self.canvas.create_text(150, 125, text="Question goes here", font=("arial", 20, "italic"),
                                                 width=250, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)
        tick_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=tick_image, borderwidth=0, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column=0, row=2)
        cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=cross_image, borderwidth=0, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(column=1, row=2)

        self.next_question_to_show()

        self.window.mainloop()

    def next_question_to_show(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=question)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.manage_score()

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.manage_score()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question_to_show)

    def manage_score(self):
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

