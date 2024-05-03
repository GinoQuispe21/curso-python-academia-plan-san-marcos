class FormulasMatematicas:
    
    @staticmethod
    def suma(a, b):
        return a + b
    
    @staticmethod
    def resta(a, b):
        return a - b
    
    @staticmethod
    def division(a, b):
        return a / b

# print(FormulasMatematicas.division(10, 20))
# objet_formula_matematica = FormulasMatematicas()
# print(objet_formula_matematica.division(10, 20))

import random as rd
import string

# logica para valdiar seguridad del usuario
class UserSecurity:

    __len_password_security =  15
    __email_domains = {'hotmail.com', 'gmail.com', 'outlook.com'}

    @staticmethod
    def generate_random_password():
        characters = string.ascii_letters + string.digits + string.punctuation
        new_password = ''.join(rd.choice(characters) for _ in range(0, UserSecurity.__len_password_security))
        return new_password
    
    @staticmethod
    def validate_email(email) -> bool:
        domain = email.split('@')[-1]
        if domain in UserSecurity.__email_domains: return True
        else: return False

#UserSecurity.generate_random_password()
UserSecurity.generate_random_password()
print(UserSecurity.generate_random_password())

class UserProfile:

    def __init__(self, username, password, email) -> None:
        self.username = username
        self.password = password
        self.correo = email

    def login(self): pass

user_1 = UserProfile(username = "Gino21", password = UserSecurity.generate_random_password(), email = "ginoquispe@yahho.com")
print(user_1.username)

print(UserSecurity.validate_email(user_1.correo))