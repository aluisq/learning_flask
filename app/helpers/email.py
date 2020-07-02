from app import mail
from flask_mail import Message

class Email:
    def welcome_email(name):
        pass

    def forgot_email(login):
        pass
    
    def alert_email(alert,email,*args):
            msg = Message("",recipients=[email])
            msg.html = "<span>Estou sendo enviado de uma aplicação</span><span style='color:blue;'>Py</span><span style='color:yellow;'>thon</span>"
            mail.send(msg)
            pass
