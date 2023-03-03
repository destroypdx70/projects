'''
products = [
  {
    "Product" : "Computer",
    "Price" : 1100
  },
  {
    "Product" : "Mouse",
    "Price" : 66
  },
  {
    "Product" : "USB",
    "Price" : 2
  }
]
items = []
prices = []
for item in products:
  items.append(item["Product"])
  prices.append(item["Price"])

items_v2 = list(map(lambda item: item["Product"], products))
prices_v2 = list(map(lambda price: price["Price"], products))

print("Products version 1 =>", items)
print("Prices version 1 =>", prices)
print("Prudcts version 2 =>", items_v2)
print("Price vesrion 2 =>", prices_v2)

def add_taxes(products):
  new_product = products.copy()
  new_product["Taxes"] = new_product["Price"] * .19
  return new_product

new_product = list(map(add_taxes, products))
print(new_product)


filter = list(filter(lambda product: product["Product"] == "USB", products))
print(filter)
print(len(filter))

import random

set_consoles = {"Ps4", "Ps5", "Ps3", "Xbox One"}
set_consoles_price = [100, 700, 20, 10]
set_consoles_buy = {}
for console in set_consoles:
    set_consoles_buy[console] = random.choices(set_consoles_price)

print(set_consoles_buy)

set_consoles_buy_v2 = {console: random.choices(set_consoles_price) for console in set_consoles}
print(set_consoles_buy_v2)

def summ(min, max):
  print("Min =>", min, "Max =_", max)
  sum = 0
  for x in range(1, 700):
    sum += x
  return sum

summ_v1 = summ(10, 90)
print(summ_v1)
result = summ(summ_v1, 10)
print(result)

def increment(x):
  return x * 4

increment_v2 = lambda x: x * 4

def increment_v3(x, func):
  return x * func(x)

increment_4 = lambda x, func : x * func(x)

result_v2 = increment_v3(44, increment)
print(result_v2)
result_v3 = increment_v3(result_v2, increment)
print(result_v3)

numbers = [1, 2, 3, 4, 5, 6, 7, 78]
numbers_v2 = []
for number in numbers:
  numbers_v2.append(number * 2)

numbers_v3 = [number * 2 for number in numbers]
print(numbers)
print(numbers_v3)

print(list(zip(numbers, numbers_v2)))

numbers_v4 = {number: number_2 for (number, number_2) in zip(numbers, numbers_v2)}
print(numbers_v4)

numbers_v5 = list(map(lambda number: number * 2, numbers_v4))
print("Numbers version 5 =>", numbers_v5)

numbers_v6 = list(map(lambda x, y : x * y, numbers_v5, numbers))
print(numbers)
print(numbers_v5)
print("Numbers version 6 =>", numbers_v6)


numbers_v100 = [1, 2, 3, 4, 5,77, 2312, 23, 424, 2, 3, 4, 5, 6]
numbers_v200 = []
for number in numbers_v100:
    numbers_v200.append(number * 3)

new_numbers = list(map(lambda x: x * 3, numbers_v100))
print(numbers_v200)
print(new_numbers)

print(list(zip(numbers_v100, numbers_v200)))

new_numbers_v1 = {number_1: number_2 for(number_1, number_2) in zip(numbers_v100, numbers_v200)}
print(new_numbers_v1)

numbers_y = list(filter(lambda x: x % 2 == 0, numbers_v100))
print(numbers_y)
'''
import functools

numbers = [1,2,3,4,5,6,6,7,7,8,8,22,1,1112,333,4]
numbers_v2 = []
for number in numbers:
  if number % 2 == 0:
    numbers_v2.append(number)

numbers_v3 = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers)
print(numbers_v2)
print(numbers_v3)


numbers_r = []
numbers_a = []
for number in numbers:
  numbers_r.append(number * 2)

numbers_v4 = list(map(lambda x: x * 2, numbers))
numbers_v5 = [number * 2 for number in numbers]
print(numbers_v4)
print(numbers_v5)
print(numbers_r)

print(list(zip(numbers_v5, numbers_v2)))

numbers_union = {number : number_2 for (number, number_2) in zip(numbers_v5, numbers_v2)}
print(numbers_union)

sum_numbers = functools.reduce(lambda x, y : x + y, numbers_v5)
print(sum_numbers)

sum_numbers_v2 = list(map(lambda x, y : x * y, numbers, numbers_v2))
print(numbers)
print(numbers_v2)
print(sum_numbers_v2)

import random

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

def sum(match):
  new_match = match.copy()
  new_match['the_whole_score'] = new_match['home_team_score'] + 20
  return new_match

new_match = list(map(sum, matches))
print(matches)
print(new_match)

set_country = {"Bolivia", "Colombia", "Venezuela"}
set_list = {}
for country in set_country:
  set_list[country] = random.randint(1, 11)

dict_winner = {country: random.randint(1, 11) for country in set_country}
print(set_list)

dict_winner_past = { country: population for(country, population) in dict_winner.items() if population < 9}
print(dict_winner_past)

home_list = []
for home_team_thewhole in matches:
  home_list.append(home_team_thewhole["home_team"])
print(home_list)

home_team = list(map(lambda item: item["home_team"], matches))
print(home_team)