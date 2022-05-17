from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**simakush):
    subject_pref = 'Create a Pitch!'
    sender_email = 'mercyakuku24@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**simakush)
    email.html = render_template(template + ".html",**simakush)
    mail.send(email)