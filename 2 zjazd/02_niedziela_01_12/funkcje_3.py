#
# def passwd_lenght(passwd):
#     print(f'Dlugosc hasla: {len(passwd)}')
#     return len(passwd)

# user_exist(user): Sprawdza, czy użytkownik istnieje w słowniku users
def user_exist(user):
    if user in users.keys():
        return True
    return False

# passwd_correct(name, passwd): Sprawdza, czy podane hasło jest poprawne dla danego użytkownika.
def passwd_correct(name, passwd):
    if users[name] == passwd:
        return True
    return False

# register_user(name, passwd): Dodaje nowego użytkownika do słownika users.
def register_user(name, passwd):
    users[name] = passwd
    print(f'Użytkownik {name} został zarejestrowany.')


users = {'Kamil': 'Kamil1',
         'Doris': 'Mandarynka',
         'Kasia_python': 'Python0'}
