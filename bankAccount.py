print('Account number: ')
account_number = input()
print('Password: ')
password = input()

account_number = int(account_number)
password = int(password)

if account_number != 102899 or password != 123:
    print('Wrong account number or password. Try again ')
else:
    print('Access granted. Welcome!')
