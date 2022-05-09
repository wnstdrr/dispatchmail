# mailing
Light, simple, mailing api written in Python

# Usage
```python
from mailing import EmailConst as Mail

# NOTE: this is unsecure, consider hashing and storing your password!
login = ("example@gmail.com", "password")

mail = Mail("Some Example Mail", "other@gmail.com", "example@gmail.com", "Hello, World!")
mail.SendMail(login, Mailing=("smtp.gmail.com", 587))
```

mailing also supports the ability to send to multiple users, just spesfiy "To" as a list

```python
mail = Mail("Some Example Mail", ["other@gmail.com", "user@gmail.com"], "example@gmail.com", "Hello, World!")
```
