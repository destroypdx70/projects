import random
countries = ["COL", "MEX", "BOL", "PER"]

population_V2 = { country: random.randint(1, 100) for country in countries }
print(population_V2)

for keys, values in population_V2.items():
  print(keys, "=>", values)

result = { country: population for (country, population) in population_V2.items() if population > 50}
print(result)

text = "Hi, I am Anyi"
unique = { c: c.upper() for c in text if c in "aeiouy"}
print(unique)

import random

countries = {"Col", "Rus", "Suz", "Arg", "Bra"}
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

population_v2 = { country: random.randint(1, 100) for country in countries }
print(population_v2)
    
population_v3 = { country: population for (country, population) in population_v2.items() if population > 70}
print(population_v3)

numbers = []
for number in range(1, 10):
  if number % 2 == 0:
    numbers.append(number * 2)
print(numbers)

numbers_v2 = [number * 2 for number in range(1, 10) if number % 2 == 0]

import random

countries = {"Rus", "Suz", "Ala", "Arg", "Bra"}
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

population_v2 = { country: random.randint(1, 100) for country in countries }
print(population_v2)

population_v3 = { country: population for (country, population) in population_v2.items() if population > 70}
print(population_v3)

my_text = "I only love Anyi"
unique = { c: c.upper() for c in text if c in "anyi"}
print(unique)
      
import random

countries = {"Bol", "Per", "Can", "Usa"}
population_v1 = {}

population_v1 = { country: random.randint(1, 100) for country in countries }
print(population_v1)

population_v2 = { country: population for (country, population) in population_v1.items() if population < 70}
print(population_v2)

my_text = "I really love you Anyi"
unique = { c: my_text.count(c) for c in my_text if c in "Anyi"}
print(unique)





















