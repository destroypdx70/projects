'''
try:
  print(0 / 0)
except ZeroDivisionError as error:
  print(error)

try:
  assert 1 != 1, "One it is the same that one"
except AssertionError as error:
  print(error)

try:
  age = int(input("Write here your age => "))
  if age < 18:
    raise Exception("Minors are not allowed")
except Exception as error:
  print(error)

try:
  print(0 / 0)
  assert 1 != 1, "One it is the same that one"
  age = int(input("Write here your age => "))
  if age < 18:
    raise Exception("Minors are not allowed")
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

def div(a, b):
  try:
    result = a / b
  except ZeroDivisionError as error:
    result = "Can not by divized by zero"
  return result

response = div(0, 0)
print(response)
response = div(4, 2)
print(response)
'''

def div(a, b):
  try:
    result = (a / b)
  except ZeroDivisionError as error:
    result = "Can not divise by zero"
  return result

response = div(0, 0)
print(response)
response = div(45, 90)
print(response)

try:
  print(0 / 0)
  assert 1 != 1, "One it is the same that one"
  age = int(input("Write here your age => "))
  if age < 18:
    raise Exception("Minors are not allowed")
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

















