## SMPT- SIMPLE MAIL TRANSFER PROTOCOL
import smtplib
import ssl
import datetime as dt
import random

current_date = dt.datetime.now()
day = current_date.weekday()

with open("./Email-SMTP/quotes.txt") as file:
    data = file.readlines()
    message = random.choice(data).strip("\n")

my_email = "ahmadfkwj@gmail.com"
password = "ztzqggocfdjfdruq"
context = ssl.create_default_context()

if day==4:
    connection = smtplib.SMTP("smtp.gmail.com",587,timeout=10)
    ## Secures connection
    connection.starttls(context=context)      

    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="ahmadfkwj@gmail.com",msg=f"Subject: Quote of the Day\n\n{message}")
    connection.close()






