'''
sum = 0
for x in range(1, 11):
  sum += x
print(sum)



def sum_with_range(min, max):
  print("min =>", min, "max =>", max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)
result_3 = sum_with_range(result_2, result_2 + 10)
print(result_3)

def summation_definity(min, max):
  print("min =>", min, "=>", max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result_1 = summation_definity(1, 10)
print(result_1)
result_2 = summation_definity(result_1, result_1 * 2)
print(result_2)

'''
def summation(min, max):
  print("min =>", min, "max =>", max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result_1 = summation(7, 90)
print(result_1)
result_2 = summation(result_1, result_1 * 3)
print(result_2)














