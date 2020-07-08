#  All the numbers divisible by 12 in a range from 1 up to 100 (including 100)
answer = [num for num in range(1, 101) if num % 3 == 0 and num % 4 == 0]
print(answer)