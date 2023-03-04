def summ(min, max):
    """ Sum from the min value to max value
    param int min anyinteger
    param int max anyinteger
    returns the sum of min and max
    """         

    print(f"min => {min} max => {max}")
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

result = summ(10, 20)
print(result)

def increment(x):
    return x * 2

increment_2 = lambda x : x * 2

def high_order_functions(x, func):
    return x * func(x)

high_order_function_v2 = lambda x, func : x * func(x)

full_name = lambda name, last_name, age : f"My name is {name.title()}, my last name is {last_name.title()}, I am {age} years"
result_v2 = full_name("Anyi", "Gallego", 17)

text = "Anyi is my real love"
result_v3 = {c: c.upper() for c in text if c in "aeiou"}
result_v4 = {c: text.count(c) for c in text if c in "aeiou"}

help(summ)