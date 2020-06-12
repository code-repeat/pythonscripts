# Steps:
# ask for age
# 18-21 wristband
# 21+ drink, normal entry
# too young, sorry

age = input('Your age: ')
if age != "":
    age = int(age)
    if age >= 18 and age < 21:
        print('You have to wear wristband')
    elif age >= 21:
        print('You can have drinks. Normal entry')
    else:
        print('Too young, sorry')
else:
    print('Please enter an age')



