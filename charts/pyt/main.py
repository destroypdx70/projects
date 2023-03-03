import functools

def run():
  
  def get_total(orders):
    total = list(map(lambda item: item["total"], orders))
    result = functools.reduce(lambda x, y : x + y , total)
    return result
  
  orders = [
    {
      "customer_name": "Nicolas",
      "total": 100,
      "delivered": True,
    },
    {
      "customer_name": "Zulema",
      "total": 120,
      "delivered": False,
    },
    {
      "customer_name": "Santiago",
      "total": 20,
      "delivered": False,
    }
  ]
  
  total = get_total(orders)
  print(total)
  
if __name__ == "__main__":
  run()