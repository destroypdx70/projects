dict = {}
for i in range(1, 5):
  dict[i] = i * 2

print(dict)

dict_V2 = { i : i * 2 for i in range(1, 5)}
print(dict_V2)

import random
countries = ["COl", "MEX", "BOL", "PER"]
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

population_V2 = { country : random.randint(1, 100) for country in countries }
print(population_V2)


my_family = ["Anyi", "Elizabeth", "Noah"]
ages = [34, 20, 23]

print(list(zip(my_family, ages)))


new_dict = {name : age for (name, age) in zip (my_family, ages)}
print(new_dict)

{
  "Anyi" : 34,
  "Elizabeth" : 20,
  "Noah" : 23
}

dict = {}
for i in range(1, 21):
  dict[i] = i * 2

print(dict)

dict_v2 = { i: i * 2 for i in range(1, 21)}
print(dict_v2)

import random

countries = {"Col", "Bol", "Per", "Suz"}
population = {}
for country in countries:
  population[country] = random.randint(1, 900)
  
print(population)

population = { country: random.randint(1, 900) for country in countries}
print(population)

names_family = ["Anyi", "Noah", "Elizabeth"]
age_family = [34, 23, 20]

print(list(zip(names_family, age_family)))

data_family = { name_family: age_family for (name_family, age_family) in zip(names_family, age_family)}
print(data_family)


dict = {}
for i in range(1, 100):
  dict[i] = i * 3

print(dict)

dict_v2 = { i: i * 3 for i in range(1, 100)}
print(dict_v2)

import random

countries = {"Rus", "Bra", "Esp", "Nor"}
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

population_v2 = { country: random.randint(1, 100) for country in countries}
print(population_v2)

names_family = ["Anyi", "Noah", "Elizabeth"]
age_family = [34, 23, 20]

print(list(zip(names_family, age_family)))

data_family = { name_family: age_family for (name_family, age_family) in zip(names_family, age_family)}
print(data_family)


set_computers = {"Msi", "Asus", "Mackbook"}
set_computers_old = {"Msi", "Asus"}

set_computers_old.add("HP")
set_computers_old.remove("Msi")
set_computers_old.discard("Asus")

set_thewhole_computers = set_computers.union(set_computers_old)
print(set_thewhole_computers)
print(set_computers | set_computers_old)
# set_computers_old.clear()
print("set computers old =>", set_computers_old)

set_products = []
for computers in set_thewhole_computers:
  if computers == "Msi":
    set_products.append(computers)

print(set_products)

set_products_v2 = [ computer for computer in set_thewhole_computers if computer == "Msi"]
print(set_products_v2)


numbers = []
for number in range(1, 90):
  if number % 2 == 0:
    numbers.append(number * 2)

print(numbers)


numbers = [number * 2 for number in range(1, 90) if number % 2 == 0]
print(numbers)


teams = ["Bolivia", "Brazil", "Mexico", "Uruguay", "Ecuador", "Venezuela"]
another_result = {}
for team in teams:
  another_result[team] : random.randint(1, 100)

print(another_result)