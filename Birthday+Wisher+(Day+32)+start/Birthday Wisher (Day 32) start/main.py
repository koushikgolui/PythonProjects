import smtplib
import datetime as dt
from email.message import EmailMessage

SENDER_EMAIL = "python.my.program@gmail.com"
PASSWORD = "test1234$$"
QUOTES_FILE = "quotes.txt"
to_mail = "koushik21_golui@yahoo.com"


def get_quotes():
    import random

    with open(QUOTES_FILE) as file:
        quote_list = file.readlines()
    return random.choice(quote_list)


def send_email():
    quote = get_quotes()
    msg = EmailMessage()
    msg.set_content(quote)
    msg["subject"] = "Sunday Motivator!!!!"
    msg["from"] = SENDER_EMAIL
    msg["to"] = to_mail
    connection = smtplib.SMTP(host="smtp.gmail.com")
    connection.starttls()
    connection.login(user=SENDER_EMAIL, password=PASSWORD)
    # connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=to_mail, msg=f"Subject:SUNDAY MOTIVATOR!!! \n\n{quote}")
    connection.send_message(msg)
    connection.close()


today = dt.datetime.today()

if today.weekday() == 6:
    send_email()
