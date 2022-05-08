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
        return namedtuple(
            "EmailConst", ["Subject", "To", "From", "Content"])(
                m.get("Subject"), m.get("To"), m.get("From"), m.get("Subject"
                )
            )

    def SendMail(self, Login: tuple, Content: dict = self.__dict__(), Mailing: str = "localhost") -> dict:
        '''Send mail via mailing server, use (smtp.gmail.com, 587) for gmail hosting.'''

        context = ssl.create_default_context()
        with smtplib.SMTP(Mailing, 587) as smtplib_server:
            smtplib_server.ehlo()
            smtplib_server.starttls(context=context)
            smtplib_server.ehlo()

            smtplib_server.login(Login[0], Login[1])
            smtplib_server.sendmail(Login[0], Content.get("To"), Content.get("Content"))

        return self.__dict__()
