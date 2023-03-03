'''
def increment(x):
  return x + 1

increment_v2 = lambda x: x + 1

def high_order_function(x, func):
  return x + func(x)

high_order_function_v2 = lambda x, func: x + func(x)

result = high_order_function(2, increment)
# 2 + (2 + 1)
print(result)

result = high_order_function_v2(2, increment_v2)
print(result)
result = high_order_function_v2(2,lambda x: x + 2)
print(result)
result = high_order_function_v2(2,lambda x: x * 2)
print(result)

def increment(x):
  return x * 2

increment_v2 = lambda x : x * 2

result = increment(50)
print(result)
result_v2 = increment(result)
print(result_v2)

result_v2 = increment_v2(40)
print(result_v2)
result_v3 = increment_v2(result_v2)
print(result_v3)

def high_order_function(x, func):
  return x * func(x)

high_order_function_v2 = lambda x, func : x * func(x)

result_1 = high_order_function(55, increment_v2)
print(result_1)
result_2 = high_order_function(55, lambda x: x * 4)
print(result_2)

def increment(x):
  return x * 2

increment_v2 = lambda x: x * 2

result_v1 = increment(17)
print(result_v1)
result_v2 = increment_v2(17)
print(result_v2)

result_v3 = increment(result_v1)
print(result_v3)
result_v4 = increment(result_v2)

def high_order_function(x, func):
  return x * func(x)

high_order_function_v2 = lambda x, func : x * func(x)

result_v5 = high_order_function(40, increment)
print("Result version 5 =>", result_v5)
# 40 * (40 * 2)
# x * (x * 2)

def increment(x):
  return x * 2

increment_v2 = lambda x : x * 2

def high_order_function(x, func):
  return x * func(x)

high_order_function_v2 = lambda x, func : x * func(x)

result_v1 = high_order_function(55, lambda x: x * 2)
result_v2 = increment_v2(90)
result_v3 = high_order_function_v2(490, lambda x: x * 70)

print("Result version 1 =>", result_v1)
print("Result version 2 =>", result_v2)
print("Result version 3 =>", result_v3)

def increment(x):
  return x * 2

increment_v2 = lambda x: x * 2

def high_order_function(x, func):
  return x * func(x)

high_order_function_v2 = lambda x, func : x * func(x)

result_v1 = increment(1)
print("Result version 1 =>", result_v1)
result_v2 = increment(result_v1)
print("Result version 2 =>", result_v2)

result_v3 = increment_v2(1)
print("Result version 3 =>", result_v3)
result_v4 = increment_v2(result_v3)
print("Result version 4 =>", result_v4)

result_v5 = high_order_function(80, increment)
print("Result version 5 =>", result_v5)
# 80 * (80 * 2)

result_v6 = high_order_function(90, lambda x: x * 40)
print("Result version 6 =>", result_v6)
result_7 = high_order_function_v2(60, lambda x: x * 5)
print("Result version 7 =>", result_7)
'''
def increment(x):
  return x * 4

increment_v2 = lambda x : x * 4

def summ(min, max):
  print("Min =>", min, "Max", max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

def high_order_function(x, func):
  return x * func(x)

high_order_function_v2 = lambda x, func : x * func(x)

full_name = lambda name, age, last_name : f"My name is {name.title()}, I am {age} years, and my last name is {last_name.title()}"

text = full_name("Anyi", 18, "Gallego")
print(text)

text_v2 = "Anyi is my real love"
result = {my_real_love : text_v2.count(my_real_love) for my_real_love in text_v2 if my_real_love in "Anyi"}
print(text_v2)
print(result)

text_v3 = "Anyi is the only real love and my real love"
result_v2 = {my_real_love : my_real_love.upper() for my_real_love in text_v3 if my_real_love in "Anyi"}
print(text_v3)
print(result_v2)










