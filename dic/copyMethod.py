profile = {
    'name': 'John Doe',
    'age': 45,
    'email': 'johndoe@net.com',
    'github': 'johndoe',
    'programmer': True
}

profile_copy = profile.copy()

if profile_copy == profile:
    print('Equal')
else:
    print('Not equal')
