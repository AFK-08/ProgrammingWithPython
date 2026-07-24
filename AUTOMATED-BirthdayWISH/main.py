## AUTOMATED BIRTHDAY WISHING PROJECT

import pandas,smtplib,random,ssl
import datetime as dt

my_email = "ahmadfkwj@gmail.com"
password = "ztzqggocfdjfdruq"
context = ssl.create_default_context()


## Accessing Birthday Dates from CSV 

data = pandas.read_csv("./AUTOMATED-BirthdayWISH/birthdays.csv")
name = data.name.item()
birthday_date = data.day.item()
birthday_month = data.month.item()

## Accessing Current Dates

current_date = dt.datetime.now()

current_month = current_date.month
current_day = current_date.day

if birthday_date==current_day and birthday_month==current_month:
    ## Picking Up letter to send:
    letter_choice = random.randint(1,3)

    ## Opening Letter and Modifying

    with open(f"./AUTOMATED-BirthdayWISH/letter_templates/letter_{letter_choice}.txt") as file:
        data = file.read()
        message = data.replace("[NAME]",name)

    connection = smtplib.SMTP("smtp.gmail.com",587,timeout=10)
    connection.starttls(context=context)
    connection.login(user="ahmadfkwj@gmail.com",password=password)
    connection.sendmail(from_addr=my_email,to_addrs="ahmadfkwj@gmail.com",msg=f"Subject:HAPPY BIRTHDAY\n\n{message}")

    connection.close()


