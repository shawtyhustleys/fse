import string
password = input("Введите пароль:") 
allowedsymb = '*&@#$%^!~-'
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + allowedsymb
isValid = True
if not len(password) == 8:
    print("Длина пароля не равна 8")
    isValid = False
if not any(symbol.isdigit() for symbol in password):
    print("В пароле отсутствуют цифры") 
    isValid = False
if not any(x in allowedsymb for x in password):
    print("В пароле отсутствуют спец символы")
    isValid = False
if not any(x.isupper() for x in password):
    print("В пароле отсутствуют заглавные буквы")
    isValid = False
if not any(x.islower() for x in password):
    print("В пароле отсутствуют строчные буквы")
    isValid = False
if any(x not in allowed for x in password):
    print("В пароле недопустимые символы")
    isValid = False
if isValid:
    print("Надежный пароль")
