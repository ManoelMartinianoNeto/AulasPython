import re

def validar_email(email):

    if '@' not in email:
        return False
  
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))
email = "exemplo@fg.com"
print(validar_email(email))
