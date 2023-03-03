numbers = [1, 2, 3, 4, 5]
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda i: i * 2, numbers))

 

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 = [1, 4, 5, 6, 7]
numbers_2 = [3, 4, 6, 2, 0]

numbers_3 = list(zip(numbers_1, numbers_2))
print(numbers_3)

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)

numbers_4 = {number : number_2 for (number, number_2) in zip(numbers_1, numbers_2)}
print(numbers_4)

numbers = [1, 2, 3, 4, 5]
numbers_v2 = []
for number in numbers:
  numbers_v2.append(number * 2)

numbers_v3 = list(map(lambda number: number * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [8, 9, 10]

result = list(map(lambda x, y : x + y, numbers_1, numbers_2))
print(result)

print(list(zip(numbers_1, numbers_2)))

result_union = {number : number_2 for (number, number_2) in zip(numbers_1, numbers_2)}
print(result_union)

numbers = [1, 2, 3, 4, 5, 6]
numbers_v2 = []
for number in numbers:
  numbers_v2.append(number * 2)

numbers_v3 = list(map(lambda number: number * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 = [1, 2, 3, 4, 5, 6]
numbers_2 = [4, 5, 6, 7, 8]

numbers_1[0] = 40

result = list(map(lambda x, y : x * y, numbers_1, numbers_2))
print(result)

result_union = { number : number_2 for(number, number_2) in zip(numbers_1, numbers_2)}
print(result_union)

print(list(zip(numbers_1, numbers_2)))

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_v2 = []
for number in numbers:
  numbers_v2.append(number * 2)

numbers_v3 = list(map(lambda number: number * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7, 8]
numbers_2 = [8, 43, 5, 6, 7, 89, 1, 464, 6, 34, 13421342]

result = list(map(lambda x, y : x * y, numbers_1, numbers_2))
print(result)

result_union = { number: number_2 for (number, number_2) in zip(numbers_1, numbers_2)}
print(result_union)

print(list(zip(numbers_1, numbers_2)))

numbers = [1, 2, 3, 4, 5, 5,]
numbers_v2 = []
for number in numbers:
  numbers_v2.append(number * 2)

numbers_v3 = list(map(lambda number: number * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8]
numbers_2 = [2, 4, 5, 76, 8, 9, 23, 5]

result = list(map(lambda x, y : x * y, numbers_1, numbers_2))
print(result)

result_union = { number: number_2 for(number, number_2) in zip(numbers_1, numbers_2)}
print(result_union)

print(list(zip(numbers_1, numbers_2)))

def multiply_numbers(numbers):
    # Escribe tu solución 👇
    result = list(map(lambda number: number * 2, numbers))
    return result

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)


numbers_h = [1, 2, 3, 4, 5]
number_z = []
for number in numbers_h:
  number_z.append(number * 2)

print(number_z)

numbers_l = [number * 2 for number in numbers_h]
print(numbers_l)

numbers_a = list(map(lambda number: number * 2, numbers_h))
print(numbers_a)




