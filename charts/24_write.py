'''
with open("./text.txt", "w+") as file:
  for line in file:
    print(line)
  file.write("My love is incredible\n")

with open("./text.txt", "r+") as file:
  for line in file:
    print(line)
  file.write("My real love is Anyi\n")

with open("./text.txt", "w+") as file:
  for line in file:
    print(line)
  file.write("My real love is Anyi\n")

with open("./text.txt", "w+") as file:
  for line in file:
    print(line)
  file.write("My real love is Anyi\n")
'''
# file = open("./text.txt")
# print(file.readline())
# print(file.read())

# file.close()

# for line in file:
 # print(line)

with open("./text.txt", "r+") as file:
  for line in file:
    print(line)
  file.write("Anyi is my real love\n")
  file.write("I never leave my real love\n")











