def increment(x):
  return x + 1

increment_v2 = lambda x : x + 1


result = increment(10)
print(result)

result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f"My name is {name.title()} and my last name is {last_name.title()}"

text = full_name("Anyi", "Gallego")
print(text)

name = ["Anyi"]
last_name = ["Gallego"]

print(list(zip(name, last_name)))

full_name = { name: last_name for (name, last_name) in zip(name, last_name) }
print(full_name)

def increment(x):
  return x * 2

result = increment(80)
print(result)
result_v2 = increment(result)
print(result_v2)

increment_v2 = lambda x : x * 2

result_v3 = increment_v2(80)
print(result_v3)
result_v4 = increment(result_v3)
print(result_v4)


full_name = lambda name, last_name: f"My name is {name.title()} and my last name is {last_name.title()}"

text = full_name("Anyi", "Gallego")
print(text)

def increment(x):
  return x * 2

result = increment(92)
print(result)
result_v2 = increment(result)
print(result_v2)

increment_v2 = lambda x : x * 2

result_v3 = increment_v2(49)
print(result_v3)
result_v4 = increment_v2(result_v3)
print(result_v4)

full_name = lambda name, last_name: f"My name is {name.title()} and my last name is {last_name.title()}"

text = full_name("Anyi", "Gallego")
print(text)














