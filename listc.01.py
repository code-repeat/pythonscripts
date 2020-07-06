#  Using for loop
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for number in numbers:
    doubled_number = number * 10
    doubled_numbers.append(doubled_number)


print(doubled_numbers)

#  Using List Comprehension
nums = [1, 2, 3, 4, 5]
new_numbers = [i * 10 for i in nums]
print(new_numbers)


