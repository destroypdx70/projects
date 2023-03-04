def divide_elements_of_list(list, divisor):
    try:
        return [i / divisor for i in list]
    except ZeroDivisionError as error:
        print(error)
        return list

list = list(range(10))
divisor = 0

print(divide_elements_of_list(list, divisor))
