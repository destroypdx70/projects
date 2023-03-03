set_countries = {"Col", "Mex", "Bol", "USA"}

size = len(set_countries)
print(size)

print("Col" in set_countries)
print("CAN" in set_countries)

# ADD
set_countries.add("CAN")
print(set_countries)
set_countries.add("CAN")
print(set_countries)

# UPDATE
set_countries.update({"AR", "ECU", "CAN"})
print(set_countries)

# REMOVE
set_countries.remove("USA")
print(set_countries)

set_countries.remove("Mex")
print(set_countries)

set_countries.discard("Mex")
print(set_countries)
set_countries.add("COL")
print(set_countries)

#CLEAR
set_countries.clear()
print(set_countries)
print(len(set_countries))

my_love = {"My real love", "Anyi", "My reason for exist", "I only go for my wife", "Anyi"}
print(my_love)

my_love.add("My only real love")
print("With add =>", my_love)

my_love.remove("My only real love")
print("With remove =>", my_love)

my_love.add("My only real love")
print("With add but again because I never leave my real love =>", my_love)

my_love.discard("Anyi")
print("With discard =>", my_love)

my_love.add("Anyi")
print("With add again because I never leave my real love =>", my_love)

my_love.clear()
print("With clear", my_love)
size = len(my_love)
print("size =>", size)

my_love.add("My real love")
print("Add again cause I never leave fall in love with you Anyi =>", my_love)

my_love.add("ANYI")
print("Add again cause I never leave fall in love with you Anyi =>", my_love)

my_love.add("My reason for exist")
print("Add again cause I never leave fall in love with you Anyi =>", my_love)

my_love.add("I only go for my wife")
print("Add again cause I never leave fall in love with you Anyi =>", my_love)

my_love.add("Anyi")
print("Add again cause I never leave fall in love with you Anyi =>", my_love)
