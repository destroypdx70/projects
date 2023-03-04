def divide_elements(list, divisor):
    try:
        [i / divisor for i in list]
    except ZeroDivisionError as error:
        print(error)
        return list
        
list = list(range(10))
divisor = 0

print(divide_elements(list, divisor))

