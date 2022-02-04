import smtplib, ssl

class EmailConst(object):
   def __init__(self, Subject, To, From, Content):
      """Generate email and send content using smtplib & email"""

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

  def SendMail(self, Login: tuple, Reciever: str, Content: dict, Mailing: str = "localhost") -> dict:
      '''Send mail via mailing server, use (smtp.gmail.com, 587) for gmail hosting.'''

      context = ssl.create_default_context()
      with smtplib.SMTP(Mailing, 587) as smtplib_server:
         smtplib_server.ehlo()
         smtplib_server.starttls(context=context)
         smtplib_server.ehlo()

         smtplib_server.login(Login[0], Login[1])
         smtplib_server.sendmail(Login[0], Reciever, Content.get("Content"))

      return self.__dict__()
