from collections import namedtuple
import smtplib, ssl

class EmailConst(object):
    def __init__(self, Subject, To, From, Content):
        """Generate email and send content using smtplib"""

        self.Subject = Subject
        self.To = To
        self.From = From
        self.Content = Content

    def __dict__(self):
        return {
            "Subject": self.Subject,
             "To": self.To,
             "From": self.From,
             "Content": self.Content
        }

    def __str__(self):
        m = self.__dict__()
        return str(namedtuple(
            "EmailConst", ["Subject", "To", "From", "Content"])(
                m.get("Subject"), m.get("To"), m.get("From"), m.get("Subject"
                )
            ))

    @property
    def mail(self):
        if (type(self.To) == type([]) and len(self.To) >= 2):
            to_string = str(", ".join(self.To))
        else:
            to_string = self.To
        
        return f"""\
From: {self.From}
To: {to_string}
Subject: {self.Subject}

{self.Content}"""

    def SendMail(self, Login: tuple, Content: dict = None, Mailing: tuple = ("localhost", 587)) -> dict:
        '''Send mail via mailing server, use (smtp.gmail.com, 587) for gmail hosting.
           
           NOTE: starting May 30, 2022, Google will no longer support the use of third-party apps or devices
           and the smtp.gmail.com server will be broken
        '''
 
        username, passwd = Login[0], Login[1]
        mail_server, mail_port = Mailing[0], Mailing[1]
        if (Content is None):
            Content = self.__dict__()

        context = ssl.create_default_context()
        with smtplib.SMTP(mail_server, mail_port) as smtplib_server:
            smtplib_server.ehlo()
            smtplib_server.starttls(context=context)
            smtplib_server.ehlo()

            smtplib_server.login(username, passwd)
            smtplib_server.sendmail(username, Content.get("To"), self.mail)

        return self.__dict__()
