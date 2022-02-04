# mailing
Python mailing API

# Usage
```python
from mailing import *
login = ("example@gmail.com", "password")

mail = EmailConst("Some Example Mail", "other@gmail.com", "example@gmail.com", "Hello, World!")
mail.SendMail(login)
```
