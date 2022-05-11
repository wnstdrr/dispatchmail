from dispatchmail import EmailConst as Mail

def create_mail(login=("username", "password"), MailServer=("smtp.gmail.com", 587), From="example@mailserver.com"):
    mail = Mail("Automated Subject", ["user1@mailserver.com", "user2@mailserver.com"], From, "Hello, from mailing!")
    mail.SendMail(login, Mailing=MailServer)
    return mail.__dict__()

create_mail()
