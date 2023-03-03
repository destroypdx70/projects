items = [
  {
    "Product" : "Ps5",
    "Price" : 800
  },
  {
    "Product" : "Xbox One",
    "Price" : 300
  },
  {
    "Product" : "Wii",
    "Price" : 200
  }
]
prices = []
for price in items:
  prices.append(price["Price"])

prices_v2 = list(map(lambda item: item["Price"], items))

print(prices)
print(prices_v2)

def add_taxes(item):
  new_item = item.copy()
  new_item["Taxes"] = new_item["Price"] * .19
  return new_item

new_item = list(map(add_taxes, items))
print(new_item)
print(items)







