'''
import functools

numbers = [1, 2, 3, 4, 5, 6,]

def accum(counter, item):
  print("Counter =>", counter)
  print("Item =>", item)
  return counter + item


result = functools.reduce(accum, numbers)
print(result)


result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

import functools

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def accumm(counter, item):
  print("Counter =>", counter)
  print("Item =>", item)
  return counter + item



result = functools.reduce(lambda counter, item : counter + item, numbers)
print(result)

result_v2 = functools.reduce(accumm, numbers)
print(result_v2)

import functools

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def accum(counter, item):
  print("Counter =>", counter)
  print("Item =>", item)
  return counter + item


result = functools.reduce(lambda counter, item : counter + item, numbers)
print(result)

result_v2 = functools.reduce(accum, numbers)
print(result_v2)

import functools

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def accum(counter, item):
  print("Counter =>", counter)
  print("Item =>", item)
  return counter + item

result = functools.reduce(lambda counter, item : counter + item, numbers)
print(result)
result = functools.reduce(accum, numbers)
print(result)
'''
import functools

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def accum(counter, item):
  print("Counter =>", counter)
  print("Item =>", item)
  return counter + item

result_v1 = functools.reduce(lambda counter, item : counter + item, numbers)
print(result_v1)

result_v2 = functools.reduce(accum, numbers)
print(result_v2)

numbers_v99 = [1, 2, 3, 5, 4, 2, 3]
numbers_v07 = [67, 32, 3, 4, 56, 1, 1]

result = list(map(lambda x, y : x * y, numbers_v99, numbers_v07))
print(result)










