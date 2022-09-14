from tkinter import *
from tkinter import messagebox
import json

LABEL_FONTS = ("arial", 12, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    import random
    import string
    gen_password = None

    special_chars = "!#$&()*+=@%/"
    gen_password = "".join([random.choice(string.ascii_letters + string.digits + special_chars)
                            for n in range(random.randint(8, 16))])
    input_pwd.delete(0, END)
    input_pwd.insert(0, gen_password)


def search():
    website = input_wsite.get()

    try:
        with open("password.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Need to add an Entry before you can search")
    else:
        try:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        except KeyError:
            messagebox.showinfo(title="OOPS!!!", message=f"No details present for\n Website: {website}")
        #     # print(f"{email}\t\t{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_to_file():
    website = input_wsite.get()
    email = input_email.get()
    password = input_pwd.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        empty_field = messagebox.showinfo(title="OOPS!!!", message="Please leave no empty field")
    else:
        is_ok_to_save = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\n"
                                                                      f"Is it OK to save?")
        if is_ok_to_save:
            try:
                with open(file="password.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open(file="password.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open(file="password.json", mode="w") as file:
                    json.dump(data, file, indent=4)
                # file.write(f"{website} | {email} | {password}\n")
            input_wsite.delete(0, "end")
            input_wsite.focus()
            input_email.delete(0, "end")
            input_pwd.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# define the labels
label_wsite = Label(text="Website:")
label_wsite.grid(column=0, row=1)
label_uname = Label(text="Email/Username:")
label_uname.grid(column=0, row=2)
label_pwd = Label(text="Password:")
label_pwd.grid(column=0, row=3)

# Define text inputs
input_wsite = Entry(width=33)
input_wsite.grid(column=1, row=1)
input_wsite.focus()
input_email = Entry(width=51)
input_email.grid(column=1, row=2, columnspan=2)
input_pwd = Entry(width=33, justify="left")
input_pwd.grid(column=1, row=3)

# define buttons
button_search = Button(text="Search", width=14, command=search)
button_search.grid(column=2, row=1)
button_pwd = Button(text="Generate Password", command=generate_password)
button_pwd.grid(column=2, row=3)
button_add = Button(text="Add", width=20, command=save_to_file)
button_add.grid(column=1, row=4)


window.mainloop()