for num in range(1, 21):
    if num == 4 or num == 13:
        print(str(num) + ' Unlucky number')
    elif num % 2 == 0:
        print(str(num) + ' is even')
    else:
        print(str(num) + ' is odd')
