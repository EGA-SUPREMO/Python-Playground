import yagmail



yag = yagmail.SMTP(email, passw)

def sendEmail(email, passw, receiver, esubject, body):
    yag.send(
        to=receiver,
        subject=esubject,
        contents=body
    )
