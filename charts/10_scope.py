'''
price = 100 # Global

def increment():
  price = 100
  price = price + 10
  print(price)
  return price
  
print(price)
price_2 = increment()
print(price_2)
'''

set_shirts = {"Black", "Blue", "Red", "Green"}
set_jeans = {"Black", "Purple", "Silver"}

set_shirts.add("Brown")
set_jeans.add("Orange")
print(set_shirts)
print(set_jeans)
set_shirts.remove("Black")
set_jeans.remove("Black")
print(set_shirts)
print(set_jeans)
set_shirts.discard("Yellow")
set_jeans.discard("Pink")
print(set_shirts)
print(set_jeans)
set_shirts.clear()
set_jeans.clear()

set_shirts = {"Black", "Blue", "Red", "Green"}
set_jeans = {"Black", "Purple", "Silver"}

import random

options_color = ["Black", "Blue", "Red", "Black", "Purple", "Silver"]
option_garment = ["Cap", "Shirt", "Sweter", "Jean"]

set_products_v1 = {}
set_products_v2 = {}
for color in options_color:
  set_products_v1[color] = random.choices(option_garment)
  set_products_v2[color] = random.choices(option_garment)
print(set_products_v1)

set_products_v3 = { color: random.choices(option_garment) for color in options_color }
print(set_products_v3)

set_thewhole_products = set_shirts.union(set_jeans)
print(set_thewhole_products)
print(set_shirts | set_jeans)

numbers = []
for number in range(1, 100):
  if number % 2 == 0:
    numbers.append(number * 4)
print(numbers)

numbers_v2 = [number * 4 for number in range(1, 100) if number % 2 == 0]
print(numbers_v2)

countries = {"Col", "Suz", "Can", "Usa", "Esp"}
population = {}
for country in countries:
  population[country] = random.randint(1, 90)

print(population)

population_v2 = { country: random.randint(1, 90) for country in countries }
print(population_v2)

population_v3 = { country: population for (country, population) in population_v2.items() if population > 40}
print(population_v3)

def summation(a, b):
  sum = (a + b)
  return sum
  
result = summation(20, 80)
print(result)
result_v2 = summation(result, result * 2)
print(result_v2)

def calculate_volume(w, d, k):
  return w * d * k

result = calculate_volume(80, 90, 100)
print(result)


price = 800

def increment():
  price = 100
  price = price + 20
  print(price)
  return price

print(price)
price_2 = increment()
print(price_2)


def summation(min, max):
  print("Min =>", min, "Max =>", max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result_v3 = summation(68, 90)
print(result_v3)

def volume(w, d, p):
  return w * d * p 

result_v4 = volume(2, 8, 10)
print(result_v4)

def increment_v1(a, b):
  print("a =>", a, "b =>", b)
  multiplication = (a * b)
  return multiplication

result_v6 = increment_v1(40, 20)
print("Result =>", result_v6)
result_v7 = increment_v1(result_v6, result_v6 * 4)
print("Result =>", result_v7)
