import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "shayanp100@gmail.com"
password = "qhfewkakrupwhhvz"

receiver = "shayanp100@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)