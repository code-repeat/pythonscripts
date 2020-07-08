numbers = [1, 2, 3, 4, 5, 6]
numbers_cond = [num * 2 if num % 2 == 0 else num / 2 for num in numbers]
print(numbers_cond)
