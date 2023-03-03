my_real_family = {"Anyi", "Noah", "Child", "Children"}
print(my_real_family)
my_real_family_eli = {"Elizabeth", "Child", "Children"}
print(my_real_family_eli)

my_family_complete = (my_real_family | my_real_family_eli)
print(my_family_complete)
print(my_real_family.union(my_real_family_eli))

my_family_complete = (my_real_family & my_real_family_eli)
print(my_real_family.intersection(my_real_family_eli))

my_family_complete = (my_real_family - my_real_family_eli)
print(my_family_complete)
print(my_real_family.difference(my_real_family_eli))

my_family_complete = (my_real_family ^ my_real_family_eli)
print(my_family_complete)
print(my_real_family.symmetric_difference(my_real_family_eli))

my_family_complete.add("Eliot")
print(my_real_family)

my_family_complete.update({"Child number 2", "Child number 3"})
print(my_real_family)

my_family_complete.remove("Child number 2")
my_family_complete.remove("Child number 3")
print(my_real_family)

my_family_complete.discard("Mi wife")
print(my_real_family)

my_family_complete.clear()
print(my_family_complete)
