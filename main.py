# import smtplib
#
# my_email="tenzinchoeyingofa@gmail.com"
# password="zxqp fezs vrdi ryhg"
# connection=smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="tenzinchoeying91@gmail.com",
#                     msg="subject: HI \n\n there this is python day 31 project about SMTP")
# connection.close()

#------------Challenge ---------------
import datetime as dt
import random as rd
import smtplib

my_email="tenzinchoeyingofa@gmail.com"
password="zxqp fezs vrdi ryhg"
week_quotes=''

today=dt.datetime.now()
currentDay=today.weekday()

with open("quotes.txt","r") as file:
    quotes=file.readlines()
    week_quotes+=rd.choice(quotes)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    if currentDay ==2:
        connection.sendmail(from_addr=my_email,
                            to_addrs="tenzinchoeying91@gmail.com",
                            msg=f"subject:WEEKLY MOTIVATIONAL QUOTES \n\n {week_quotes}")
    else:
        print("today is not Wednesday")


