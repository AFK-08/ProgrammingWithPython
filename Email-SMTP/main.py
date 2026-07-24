## SMPT- SIMPLE MAIL TRANSFER PROTOCOL
import smtplib
import ssl

my_email = "ahmadfkwj@gmail.com"
password = "ztzqggocfdjfdruq"
context = ssl.create_default_context()


connection = smtplib.SMTP("smtp.gmail.com",587,timeout=10)
 ## Secures connection
connection.starttls(context=context)      

connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="onegreatparagraph@gmail.com",msg="Hello Ahmad, It's Python Here!")
connection.close()

