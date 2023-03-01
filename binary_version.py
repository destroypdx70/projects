def square_root_v1(x):
    goal = int(input("Choose a number => "))
    result = 0

    while result**2 < goal:
        result += 1
    if result**2 == goal:
        print(f"The square root of {goal} is {result}")
    else:
        print(f"{goal} did not have been found")
    return result