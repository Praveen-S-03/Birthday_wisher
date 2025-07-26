import pandas
import datetime as dt
import smtplib
import random
import os
from dotenv import load_dotenv
load_dotenv()
my_email = os.getenv("Enter_your_email")
password = os.getenv("Enter_your_password")
now = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
data_sheet = data.to_dict(orient="records")
for i in range(len(data_sheet)):
    current_name = data_sheet[i]
    sender_mail =current_name["email"]
    sender_name = current_name["name"]
    with open("letter_templates/letter_1.txt", "r") as l1:
        content = l1.read()
        letter_1 = content.replace("[NAME]", sender_name)
    with open("letter_templates/letter_1.txt", "r") as l2:
        content = l2.read()
        letter_2 = content.replace("[NAME]", sender_name)
    with open("letter_templates/letter_1.txt", "r") as l3:
        content = l3.read()
        letter_3 = content.replace("[NAME]", sender_name)
    letter = [letter_1, letter_2, letter_3]
    new_randon_letter = random.choice(letter)
    if current_name["month"] == now.month and current_name["day"] == now.day:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=sender_mail,
                                msg=f"Subject:Happy Birthday\n\n {new_randon_letter} ")
