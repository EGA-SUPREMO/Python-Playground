import yagmail
import files

import time
import random

try:
    data = files.readJSON()[0]
except Exception:
    data = files.readJSON()[0]

yag = yagmail.SMTP(data["email"], data["apppassword"])

names = open("names.tm" , "r", encoding="utf8");
emails = open("emails.tm" , "r", encoding="utf8");

names = names.read().split("\n")
emails = emails.read().split("\n")

def sendEmail(receiver, esubject, body):
    yag.send(
        to=receiver,
        subject=esubject,
        contents=body
    )

    time.sleep(random.randint(120, 300))

x = open('x.txt', 'r').read()
x = int(x)

def send_spam(j, firstTime):
    how_many = 10
    for i in range(j, j + how_many):
        gretting = "Hello,\n\n"
        if names[i] != "":
            gretting = "Hello " + names[i] + ",\n\n"
        
        body = gretting + data["data_emails"][firstTime]
        print(str(i)+ " - "+ str(how_many - (i - j)))
        sendEmail(emails[i], "Offer to add subtitles to your videos", body)

    if firstTime<1:
        print("Ultima vez mandado para el id: "+ str(j+10))
        print("CAMBIADA LA X A: "+ str(x+10))
        files.writeX(x+10)

send_spam(x, 0)
if x > 9:
    send_spam(x, 1)
if x > 19:
    send_spam(x-20, 2)