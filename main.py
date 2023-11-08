import smtplib

my_email="tenzinchoeyingofa@gmail.com"
password="zxqp fezs vrdi ryhg"
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs="tenzinchoeying91@gmail.com",
                    msg="subject: HI \n\n there this is python day 31 project about SMTP")
connection.close()