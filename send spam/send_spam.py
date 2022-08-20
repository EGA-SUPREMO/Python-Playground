import yagmail
import files

import time
import random

try:
    data = files.readJSON()[0]
except Exception:
    data = files.readJSON()[0]

#yag = yagmail.SMTP(data["email"], data["apppassword"])

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

x = 0

def send_spam(j, firstTime):
    for i in range(j, j + 10):
        gretting = "Hello,\n\n"
        if names[i] != "":
            gretting = "Hello " + names[i] + ",\n\n"
        
        body = gretting + data["data_emails"][firstTime]

        sendEmail(emails[i], "Offer to add subtitles to your videos", body)

    print("Ultima vez mandado para el id: "+ str(j+10))
    print("CAMBIA LA X A: "+ str(x+10))

send_spam(x, 0)
if x > 9:
    send_spam(x-10, 1)