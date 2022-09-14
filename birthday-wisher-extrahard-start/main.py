##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "python.my.program@gmail.com"
PASSWORD = "test1234$$"

# 1. Update the birthdays.csv'


def add_csv_entry():
    name = input("Enter name of person to send mail: ")
    email = input("Enter the person's email: ")
    dob = input("Enter the Date of Birth (format : MM/DD/YYYY): ")
    year = int(dob.split("/")[2])
    month = int(dob.split("/")[0])
    day = int(dob.split("/")[1])
    user_details = f"{name},{email},{year},{month},{day}\n"
    with open(file="birthdays.csv", mode="a") as file:
        file.write(user_details)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


def choose_letter_template():
    import glob
    letter_templates = [f for f in glob.glob("letter_templates\*.txt")]
    return random.choice(letter_templates)


# 2. Check if today matches a birthday in the birthdays.csv

date_today = dt.datetime.today()
month_today = date_today.month
# print(month_today)
day_today = date_today.day

with open(file="birthdays.csv", mode="r") as file:
    name_list = file.readlines()[1:]
    for line in name_list:
        # print(line)
        fields = line.split(",")
        name = fields[0]
        month = int(fields[3])
        day = int(fields[4])
        email = fields[1]
        if month == month_today and day == day_today:
            with open(file=choose_letter_template(), mode="r") as letter:
                letter_content = letter.read()
                new_content = letter_content.replace("[NAME]", name)
                msg = EmailMessage()
                msg.set_content(new_content)
                msg["subject"] = "Happy Birthday!!"
                msg["to"] = email
                msg["from"] = SENDER_EMAIL
                connection = smtplib.SMTP(host="smtp.gmail.com")
                connection.starttls()
                connection.login(user=SENDER_EMAIL, password=PASSWORD)
                # connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=to_mail, msg=f"Subject:SUNDAY MOTIVATOR!!! \n\n{quote}")
                connection.send_message(msg)
                connection.close()

        else:
            print("No match")


# 4. Send the letter generated in step 3 to that person's email address.

# add_csv_entry()




