import smtplib

def send_mail(message):
    user = "rodenko.d96@gmail.com"
    passwd = "password"

    server = "smtp.gmail.com"
    port = 587

    receiver = "rodenko.d96@gmail.com"

    # подключаемся к почтовому сервису
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.ehlo()
    # логинимся на почтовом сервере
    smtp.login(user, passwd)
    # пробуем послать письмо
    smtp.sendmail(user, receiver, message.encode('utf-8'))




