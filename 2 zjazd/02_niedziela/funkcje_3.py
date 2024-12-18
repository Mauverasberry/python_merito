#
# def passwd_lenght(passwd):
#     print(f'Dlugosc hasla: {len(passwd)}')
#     return len(passwd)

def user_exist(user):
    if user in users.keys():
        return True
    return False

def passwd_correct(name, passwd):
    if users[name] == passwd:
        return True
    return False

users = {'Kamil': 'Kamil1',
         'Doris': 'Mandarynka',
         'Kasia_python': 'Python0'}
