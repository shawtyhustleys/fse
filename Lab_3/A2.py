import string
password = input()  
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
#print(allowed)        
#print(password.lower())
if len(password) != 8:
    print("Длина пароля не равна 8")
if not any(symbol.isdigit() for symbol in password):
    print("В пароле отсутствуют цифры") 
if not any(symb.isdigit() in '*&@#$%^!~-#' for symb in password):
    print("В пароле отсутствуют спец символы")
if not any(symbol.isupper() for symbol in password):
    print("В пароле отсутствуют заглавные буквы")
if not any():
    print("В пароле отсутствую")