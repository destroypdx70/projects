'''
file = open("./text.txt")
print(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

for line in file:
  print(line)

with open("./text.txt"):
  for line in file:
    print(line)

file = open("./text.txt")
print(file.read())

print(file.readline())
print(file.readline())

file.close()

for line in file:
  print(line)

with open("./text.txt"):
  for line in file:
    print(line)  
'''
file = open("./text.txt")

# print(file.read())
# print(file.readline())

# file.close()

# for line in file:
 # print(line)

with open("./text.txt"):
  for line in file:
    print(line)



