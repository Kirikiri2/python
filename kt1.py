network_connection = True
email = str(input("Введите почту: "))
at = "@"
dot = "."
while network_connection:
    while ((not(at in email)) or (not(dot in email))):
        email = str(input("Адрес не действителен, повторите попытку: "))
    network_connection = False
print("Ответ записан")
