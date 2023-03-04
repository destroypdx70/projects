my_list_v2 = []
my_list = [1,2,3,4,5,6]
for number in my_list:
    if number % 2 == 0:
        my_list_v2.append(number * 2)

numbers_v0 = [number * 2 for number in my_list if number % 2 == 0]
print(numbers_v0)

numbers_v1 = list(filter(lambda x : x % 2 == 0, my_list))
print(my_list_v2)
print(numbers_v1)

my_new_tuple = (1,)
my_tuple_2 = (2,3,4)
my_new_list = list(my_new_tuple)
my_new_tuple_v2 = tuple(my_list_v2)
my_new_tuple += my_tuple_2
print(my_new_tuple)
x, y, z, k = my_new_tuple
print(x)

def coordinates():
    return (5, 6)

x, y = coordinates()
print(x, y)