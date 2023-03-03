try:
  print(0 / 0)
  assert 1 != 1, "One it is the same than one"
  age = int(input("Write here your age => "))
  if age < 18:
    raise Exception("Minors are not allowed")
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

for i in range(1, 11):
  print(i)

counter = iter(range(1, 11))
print(next(counter))


import functools

numbers = [1,2,3,4,5,6,6,6,7,8]
result = functools.reduce(lambda x, y : x + y, numbers)
print(result)

def accum(counter, item):
  print("Counter =>", counter)
  print("Item =>", item)
  return counter + item

result_v3 = functools.reduce(accum, numbers)
print("Result version 3 =>", result_v3)

numbers_v1 = [1,2,3,4,5]
numbers_v2 = [1,2,3,4,5]

result = list(map(lambda x, y : x * y, numbers_v1, numbers_v2))
result_v2 = list(map(lambda x : x * 2, numbers_v1))
print(result)
print(result_v2)

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

home_list = []
for home in matches:
  home_list.append(home['home_team'])

home_version_2 = list(map(lambda item: item['home_team'], matches))
print(home_list)
print(home_version_2)

home_filter = list(filter(lambda item: item['home_team'] == 'Bolivia', matches))
print(home_filter)

home_filter = list(filter(lambda item: item['home_team'] == 'Brazil', matches))
print(home_filter)

home_filter = list(filter(lambda item: item['home_team'] == 'Ecuador', matches))
print(home_filter)



set_team = ['Bolivia', 'Uruguay', 'Brazil', 'Mexico', 'Ecuador', 'Venezuela']
set_wins = [3,1,1,1,5,0]
set_wins_all = {}
for team in set_team:
  set_wins_all['Bolivia'] = 3
  set_wins_all['Uruguay'] = 1
  set_wins_all['Brazil'] = 1
  set_wins_all['Mexico'] = 1
  set_wins_all['Ecuador'] = 5
  set_wins_all['Venezuela'] = 0

print(set_wins_all)

set_wins_all_version_2 = {team: wins for(team, wins) in zip(set_team, set_wins)}
print(set_wins_all_version_2)

import csv

def read_csv(path):
   total = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for row in reader:
         total += int(row[1])
   return total

response = read_csv('./data.csv')
print(response)