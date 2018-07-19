import smtplib
content="Example email"
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail_id=input()
password=input()
mail.login(mail_id,password)
username=input()
receiver_mail=input()
mail.sendmail(username,receiver_mail,content)
mail.close()