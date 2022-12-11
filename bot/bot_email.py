import smtplib


def send_email(message):
    sender = "english.test.cs@gmail.com"
    password = "ah0764vv"
    destination = "ivan4ik1986@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, destination, message)

        return "The message was sent successfully"

    except Exception as ex:
        return ex
