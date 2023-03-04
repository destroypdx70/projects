my_range = range(1, 5)
for i in my_range:
    print(i)

my_other_range = range(0, 9, 3)
for i in my_other_range:
    print(i)

one_hundred = range(1, 101)
col = 1
for i in one_hundred:
    if (col<10):
        print(f"{i}\t", end="")
        col += 1
    else:
        print(i)
        col = 1
    

one_hundred_v2 = range(0, 101, 2)
for i in one_hundred_v2:
    print(i)

one_hundred_v3 = range(1, 100, )
for i in one_hundred_v3:
    print(i )

