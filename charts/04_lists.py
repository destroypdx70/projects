numbers = []
for element in range(1, 11):
  numbers.append(element * 2)

print(numbers)

numbers_V2 = [element * 2 for element in range(1, 11)]
print(numbers_V2)

numbers = []
for i in range(1, 11):
  if i % 2 == 0:
     numbers.append(i * 2)

print(numbers)

numbers_V2 = [i * 2 for i in range(1, 11)if i % 2 == 0]
print(numbers_V2)

print(34 in numbers_V2)

numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# List Comprehension 
even_numbers_v2 = [number for number in numbers if number % 2 == 0]

print('v2 =>', even_numbers_v2)

def run():
    text = "Hola a todos, esta es una cadena de texto de prueba."
    print(text)
    unique = { c: text.count(c) for c in text if c in 'aeiou' }
    print(f"unique: {unique}")

if __name__ == '__main__':
    run()


numbers = []
for number in range(1, 101):
  if number < 71:
    numbers.append(number)

print(numbers)

numbers_v2 = [number for number in range(1, 101) if number < 71]
print(numbers_v2)

numbers = []
for number in range(40, 118):
  if number < 87:
    numbers.append(number)
print(numbers)

numbers_v2 = [number for number in range(40, 118) if number < 87]

numbers = []
for number in range(200, 1899):
  if number < 1498:
    numbers.append(number)
    
print(numbers)

numbers_v2 = [number for number in range(200, 1899) if number < 1498]

set_console_new = {"Ps2", "Ps3"}
set_console_old = {"Ps1"}
set_thewhole_consoles = (set_console_new.union(set_console_old))
print(set_thewhole_consoles)
print(set_console_new | set_console_old)

shopping_car = []

for console in set_thewhole_consoles:
  if console == "Ps1":
    shopping_car.append(console)
    print("Old console =>", console)
    
print("Shopping car =>", shopping_car)

shopping_car_V2 = [console for console in set_thewhole_consoles if console == "Ps1"]
print(shopping_car_V2)

numbers_v3 = []
for number in range(1, 101):
  if number < 70:
    numbers_v3.append(number * 4)
    
print("The new numbers =>", numbers)

numbers_v4 = [number * 4 for number in range(1, 101) if number < 70]
print("The new numbers =>", numbers_v4)

numbers_v5 = []
for number in range(57, 907):
  if number % 2 == 0:
    numbers_v5.append(number)

print("The old numbers =>", numbers_v5)

numbers_v6 = [number for number in range(57, 907) if number % 2 == 0]
print("The new numbers =>", numbers_v6)

set_console_new = {"Ps4", "Xbox One", "Ps5", "Nintendo swich"}
set_console_old = {"Ps2", "Ps1", "Ps4 Slim", "Ps4 Pro", "Ps4", "Nintendo switch"}
set_thewhole_consoles = set_console_new.union(set_console_old)
print(set_thewhole_consoles)
print(set_console_new | set_console_old)

shopping_car = []
for console in set_thewhole_consoles:
  if console == "Ps4 Slim":
    shopping_car.append(console)
print("With for =>", shopping_car)

shopping_car_v2 = [console for console in set_thewhole_consoles if console == "Ps4 Slim"]
print("With list comprehension", shopping_car)



numbers = []
for number in range(1, 70):
  if number % 2 == 0:
    numbers.append(number)
    
print(numbers)

numbers_v2 = [number for number in range(1, 70) if number % 2 == 0]
print(numbers_v2)


numbers_v3 = []
for number in range(1, 70):
  if number % 2 == 0:
    numbers_v3.append(number * 2)
print(numbers_v3)


numbers_v4 = [number * 2 for number in range(1, 70) if number % 2 == 0]
print(numbers_v4)

numbers_v5 = []
for number in range(1, 10000):
  if number % 2 == 0:
    numbers_v5.append(number / 2)
print("numbers v5 =>", numbers_v5)

numbers_v6 = [number / 2 for number in range(1, 10000) if number % 2 == 0]
print("numbers v6 =>", numbers_v6)

numbers_v9 = []
for number in range(1, 70):
  if number % 2 == 0:
    numbers_v9.append(number)
print(numbers_v9)

numbers_v10 = [number for number in range(1, 70) if number % 2 == 0]
print("Numbers version 10 =>", numbers_v10)

numbers_v11 = []
for number in range(1, 70):
  if number % 2 == 0:
    numbers_v11.append(number * 3)
print(numbers_v11)

numbers_v11 = [number * 3 for number in range(1, 70) if number % 2 == 0]
print("Numbers version 11 =>", numbers_v11)
                    
list_numbers = []
for number in range(1, 70):
  if number % 2 == 0:
    list_numbers.append(number)
print("list numbers v1 =>", list_numbers)

list_numbers_v2 = [number for number in range(1, 70) if number % 2 == 0]
print("list numbers v2 =>", list_numbers_v2)





