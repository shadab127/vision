import sys
sys.path.append("C:\Users\Shadab Khan\Desktop\\vision7")
import smtplib
from Speechmanager.speech_manager import speech as sp
from Speechmanager.TTS import tts
from email.mime.text import MIMEText
def gmailer():
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("shadab1234567891011@gmail.com", "123456789@qwerty")

    tts.say("give me reciever email id")
    recieveremail = str(sp.gstt())
    recieveremail = recieveremail + '@gmail.com'
    print('vikas1000ad@gmail.com')

    # message to be sent
    tts.say("start writing mail")
    message = ''

    while True:
        text = sp.gstt()
        text = str(text)
        print(text)
        if text.lower() == 'stop writing':
            break
        text = text+" "
        message=message+text
    print(message)

    # sending the mail
    s.sendmail("shadab1234567891011@gmail.com", "vikas1000ad@gmail.com", message)

    x = "mail sent successfully to"+recieveremail
    tts.say(x)
    # terminating the session
    s.quit()
