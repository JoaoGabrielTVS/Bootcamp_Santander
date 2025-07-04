email = input().strip()


if(email[0] == "@" or email[-1] == '@' or ('@gmail.com' not in email and '@outlook.com' not in email) ):
    print('E-mail inválido')
else:
    print('E-mail válido')

