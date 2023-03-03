'''
set_a = {"COL", "MEX", "BOL"}
set_b = {"PER", "BOL"}

set_a_b = set_a.union(set_b)
print(set_a_b)
print(set_a | set_b)

set_a_b = set_a.intersection(set_b)
print(set_a_b)
print(set_a & set_b)

set_a_b = set_a.difference(set_b)
print(set_a_b)
print(set_a - set_b)

set_a_b = set_a.symmetric_difference(set_b)
print(set_a_b)
print(set_a ^ set_b)

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()

new_set = countries.union (northAm, centralAm, southAm)
print(new_set)
print(countries | northAm | centralAm | southAm)

new_set = countries.symmetric_difference(northAm)
print(new_set)
print(countries ^ northAm ^ centralAm ^ southAm)

new_set = countries.intersection(northAm, centralAm, southAm)
print(new_set)
print(countries & northAm & centralAm & southAm)

new_set = countries.difference(northAm, centralAm, southAm)
print(new_set)
print(countries - northAm - centralAm - southAm)
'''
set_consoles = {"Ps5", "Xbox 360", "Wii", "Nintendo", "Ps3", "Ps2"}
set_consoles_old = {"Super nintendo", "Ps1", "Gamecube", "Ps2"}

set_thewhole_consoles = set_consoles.union(set_consoles_old)
print(set_thewhole_consoles)
print(set_consoles | set_consoles_old)

set_thewhole_consoles = set_consoles.intersection(set_consoles_old)
print(set_thewhole_consoles)
print(set_consoles & set_consoles_old)

set_thewhole_consoles = set_consoles.difference(set_consoles_old)
print(set_thewhole_consoles)
print(set_consoles - set_consoles_old)

set_thewhole_consoles = set_consoles.symmetric_difference(set_consoles_old)
print(set_thewhole_consoles)
print(set_consoles ^ set_consoles_old)

set_consoles.add("Nintendo switch")
print(set_consoles)
print(set_consoles | set_consoles_old)