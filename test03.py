access_to_bank = False

while access_to_bank != True:
    print('Your name: ')
    name = input()
    print('Account number:')
    account_number = input()
    print('Password:')
    password = input()

    if account_number == '102899' and password == 'qwert123':
        print(f"Welcome to your account, {name}!")
        break
    else:
        print('Try again')
        continue



