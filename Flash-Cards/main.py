from tkinter import *
import pandas
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"
next_card = {}

# function to generate a new word


def generate_new_word():
    from random import choice
    global next_card
    if len(words_dict) > 0:
        next_card = choice(words_dict)
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(french_english, text="French", fill="black")
        canvas.itemconfig(word, text=next_card["French"], fill="black")
        window.after(3000, flip_card)
    else:
        messagebox.showinfo(title="Great!!", message="YAHOO!!!\nYou got all cards right!")

# flip the image


def flip_card():
    global next_card
    canvas.itemconfig(canvas_image, image=flip_image)
    canvas.itemconfig(french_english, text="English", fill="white")
    canvas.itemconfig(word, text=next_card["English"], fill="white")

# remove known words


def remove_known_words():
    global next_card
    words_dict.remove(next_card)
    generate_new_word()

# Read the csv get the data


words = pandas.read_csv("data/french_words.csv")
words_dict = words.to_dict(orient="records")

# Create the UI

# set up the window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Set the canvas attribute
canvas = Canvas(width=800, height=526, highlightthickness=0, borderwidth=0, relief="solid", bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
flip_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)

# create canvas Text

french_english = canvas.create_text(400, 150, text="", font=("arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("arial", 60, "bold"))
generate_new_word()
# set the button
right_image = PhotoImage(file="images/right.png")
r_button = Button(image=right_image, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0,
                  command=remove_known_words)
r_button.grid(row=1, column=1)
wrong_image = PhotoImage(file="images/wrong.png")
l_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0, padx=50,
                  command=generate_new_word)
l_button.grid(row=1, column=0)

window.mainloop()
