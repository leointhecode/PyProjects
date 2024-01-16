import smtplib
import datetime as dt
import random as rd
import pandas as pd

file = pd.read_csv("birthdays.csv")

PLACEHOLDER = "[NAME]"
    MY_EMAIL = "strongmaidboy@gmail.com"
    MY_PASSWORD = "501073yt lol"
DATE = dt.datetime.now()

with open("letter_templates/letter_1.txt") as letter1:
    let1 = letter1.read()
with open("letter_templates/letter_2.txt") as letter2:
    let2 = letter2.read()
with open("letter_templates/letter_3.txt") as letter3:
    let3 = letter3.read()

letters_list = [let1, let2, let3]
current_letter = rd.choice(letters_list)

for (index, row) in file.iterrows():

    if DATE.day == row[4] and DATE.month == row[3]:

        final_letter = current_letter.replace(PLACEHOLDER, row[0])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=row[1],
                                msg="Subject:Happy Birthday \n\n"
                                    f"{final_letter}",
                                )
    else:
        print("No birthday today")
        pass
