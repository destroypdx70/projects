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

home_team_result = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
print(home_team_result)
print(len(home_team_result))

away_team = list(filter(lambda item: item['away_team_score'] == 1, matches))
print(away_team)
print(len(away_team))

home_team_result_draw = list(filter(lambda item: item['home_team_result'] == 'Draw', matches))
print(home_team_result_draw)
print(len(home_team_result_draw))









def filter_by_length(words):
   # Escribe tu solución 👇
   result = list(filter(lambda letters: len(letters) >= 4, words))
   return result

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)