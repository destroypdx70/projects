number_1 = int(input("Write a number => "))
number_2 = int(input("Write a number => "))

if number_1 == number_2:
    print(f"{number_1} has the same value of {number_2}")
elif number_1 > number_2:
    print(f"{number_1} is mayor than {number_2}")
else:
    print(f"{number_2} is mayor than {number_1}")


number_1 = int(input("Write here a number => "))
number_2 = int(input("Write here a number => "))

if number_1 > number_2:
    print(f"{number_1} is mayor than {number_2}")
elif number_1 < number_2:
    print(f"{number_2} is mayor than {number_1}")
else:
    print("Both numbers are the same")
