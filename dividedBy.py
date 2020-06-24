def spam(d):
    try:
        return 42 / d
    except ZeroDivisionError:
        print('Error: Invalid argument')


print(spam(2))
print(spam(12))
print(spam(0))
