import utils
import read_csv
import charts
import pandas as pd

def run():
  """
  data = read_csv.read_csv("data_population.csv")
  data = list(filter(lambda item: item["Continent"] == "Sount America", data))
  
  countries = list(map(lambda x : x["Country/Territory"], data))
  percentages = list(map(lambda x : x["World Population Percentage"], data))
  charts.generate_pie_chart(countries, percentages)
  """
  df = pd.read_csv("data_population.csv")
  df = df[df["Continent"] == "South America"]

  countries = df["Territory/Country"].values
  percentages = df["World Population Percentage"].values

  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv("data_population.csv")
  country = input("Type country => ")
  print(country)

  result = utils.population_by_countries(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country["Territory/Country"], labels, values)
  
if __name__ == "__main__":
  run()










