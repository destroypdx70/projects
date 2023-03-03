'''
numbers = [1, 2, 3, 4, 5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
print(numbers)
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 90, 347, 233, ]
numbers_v2 = []
for number in numbers:
  numbers_v2.append(number * 3)

print(numbers_v2)
result = list(map(lambda x: x * 2, numbers))
print(result)
result_v2 = [number * 2 for number in numbers]
print(result_v2)

new_numbers = list(filter(lambda x: x % 2 == 0, numbers_v2))
print(new_numbers)




