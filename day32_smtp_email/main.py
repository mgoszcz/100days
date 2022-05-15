# import smtplib
#
# my_email = "test.mg.python@gmail.com"
#
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#
#     # connection.starttls()
#     connection.login(user=my_email, password="test python")
#     connection.sendmail(from_addr=my_email, to_addrs="marcin.goszczynski88@gmail.com", msg="Subject:Hello\n\nBody")

import datetime

now = datetime.datetime.now()

print(datetime.datetime.now())