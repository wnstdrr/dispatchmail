from mailing import *

login = ("example@gmail.com", "password")
mail = EmailConst("Example", login[0], login[0], "Hello, World!")

print(mail)
