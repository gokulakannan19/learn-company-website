import os
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "####"
    password = os.getenv("APP_PASSWORD")

    context = ssl.create_default_context()
    receiver = "####"

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)

    except Exception as e:
        print(f"Error sending email: {e}")
