def square_root_v1():
    goal = int(input("Choose a number => "))
    result = 0

    while result**2 < goal:
        result += 1
    if result**2 == goal:
        print(f"The square root of {goal} is {result}")
    else:
        print(f"{goal} did not have been found")
    return result

def square_root_v2():
    goal = int(input("Choose a number => "))
    epsilon = 0.01
    step = epsilon**2
    result = 0.0

    while abs(result**2 - goal) >= epsilon and result <= goal:
        result += step
    if abs(result**2 - goal) >= epsilon:
        print(f"{goal} did not have been found")
    else:
        print(f"The square root of {goal} is {result}")
    return result

def square_root_v3():
    goal = int(input("Choose a number => "))
    epsilon = 0.01
    limit = 0.0
    maximun = max(1.0, goal)
    result = (maximun + limit) / 2

    while abs(result**2 - goal) >= epsilon:
        print(f"limit => {limit}, maximun => {maximun}, result => {result}")
        if result**2 < goal:
            limit = result
        else:
            maximun = result
        
        result = (maximun + limit) / 2

    print(f"The square root of {goal} is {result}")
    return result
        
if __name__ == "__main__":
    square_root_v1()
    square_root_v2()
    square_root_v3()