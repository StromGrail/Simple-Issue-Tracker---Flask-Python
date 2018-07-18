import smtplib
content="Example email"
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('mohitatul0803@gmail.com',password)
mail.sendmail('mohitatul0803','mohitatul0803@gmail.com',content)
mail.close()